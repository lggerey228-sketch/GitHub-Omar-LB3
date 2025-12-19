from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Hello, World!"

if name == 'main':
    app.run(debug=True)
