# Automation Eight Code test task

## Run applications: 

First of all, you need install all required dependencies: 

    pip install -r requirements.txt

or you can just run virtual environment: 

    source access_points/bin/activate

Firstly, run changer.py

    python changer.py

This application continiously make changes in access_point.json file. You can manage speed of changes by changing time.sleep() method.

Then, you need to run changes_handler_app.py first: 

    python changes_handler_app.py

and run monitor_app.py:

    python monitor_app.py

You are ready. Now you can see output of changed parameters in access_point.json file.
