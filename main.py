import os
from price_gun import pricecheck
from send_mail import notify_user


# variables needed to pass into requests module
# amazon will mask HTML / raise an error otherwise


AMAZON_URL = os.environ['AZ_URL']
REQUEST_HEADER = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Accept-Language': 'en-US',
}

# SMTP variables

GMAIL_USER = os.environ['G_USER']
GMAIL_PW = os.environ['G_PW']
TO_USER = os.environ['TO_USR']


user_from = GMAIL_USER
body_text = 'scrampo scrimpo bimpo banbmo'

target_price = 50
current_price = pricecheck(url=AMAZON_URL, request_header=REQUEST_HEADER)

if current_price < target_price:
    notify_user(GMAIL_USER, GMAIL_PW, user_from, TO_USER, body_text)
