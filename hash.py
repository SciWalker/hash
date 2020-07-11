
import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
import flask
import requests
from flask import Flask, jsonify, request,Response


def hash(block):
    """
    Creates a SHA-256 hash of a Block

    :param block: Block
    """

    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
#print(hashlib.sha256(b'{"index": 2, "previous_hash": "43792c8edc71b2e104bdef9e292ed1ec088a130a0a0a30dd6728eaf68756a0ff", "proof": 105045, "timestamp": 1584431407.95485, "transactions": [{"amount": 1151, "recipient": "d732ffef5c894bf4854047fb6c436d8d1", "sender": "some-other-addressasdfasdfasdf1"}, {"amount": 11, "recipient": "d732ffef5c894bf4854047fb6c436d8d1", "sender": "some-other-addressasdfasdfdf1"}, {"amount": 1, "recipient": "9b3d2fb108834247bead01ebcf3f3332", "sender": "0"}]}').hexdigest())
#print(hash({"index": 2, "previous_hash": "3dacf987b7d80eee5cd542079e6237e0cbf3b63e2bcb8e37b4d1ae49c60c1842", "proof": 124388, "timestamp": 1583915430.0173683, "transactions": [{"amount":1,"recipient":"150fb1e217a8429b8072dd5662edaa72","sender":"0"}]}))


###################################################Start API######################################################
app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/')
def home():
#    return '''<h1>QR codes</h1>
#<p>A prototype API for a great project</p>'''
    return "testing"
# A route to return all of the available entries in our catalog.
    
@app.route('/api/hash', methods=['POST'])
def result():
    json_api=request.get_json()
    api_message = json_api['content']
    hashed_message=hash(api_message)
    print(hashed_message)
    #post the result image through api
    payload = {'response': hashed_message}

    return Response(json.dumps(payload), status=200, mimetype='application/json')





@app.route('/api/result', methods=['GET'])
def result_get():
    
    return result



#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000,debug=True)
