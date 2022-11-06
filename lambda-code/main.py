#!/usr/bin/python3

import os
import boto3

client     = boto3.client('ses')
debug      = os.environ['DEBUG'].upper() if 'DEBUG' in os.environ.keys() else 'FALSE'
production = os.environ['PRODUCTION'].upper() if 'PRODUCTION' in os.environ.keys() else 'FALSE'

def print_environment():
    print_debug(os.environ.items())

def disable_sending():
    if (production == 'FALSE'):
        return

    response = client.update_account_sending_enabled(
        Enabled=False
    )
    print_debug(response)

def check_sending_status():
    response = client.get_account_sending_enabled()
    print_debug(response)

def print_debug(response):
    if (debug == 'TRUE'):
        print(response)

def lambda_handler(event, context):
    print_debug(event)
    print_debug(context)
    main()

def main():
    print_environment()
    check_sending_status()
    disable_sending()
    check_sending_status()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()