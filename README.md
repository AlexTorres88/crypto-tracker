# Purpose

The purpose of this project is to store the data collected by the azure-crypto-scraper I made and use it for something down in the road. 

# Setup 

First of all, you should activate the virtual environment:
````
source/bin/activate
````
After that, run:
````
pip install -r requirements.txt
````
Now export the environment variables in the cli using:
````
export FLASK_APP=flaskr
`````
and 
`````
export FLASK_ENV=development
`````

All that is left is to setup the environment variables located in the settings.py file (Remember to rename your settings.example.py file to this) and then run:
````
flask run
`````
