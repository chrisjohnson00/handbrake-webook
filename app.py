from flask import Flask, request
import logging
import os
import consul
from json import dumps
from kafka import KafkaProducer, KafkaClient
from api_client.client import get_full_file_path, get_quality_level

application = Flask(__name__)
application.logger.setLevel(logging.INFO)
required_configs = ['KAFKA_TOPIC', 'KAFKA_SERVER']
CONFIG_PATH = "handbrake-webhook"


@application.route('/')
def index():
    return 'Welcome to the Handbrake Webhook Server!'


@application.route('/webhook', methods=['POST'])
def web_hook():
    producer = KafkaProducer(bootstrap_servers=[get_config('KAFKA_SERVER')],
                             acks=1,
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    application.logger.info("Web hook called")
    application.logger.info("Web hook headers: {}".format(request.headers))
    application.logger.info("Web hook data: {}".format(request.get_json()))
    application.logger.info("Calculated file path is {}".format(get_full_file_path(request.get_json())))
    application.logger.info("Calculated quality level is {}".format(get_quality_level(request.get_json())))
    kafka_message = {'source_full_path': get_full_file_path(request.get_json()), 'move_type': 'to_encode',
                     'type': 'tv', 'quality': get_quality_level(
            request.get_json())}
    application.logger.info("Sending message {} to topic '{}'".format(kafka_message, get_config("KAFKA_TOPIC")))
    future = producer.send(topic=get_config("KAFKA_TOPIC"),
                           value=kafka_message)
    result = future.get(timeout=60)

    return 'Done'


@application.route('/health')
def health_check():
    client = KafkaClient(bootstrap_servers=[get_config('KAFKA_SERVER')])
    if not client.bootstrap_connected():
        raise Exception("Unable to connect to Kafka: {}".format(get_config('KAFKA_SERVER')))
    return "Success"


@application.route('/config')
def config():
    application.logger.info("Rendering config page")
    response_text = ""
    for config in required_configs:
        value = get_config(config)
        if any(secret in config for secret in ['KEY', 'TOKEN', 'PASSWORD']):
            response_text += "{}: [REDACTED]<br/>".format(config)
        else:
            response_text += "{}: {}<br/>".format(config, value)
    return response_text


def get_config(key, config_path=CONFIG_PATH):
    if os.environ.get(key):
        return os.environ.get(key)
    c = consul.Consul()
    index, data = c.kv.get("{}/{}".format(config_path, key))
    return data['Value'].decode("utf-8")


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80)
