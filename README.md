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
The last thing left to do is to set the file we will run. Just type set FLASK_APP=app.py. App.py is the name of the file.

##Usage

Now that we have set everything up, We will run the app and test it using postman.
Type flask run. This will run the app that you have set up before with "set FLASK_APP=app.py.
The prompt will give you the localhost address. For this example I will use 127.0.0.1:5000.
Now you type 127.0.0.1:5000/urls on postman. Set the method to GET.
This should give us the list of urls saved.
This service is not using a database to store the data. It uses a list intead. So, if you exit the application all the data will be lost.
If you want to search for a specific url just type 127.0.0.1:5000/urls/id where id is the id of that url. Each url will receive an id when saved in the list.
In order to store a new id we need to change the method to POST first.
Then we will click on import and then raw text.
We will type "curl -i -H "Content-Type: application/json" -X POST -d '{"long":"https://www.example.com"}' http://127.0.0.1:5000/urls".
This should add the url to the list, convert it to a short version and get the current time.
In order to see that information just get the urls as mentioned above.
If you want to delete a url from the list change the method to DELETE first and then just type 127.0.0.1:5000/id.
This should delete the url correspondent to the id you typed.
