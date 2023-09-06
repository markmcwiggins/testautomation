#!/usr/bin/env python3
import os
import sys
from slack_sdk import WebClient

slackuser = sys.argv[1]
hash = sys.argv[2]

# Set your OAuth Access Token
SLACK_TOKEN = os.getenv('SLACK_TOKEN')

# Initialize the Slack WebClient
client = WebClient(token=SLACK_TOKEN)

def send_message(channel, message):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message,
            username='<mark>'
        )
        if response['ok']:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    channel = "test-automation" 
    message = "user <%s> broke the build with commit <%s>" % (slackuser, hash)
    send_message(channel, message)
