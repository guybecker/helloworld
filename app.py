from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# This is needed for Azure to find the app
if __name__ == '__main__':
    # Use the PORT environment variable provided by Azure if available
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
else:
    # For Gunicorn to find the app
    application = app
