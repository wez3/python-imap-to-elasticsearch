#!/usr/bin/python3

import imaplib
import mailparser
import json

imap_host = ''
imap_user = ''
imap_pass = ''

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

# login to server
imap.login(imap_user, imap_pass)

# open the output file
output = open('/tmp/mail.json', 'a')

# select the imap folder
imap.select('Inbox')

# select all mails
tmp, data = imap.search(None, 'ALL')

# loop through the emails
for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')
    mail = mailparser.parse_from_bytes(data[0][1])

    json.dump(json.loads(mail.mail_json), output)
    output.write("\r\n")

    imap.store(num, '+FLAGS', '\\Deleted')

imap.expunge()
imap.close()