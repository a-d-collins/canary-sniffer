import flask
from flask import request, jsonify

from canary_sniffer import helpers

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/api/v1/property/has-septic', methods=['GET'])
def property_has_septic():
    if 'address' in request.args and 'zipcode' in request.args:
        address = request.args['address']
        zipcode = request.args['zipcode']
    else:
        return jsonify(
            error="Address and zipcode must both be provided. Please include 'address' and 'zipcode' params.")

    return jsonify(helpers.property_has_septic(address, zipcode))


app.run()
