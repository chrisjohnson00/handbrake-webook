# handbrake-webook
A webhook receiver for Sonarr/Radarr that copies files for the handbrake pipeline

## Local setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run Locally

    echo "Starting Kafka locally"
    docker-compose up -d
    export watch1080p=/1080p
    export watch720p=/720p
    export KAFKA_SERVER=localhost:9092
    export KAFKA_TOPIC=bla
    export FLASK_ENV=development
    flask run

## Updating PyPi deps

    pip install --upgrade pip Flask gunicorn kafka-python python-consul
    pip freeze > requirements.txt
    sed -i '/pkg-resources/d' requirements.txt
