class Plugin(object):
    """ Hello world plugin.

    This class represent a really simple plugin.
    It can be used as base to other plugins

    Attributes:
        FREQUENCY (int, optional): integer represing minimum hours to execute.
        SCRIPTS (list): List of scripts to run in the backend of CM.
        FIELDS (list): List of fields to add in the admin interface of CM.
    """

    FREQUENCY = 1 # run every hour
    SCRIPTS = []
    FIELDS = [{
        "key": "example-field",
        "label": "just a example",
        "description": "Example of required field",
        "type": "input",
        "required": True,
        "default": "hello",
    },
    {
        "key": "example-field-2",
        "label": "just a example 2",
        "description": "Example of optional field",
        "type": "input",
        "required": False,
        "default": "hello-optional",
    }]

    def __init__(self):
        pass

    def activate(self, app):
        @app.route("/hello_world")
        def hello():
            return "Hello world from a simple plugin"

    def run_scripts(self, plugin_name):
        print("hello world")

