from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Flask Cookie Example</h1>
        <a href="/set_cookie">Set Cookie</a><br>
        <a href="/get_cookie">Get Cookie</a><br>
        <a href="/delete_cookie">Delete Cookie</a>
    '''

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie has been set!")
    resp.set_cookie('username', 'JohnDoe', max_age=60*60*24*30)  # Cookie expires in 30 days
    return resp

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    if username:
        return f'Username: {username}'
    else:
        return 'No cookie found'

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response("Cookie has been deleted!")
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
