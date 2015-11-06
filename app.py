from flask import Flask, request

app = Flask(__name__)


@app.route("/todoist/")
def todoist_listener():
    print request
    return "Ok"


app.run("0.0.0.0", 9999)
