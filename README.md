Assumes you already have Bitcoin Core daemon (bitcoind) and c-lightning daemon (lightningd) installed and running

Assumes you have python and python pip already installed

Install virtualenv so we can set up an isolated build environment

sudo pip install virtualenv

Move to the home directory

cd

Set up a virtualenv workspace for our project

virtualenv python-django-workspace

Move into the new directory

cd python-django-workspace

Install components we will use: 
django as the web framework
lightningd rpc using https://github.com/ElementsProject/lightning/tree/master/contrib/pylightning
bitcoind rpc using https://github.com/jgarzik/python-bitcoinrpc

sudo python -m pip install "django<2"
sudo pip install pylightning
sudo pip install python-bitcoinrpc 

CONFIG:
todo - add u and p to settings file?
edit nodemonitor/dashboard/views.py and change:
rpc_port="8332"
    rpc_user="user82ue99fwo3049f7c8a8d93dkall2l1l11"
    rpc_password="passwordb084b7v85f7hd06s06d06fgd01shaj"

and you need to change this to make sure it points to your nodes "lightning-rpc" socket file:
ln = LightningRpc("/home/pi/.lightning/lightning-rpc")

find your machine's IP
ifconfig 
192.168.etc
let's say it is 192.188.1.150

use that and run the server using:

cd nodemonitor
python manage.py runserver 192.168.1.150:8000

http://127.0.0.1:8000/dashboard/

that actually uses the app in 'dashboard' which you can also get to via http://127.0.0.1:8000/dashboard/ - we just map the root url to that in the urls.py file.

If you want to make the website available to other machines locally or public you need to change debug=false. see here for how to do this:


You will want to also change the SECRET_KEY in settings.py as well - it should be set to a unique, unpredictable value. See here for details: https://docs.djangoproject.com/en/2.1/ref/settings/#secret-key

Also: 
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'


