# DistanceTracker
Description:
This application allows you to upload and track any distance based workout that you complete, such as a walk, run, or bicycle ride.
In a later version, the ability to edit workouts, delete them, and visualize progress will be added.

Needed Environment:
TERM_PROGRAM=Apple_Terminal
SHELL=/bin/bash
TERM=xterm-256color
TMPDIR=/var/folders/0r/4q31g91x7c18664lr0vcqx_80000gn/T/
TERM_PROGRAM_VERSION=440
OLDPWD=/Users/kaylaellis
TERM_SESSION_ID=032F841A-E2D3-4D8C-A896-81E741E91E3A
FLASK_APP=distance_tracker
USER=kaylaellis
SSH_AUTH_SOCK=/private/tmp/com.apple.launchd.93pqB1X4v5/Listeners
PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/Library/Frameworks/Python.framework/Versions/3.8/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware Fusion.app/Contents/Public
__CFBundleIdentifier=com.apple.Terminal
PWD=/Users/kaylaellis/Documents/DistanceTracker
LANG=en_US.UTF-8
XPC_FLAGS=0x0
XPC_SERVICE_NAME=0
SHLVL=1
HOME=/Users/kaylaellis
LOGNAME=kaylaellis
_=/usr/bin/printenv

Run On:
macOS Big Sur
Version 11.1

Needed libraries and resources:
aenum==3.0.0
aiohttp==3.7.4.post0
appdirs==1.4.4
async-timeout==3.0.1
attrs==20.3.0
bandit==1.7.0
cachelib==0.1.1
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
distlib==0.3.1
dnspython==2.1.0
ecdsa==0.14.1
filelock==3.0.12
Flask==1.1.2
Flask-Login==0.5.0
Flask-Session==0.3.2
Flask-SQLAlchemy==2.5.1
flatdict==4.0.1
gitdb==4.0.7
GitPython==3.1.14
greenlet==1.0.0
idna==3.1
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
multidict==5.1.0
okta==1.6.0
pbr==5.6.0
pyasn1==0.4.8
pycryptodome==3.10.1
pydash==5.0.0
pymongo==3.11.3
python-jose==3.2.0
PyYAML==5.4.1
rsa==4.7.2
sentry-sdk==1.0.0
six==1.15.0
smmap==4.0.0
SQLAlchemy==1.4.12
stevedore==3.3.0
tk==0.1.0
typing-extensions==3.7.4.3
urllib3==1.26.4
virtualenv==20.4.4
Werkzeug==1.0.1
xmltodict==0.12.0
yarl==1.6.3

Process to run the application:
1. Install all needed requirements from the requirements.txt file or from the list listed about
2. Navigate to the parent folder for the project using your terminal (e.g. cd ~/Documents/DistanceTracker)
3. Type the command export FLASK_APP=distance_tracker
4. Type the command flask run

    The application will now be running on http://127.0.0.1:5000/
