"""
INTRODUCTION
=============
This is a simple echo bot written for Slack
The bot will echo any text sent by a user if their message begins with "echo".

Example:
--------
NixonInnes: echo Hello, World!
EchoBot: Hello, World!


PREREQUISITES
==============
You will need to get a token from your Slack to allow it to connect to the service.
See: https://api.slack.com/bot-users

If you are using a public Slack, and don't have permission to create a token, you can
set up your own Slack to test the bot within.

You will need to add the token into an environment variable, called SLACK_TOKEN.


PACKAGES
=========
We're using slackclient; documentation for it can be seen here:
https://github.com/slackhq/python-slackclient

"""

import os
import time
from slackclient import SlackClient

# Get the token from env
token = os.getenv('SLACK_TOKEN', '')


def main():
    """
    Creates a Slack client.
    If the client has connected the program enters into an infinite loop.
    Check for any new events with SlackClient.rtm_read().
    Iterate through the new events
    If the event is a message, and the first word in the text is 'echo'
    Then the client sends the message back to the channel
    At the end of each loop, the client waits 1 second to prevent spamming the Slack
    """

    client = SlackClient(token)

    if client.rtm_connect():
        while True:
            new_events = client.rtm_read()
            for event in new_events:
                if event.get('type') == 'message':
                    msg = event['text']
                    if len(msg) > 0 and msg.split()[0] == 'echo':
                        response = ' '.join(msg.split()[1:])
                        client.rtm_send_message(event['channel'], response)
            time.sleep(1)


if __name__ == '__main__':
    main()
