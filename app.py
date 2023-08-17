from flask import Flask, escape

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'


@app.route('/blog_post/<int:post_id>')
def blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'


@app.route('/about', methods=['GET'])
def about():
    return '<h2>About this application ... </h2>'


@app.route('/stocks/', methods=['GET', 'POST'])
def stocks():
    return '<h2>Stock List ... </h2>'


if __name__ == '__main__':
    app.run()
