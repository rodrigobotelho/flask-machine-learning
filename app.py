from flask import Flask, request, jsonify
import logging
import machine

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)

ml = machine.MachineLearning()
@app.route('/<text>')
def predict(text):
    return jsonify(ml.predict(text))

if __name__ == '__main__':
    app.run(debug = True)
