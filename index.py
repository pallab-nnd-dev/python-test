from flask import Flask

app = Flask(__name__)  # Initialize the Flask application

@app.route("/")  # Define the route for the root URL
def home():
    return "Hello, Flask!"  # The response that will be displayed in the browser

@app.route("/file")
def execute_dynamic_file():
    with open("forloop.py", "r") as file:
        exec(file.read())  # Execute the code in the file
    return "Dynamic execution completed!"

@app.route("/pallab")
def execute_dynamic_file1():
    with open("forloop.py", "r") as file:
        exec(file.read())  # Execute the code in the file
    return "Dynamic execution completed pallab!"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=100, debug=True)
