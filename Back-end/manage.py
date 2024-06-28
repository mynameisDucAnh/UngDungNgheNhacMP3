from app import create_app
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
