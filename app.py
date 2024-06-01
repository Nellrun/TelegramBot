from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Welcome to the Web App</h1>
    <p>This is a simple web application.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
