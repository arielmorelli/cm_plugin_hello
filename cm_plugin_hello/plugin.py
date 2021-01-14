class Plugin(object):
    def __init__(self):
        pass

    def activate(self, app):
        @app.route("/hello_world")
        def hello():
            return "Hello world from a simple plugin"

    def run_scripts(self):
        print("hello world")

