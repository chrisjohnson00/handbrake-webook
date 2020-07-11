from flask import Flask, request
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
required_configs = []


@app.route('/')
def index():
    return 'Welcome to the Handbrake Webhook Server!'


@app.route('/webhook', methods=['GET', 'POST'])
def web_hook():
    app.logger.info("Web hook called")
    app.logger.info("Web hook headers: {}".format(request.headers))
    app.logger.info("Web hook data: {}".format(request.get_json()))
    return 'Done'


@app.route('/health')
def health_check():
    # put logic here to ensure we are happy to fulfill user requests
    return "Success"


@app.route('/config')
def config():
    app.logger.info("Rendering config page")
    response_text = ""
    for config in required_configs:
        value = app.config.get(config)
        if any(secret in config for secret in ['KEY', 'TOKEN', 'PASSWORD']):
            response_text += "{}: [REDACTED]<br/>".format(config)
        else:
            response_text += "{}: {}<br/>".format(config, value)
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
