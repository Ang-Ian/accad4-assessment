from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask via CodeDeploy! NEW CHANGE!!!!! 暹罗猫 kedi. This is not what I wanted..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
