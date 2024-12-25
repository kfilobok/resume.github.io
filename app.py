from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    language = session.get('language', 'ru')
    theme = session.get('theme', 'light')
    return render_template('index.html', language=language, theme=theme)

@app.route('/set_language', methods=['POST'])
def set_language():
    session['language'] = request.json.get('language', 'ru')
    return '', 204

@app.route('/set_theme', methods=['POST'])
def set_theme():
    session['theme'] = request.json.get('theme', 'light')
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
