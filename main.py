from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello World'

@app.route('/about')
def about():
    return 'It\'s about Time'

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
