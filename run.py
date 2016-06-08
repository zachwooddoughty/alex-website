import os
from flask import Flask, request, redirect, url_for, send_from_directory

# Setup Flask app.
app = Flask(__name__)
app.debug = True


# Routes
@app.route('/css/<path:path>')
def static_files():
  return app.send_static_file('/static/' + path)


@app.route('/')
@app.route('/<path>')
def pages(path="bio"):
    return app.send_static_file(path + ".html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

