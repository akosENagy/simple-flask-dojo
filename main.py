from flask import Flask, render_template, request, redirect, url_for
import csv
import os.path
app = Flask(__name__, static_url_path='/static')

counts = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}


@app.route('/')
def route():
    return render_template('root.html')


@app.route('/request_counter', methods=['PUT', 'GET', 'DELETE', 'POST'])
def req_counter():
    counts[request.method] += 1
    return redirect(url_for('route'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
