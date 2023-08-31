#!/usr/bin/env python3
import os
from slack_sdk import WebClient

# Set your OAuth Access Token
SLACK_TOKEN = os.getenv('SLACK_TOKEN')

# Initialize the Slack WebClient
client = WebClient(token=SLACK_TOKEN)

def send_message(user_id, message):
    try:
        response = client.chat_postMessage(
            channel=user_id,
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
    user_id = "test-automation"  # Replace with the user's Slack ID
    message = "user <mark> broke the build with commit sdflkjsdfl"
    send_message(user_id, message)
