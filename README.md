# weather-bot
Rasa NLU/Core Weather Bot

Current configuration supports training, command-line interface and HTTP server API.

## Dependencies

- pip install rasa_nlu
- pip install rasa-core
- pip install weather-api

## Train

*python3 trainer.py train-all*

This will train both the NLU and Stories using Tensorflow machine learning.

## Run Server

*python3 -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current -o models/out.log*

Talk to the server through API as: *curl -XPOST localhost:5005/conversations/default/respond -d '{"query":"hi"}'*

Documentation: http://rasa.com/docs/core/http/

## Run action python class

*python3 -m rasa_core_sdk.endpoint --actions actions*
