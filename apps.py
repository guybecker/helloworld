from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')
#
# This is needed for Azure to properly start the application
if __name__ == '__main__':
    # Azure App Service expects your app to listen on port 8000
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
