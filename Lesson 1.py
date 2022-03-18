from flask import Flask

app = Flask(__name__)


@app.route("/hello/test/")
def hello_world():
    return "<p>Hello from Flask application</p>"


app.run(debug=True)

# http://localhost/folder1/folder2?file=some_file.txt


