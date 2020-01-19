# Python imap to elasticsearch

This script monitors a IMAP mailbox and writes the incoming mails to a file in JSON-format (line by line).
The output file can be read by filebeat, to forward the e-mails to logstash / elasticsearch.
Adding the script to a cronjob allows to repeat this every X.

Note: The script automatically deletes all e-mail messages processed.

## Requirements

``pip3 install mail-parser``

Modify the imap host, username and password variables in mail.py

## Usage

``python3 mail.py``
