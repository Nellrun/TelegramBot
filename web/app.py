from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')


@app.route('/username/save', methods=['POST'])
def save_username():
    username = request.form.get('username')
    # Здесь вы можете сохранить имя пользователя или выполнить другие действия
    return jsonify({"message": "Username saved successfully!", "username": username})


if __name__ == '__main__':
    app.run(debug=True)
