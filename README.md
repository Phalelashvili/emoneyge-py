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
Receive SMS authentication code
```python
client.send_code()
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