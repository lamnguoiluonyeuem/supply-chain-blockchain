from flask import Flask, jsonify, request
from blockchain import Blockchain, generate_keys, sign_transaction

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'product', 'quantity', 'signature', 'status']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(
        sender=values['sender'],
        recipient=values['recipient'],
        product=values['product'],
        quantity=values['quantity'],
        signature=values['signature'],
        status=values['status']
    )

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    block = blockchain.new_block(proof)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)