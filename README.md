# UrlShortener

UrlShortener is a simple RESTful service developed in python and flask.
It can be used to make short versions of urls.

##Installation

FIrst of all you must have python installed in your computer. If you are using Linux this should not be a problem. If you are using Windows you can download the newest version of Python here:https://www.python.org/downloads/.
Make sure to have python 3 installed. If you are using linux you should check the version of Python by typing "python -V" or "python --version" on the shell window.
If your version is anything below 3 just update python by typing "sudo apt-get python3.8".
Now it is time to create a virtual environment.
Just type "python 3 -m venv env" on linux or "py -m venv env".
I am using env for this example but you can give any name to the envirnment.
In order to access or virtual environment type env/bin/activate on linux or env\Script\activate on windows.
Be sure to do this in the same folder you created the virtual environment.
When you see (env) before the path it means you are ready to go.
If you want to exit the environment just type "env/bin/deactivate" on linux or env\Script\deactivate on windows.
Now we need to install flask. Just type "pip install flask".
We will also need to install curl. Just type "pip install curl"
We will need postman to test the service. You can download postman here https://www.postman.com/downloads/.

##Usage

