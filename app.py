from flask import Flask, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return redirect('/api/hello')  # 重定向到 hello 接口

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return {"message": "Hello, World!"}

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0') 