from flask import Flask,render_template

app=Flask(__name__)

@app.route('/hello/<int:score>')
def hello_score(score):
    return render_template('hello1.html',marks=score)

if __name__=="__main__":
    app.run(debug=True)