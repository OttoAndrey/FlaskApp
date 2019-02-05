from flask import Flask


app = Flask(__name__) #экземпляр класса flask


@app.route('/')
def index():
    return '<h1>kek</h1>'

if __name__ == '__main__':
    app.run()