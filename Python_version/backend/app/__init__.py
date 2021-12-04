from flask import Flask, jsonify
import os
import random

from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub


app         = Flask(__name__)
blockchain  = Blockchain()
pubsub      = PubSub() 




@app.route('/')
def route_default():
    return 'Welcome to the blockchain'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())


PORT = 5000

# After doing a "export PEER=True && python3 -m backend.app"
# there won't be a "OSError: [Errno 98] Address already in use" (port)
if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)



app.run(port = PORT)