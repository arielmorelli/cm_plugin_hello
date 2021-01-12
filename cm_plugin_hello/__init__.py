from plugin import run

# routes should use same syntax from flask add_url_rule
#  More information here https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.add_url_rule
routes = [
    {"rule": "/hello_world", "view_func": run},
]

run_func = [] # functions to run wasn't defined yet, but this variable is necessary
