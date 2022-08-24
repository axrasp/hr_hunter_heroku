#Parse HRs from Telegram

This code allows you to obtain HRs Telegram IDs form open chats and send them any message (maybe it's your CV).

ATTENTION: The authors of the code are not responsible for immoral and illegal ways of using it. 
Don't be assholes.

##Installing

Python3 shoulbe installed. Then use ``pip`` (or ``pip3``) for installing dependencies:

```
pip install -r requirements.txt
```

Create file ``.env`` in project root directory and place there Telegramm app data like this:

```
API_ID=16277445
API_HASH='12asfad3'
USERNAME=''
```

Additional info here:
https://my.telegram.org/auth?to=apps


## Lanuching

Start the code using 

```
python3 parser.py 
```

