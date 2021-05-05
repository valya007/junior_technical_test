Instructions:

Please make sure that gunicorn (version 20.1.0) is installed:
https://docs.gunicorn.org/en/stable/install.html

Go to downloaded folder where webapp.py is located
Launch gunicorn with foloowing arguments: 

gunicorn webapp:main --reload

If successful the following lines will be displayed:

[32154] [INFO] Starting gunicorn 20.1.0 

[32154] [INFO] Listening at: http://127.0.0.1:8000 (32154)

Follow the url that gunicorn is listening at.
Hopefully you'll see the request to enter a sentence and be able to get an expected answer :)

