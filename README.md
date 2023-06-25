BitcoinMessageTools
======

An online web application for signing and verification of bitcoin messages.

A web user interface for https://github.com/shadowy-pycoder/bitcoin_message_tool

Installation
------------

If you have Docker installed:

    git clone https://github.com/shadowy-pycoder/BitcoinMessageTools.git

    cd BitcoinMessageTools

    docker compose -f docker-compose.dev.yml up -d

If you don't have Docker installed:

    git clone https://github.com/shadowy-pycoder/BitcoinMessageTools.git

    cd BitcoinMessageTools/web

    python3.10 -m venv env
    
    source env/bin/activate

    pip install -r requirements.txt

    export SECRET_KEY=<some_random_data>

    python run.py

Go to localhost:5000 in your browser and your shoud see a website running offline.

Quickstart Guide
----------------

TODO - fill this in later

Contribute
----------

If you'd like to contribute to BitcoinMessageTools, check out https://github.com/shadowy-pycoder/BitcoinMessageTools
