import re

email = 'someone@gmail.com'
email2 = 'someon2e@gma2il.com'
email3 = 'someon#2e@gma2il.com'


def valid_email(e):
    s = r'^[\w\.]+@\w+.com'
    if (re.match(s, e)):
        print('ok')
    else:
        print('no ok')

valid_email(email)
valid_email(email2)
valid_email(email3)
