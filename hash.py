import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


def hash(block):
    """
    Creates a SHA-256 hash of a Block

    :param block: Block
    """

    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
print(hashlib.sha256(b'{"index": 2, "previous_hash": "43792c8edc71b2e104bdef9e292ed1ec088a130a0a0a30dd6728eaf68756a0ff", "proof": 105045, "timestamp": 1584431407.95485, "transactions": [{"amount": 1151, "recipient": "d732ffef5c894bf4854047fb6c436d8d1", "sender": "some-other-addressasdfasdfasdf1"}, {"amount": 11, "recipient": "d732ffef5c894bf4854047fb6c436d8d1", "sender": "some-other-addressasdfasdfdf1"}, {"amount": 1, "recipient": "9b3d2fb108834247bead01ebcf3f3332", "sender": "0"}]}').hexdigest())
#print(hash({"index": 2, "previous_hash": "3dacf987b7d80eee5cd542079e6237e0cbf3b63e2bcb8e37b4d1ae49c60c1842", "proof": 124388, "timestamp": 1583915430.0173683, "transactions": [{"amount":1,"recipient":"150fb1e217a8429b8072dd5662edaa72","sender":"0"}]}))