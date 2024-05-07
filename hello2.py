from flask import Flask

app=Flask(__name__)

@app.route('/blog/<int:postID>')
def blog(postID):
    return f'blog ID is {postID}'

@app.route('/rev/<float:revno>')
def rev(revno):
    return f'revision number is {revno}'

if __name__=="__main__":
    app.run(debug=True)