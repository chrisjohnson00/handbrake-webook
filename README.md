# handbrake-webook
A webhook receiver for Sonarr/Radarr that copies files for the handbrake pipeline

## Local setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run Locally

    export watch1080p=/1080p
    export watch720p=/720p
    flask run
