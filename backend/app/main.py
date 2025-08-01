from flask import Flask
from flask_cors import CORS
# from .routes import bp
from routes import bp

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins
app.register_blueprint(bp, url_prefix="/api")

# if __name__ == "__main__":
#     app.run(host="localhost", port=5000, debug=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))   # Use PORT from environment, default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
