# Sample bot used for medical appointment scheduling

## Using with Rasa X

1. install requirements.txt
2. into root directory: python3 -m rasa x (copy obtained url path - it contains password for webservise)
3. into root directory: python3 -m rasa run actions
4. ngrok http 5002


## for using telegram
1. ngrok http 5005
2. copy obtained https address and paste it into file credentials.yml / line webhook_url
3. into root directory: python3 -m rasa run
4. into root directory: python3 -m rasa run actions
5. @Medical_AssistantBot in the Telegram 