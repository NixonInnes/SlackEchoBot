# SlackEchoBot

### INTRODUCTION
This is a simple echo bot written for Slack  
The bot will echo any text sent by a user if their message begins with "echo".  

Example:  
NixonInnes: echo Hello, World!  
EchoBot: Hello, World!  

### PREREQUISITES
You will need to get a token from your Slack to allow it to connect to the service.  
See: https://api.slack.com/bot-users  

If you are using a public Slack, and don't have permission to create a token, you can set up your own Slack to test the bot within.  
You will need to add the token into an environment variable, called SLACK_TOKEN.  

### PACKAGES
We're using slackclient; documentation for it can be seen here:  
https://github.com/slackhq/python-slackclient
