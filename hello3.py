from flask import Flask

app=Flask(__name__)

@app.route('/flask')
def hello_flask():
    return f'Hello Flask'

@app.route('/python/')
def hello_python():
    return f'hello python'

if __name__=="__main__":
    app.run(debug=True)