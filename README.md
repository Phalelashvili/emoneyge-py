Unofficial eMoney.ge Client for Python
=======

Installation
============

```
pip install emoneyge-py
```

Usage
=======
pincode is whatever method you're using to confirm transactions, can be password or even sms
```python
from emoney import eMoneyClient
client = eMoneyClient()
client.login('username', 'password', pincode=pincode)
```
if you have SMS, or Google Authentication
```python
client.send_code()
sms = # received code
client.login('username', 'password', googleauthcode='foobar', smsauthcode=sms)
```
```
Get Balance
```python
client.get_balance()
```
Get transaction
```python
client.get_transaction(transactioncode)
```
Request money
```python
client.request_money(sender, amount)
```
Send money
currency you're sending, default is GEL, default is GEL, accepts GEL, USD, EUR, RUB, AMD, AMZ, UAH
description of transaction (optional)  
if given value between 0 and 5, function will return security code which must be used by recipient to redeem money, value is amount of days till it expires
```python
client.send_money(receiver, amount, currency='GEL', description='', protect: 5)
```
Cancel transaction
```python
client.cancel_transaction(transactioncode)
```
