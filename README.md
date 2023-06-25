BitcoinMessageTools
======

An online web application for signing and verification of bitcoin messages.

A web user interface for https://github.com/shadowy-pycoder/bitcoin_message_tool

Installation
------------

If you have Docker installed:

Clone the repository

    git clone https://github.com/shadowy-pycoder/BitcoinMessageTools.git

Switch to the project directory

    cd BitcoinMessageTools

Run a docker compose yaml file in detached mode

    docker compose -f docker-compose.dev.yml up -d

If you don't have Docker installed:

Clone the repository

    git clone https://github.com/shadowy-pycoder/BitcoinMessageTools.git

Switch to the project directory

    cd BitcoinMessageTools/web

Create new virtual enviroment

    python3.10 -m venv env
    
    source env/bin/activate

Install project dependencies

    pip install -r requirements.txt

Create a secret key for Flask app

    export SECRET_KEY=<some_random_data>

Start the programm

    python run.py

Go to localhost:5000 in your browser and your shoud see a website running offline.

Quickstart Guide
----------------

TODO - fill this in later

Contribute
----------

If you'd like to contribute to BitcoinMessageTools, check out https://github.com/shadowy-pycoder/BitcoinMessageTools
