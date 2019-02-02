Unofficial eMoney.ge Client for Python
=======

Installation
============

```
pip install emoneyge-py
```

Usage
=======

```python
from emoney import eMoneyClient
client = eMoneyClient()
client.login('username', 'password')
```
if you have SMS, Google Authentication
```python
client.send_code()
sms = # received code
client.login('username', 'password', googleauthcode='foobar', smsauthcode=sms)
```
