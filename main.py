from flask import Flask, render_template, request, redirect, url_for
import csv
import os.path
import pickle
app = Flask(__name__, static_url_path='/static')


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


@app.route('/')
def route():
    return render_template('root.html')


@app.route('/request_counter', methods=['PUT', 'GET', 'DELETE', 'POST'])
def req_counter():
    counts = load_obj('counts')
    counts[request.method] += 1
    save_obj(counts, 'counts')
    return redirect(url_for('route'))


@app.route('/statistics')
def statistics():
    counts = load_obj('counts')
    return render_template('statistics.html', counts=counts)


def main():
    counts = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}
    if os.path.isfile('counts.pkl'):
        counts = load_obj('counts')
    else:
        save_obj(counts, 'counts')
    app.run(debug=True)


if __name__ == '__main__':
    main()
