from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
    hostname = request.host_url
    message = 'Thanks for being you!'
    return render_template('main.html', host=hostname, msg=message)

@app.route('/about', methods=['GET'])
def mission():
    return render_template('about.html')
