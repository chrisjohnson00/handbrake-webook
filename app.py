from flask import Flask, request
import logging
from api_client.client import get_full_file_path, get_quality_level

application = Flask(__name__)
application.logger.setLevel(logging.INFO)
required_configs = []


@application.route('/')
def index():
    return 'Welcome to the Handbrake Webhook Server!'


@application.route('/webhook', methods=['GET', 'POST'])
def web_hook():
    application.logger.info("Web hook called")
    application.logger.info("Web hook headers: {}".format(request.headers))
    application.logger.info("Web hook data: {}".format(request.get_json()))
    application.logger.info("Calculated file path is {}".format(get_full_file_path(request.get_json())))
    application.logger.info("Calculated quality level is {}".format(get_quality_level(request.get_json())))
    return 'Done'


@application.route('/health')
def health_check():
    # put logic here to ensure we are happy to fulfill user requests
    return "Success"


@application.route('/config')
def config():
    application.logger.info("Rendering config page")
    response_text = ""
    for config in required_configs:
        value = application.config.get(config)
        if any(secret in config for secret in ['KEY', 'TOKEN', 'PASSWORD']):
            response_text += "{}: [REDACTED]<br/>".format(config)
        else:
            response_text += "{}: {}<br/>".format(config, value)
    return response_text


def move_file(src, dest):
    command = ["mv", src, dest]
    application.logger.info("File move command called {}".format(command))
    # subprocess.run(command, check=True)


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80)
