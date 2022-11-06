# AWS SES SPAM PROTECTOR [WIP]

Serverless Architecture to protect your AWS SES Account in case of your credentials was breached to internet.

Some examples that I've found in differents projects:

* Wrong application configuration (directory traversal) [OWASP](https://owasp.org/www-community/attacks/Path_Traversal)
* Debug mode enabled
* Public environment file (.env accessible from url)
* Public backup environment file (.env.txt, .env.example, .env.backup, .env.bak, .env.back)
* Vulnerable plugins
* Application outdated

This project has the abailability to deactivate the AWS SES sending status throught a python script hosted in lambda.

## Flow process

## Create lambda function

## Create notification topic

## Create cloudwatch alert

## Create ses identity

### Create identity policy

## Create iam smtp user

### Create iam policy

## Local debug