# Python imap to elasticsearch

This script monitors a IMAP mailbox and writes the incoming mails in JSON-format to a file. 
The file can be read by filebeat, to forward it to logstash / elasticsearch
Adding the script to a cronjob allows to repeat this every X.

## Requirements

``pip3 install mail-parser``

## Usage

``python3 mail.py``
