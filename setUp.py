# using FLASK set up

# export variable FLASK_APP to locate the app -> write into terminal
export FLASK_APP=server.py

# to run the server
python -m flask run

# to turn off debug mode -> no need to restart the server all the time
export FLASK_ENV=development