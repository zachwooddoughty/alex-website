import os
from flask import Flask, request, redirect, url_for, send_from_directory

# Setup Flask app.
app = Flask(__name__)
app.debug = True
root = os.getcwd()
app.static_folder = root
app.template_folder = root
app.static_url_path = root


# Routes
@app.route('/')
@app.route('/bio')
def bio():
  return app.send_static_file('bio.html')

@app.route('/research')
def research():
  return app.send_static_file('research.html')

@app.route('/teaching')
def teaching():
  return app.send_static_file('teaching.html')

@app.route('/<image>.png')
def static_proxy(image):
  return app.send_static_file(image + '.png')

@app.route('/<path:path>')
def err404(path):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


