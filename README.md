# Purpose

The purpose of this project is to store the data collected by the azure-crypto-scraper I made and use it for something down in the road. 

# Setup 

First of all, you should create the virtual environment (you need to have virtualenv installed):
````
virtualenv [env_name_here_without_brackets]
`````
Then, you should activate the virtual environment:
````
source [env_name_here]/bin/activate
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

You should also create a settings.py folder inside the flaskr directory with the necesarry env variables

`````
touch flaskr/settings.py
`````

All that is left is to setup the environment variables located in the settings.py file (Remember to rename your settings.example.py file to this) and then run:
````
flask run
`````

## Datadog Monitoring

It is really easy to configure datadog monitoring for this flask application.

First of all, you'll need to create an account on Datadog. I recommend using Github's Student Developer Pack to get 2 years of free Datadog services. 

After that, you need to install the Datadog Agent, you can do that [here.](https://app.datadoghq.com/account/settings?_gl=1*1t3z4bu*_ga*MTkyNzI2Njk5Mi4xNjI4NTM2MzUz*_ga_KN80RDFSQK*MTYzMDc2OTMwNC43LjEuMTYzMDc3MDQ4My4w&_ga=2.128954956.1356085242.1630732538-1927266992.1628536353#agent/overview)

All that is left to do is install the ddtrace package by running: 
`````
pip install ddtrace
`````
And then running:
`````
FLASK_APP=[name_of_your_app_without_brackets] DATADOG_ENV=flask_test ddtrace-run flask run --port=[port_you_want]
`````
*Default port is 4999
