from flask import Flask
app=Flask(__name__)

@app.route("/hello")
def hello_world():
    return "HELLO WORLD!"
app.add_url_rule('/','hello',hello_world)

if __name__=="__main__":
    app.run(debug=True)