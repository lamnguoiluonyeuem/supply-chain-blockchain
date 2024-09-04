from blockchain import Blockchain, generate_keys
import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

blockchain = Blockchain()

private_key, public_key = generate_keys()

def sign_transaction(private_key, recipient, product, quantity):
    private_key = serialization.load_pem_private_key(private_key, password=None)
    message = f"{recipient}{product}{quantity}".encode()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

signature = sign_transaction(private_key, "Nhà sản xuất", "Nguyên liệu A", 100)
blockchain.new_transaction(sender=public_key.decode(), recipient="Nhà sản xuất", product="Nguyên liệu A", quantity=100, signature=signature)

signature = sign_transaction(private_key, "Nhà phân phối", "Sản phẩm B", 50)
blockchain.new_transaction(sender=public_key.decode(), recipient="Nhà phân phối", product="Sản phẩm B", quantity=50, signature=signature)

last_proof = blockchain.last_block['proof']
proof = blockchain.proof_of_work(last_proof)
block = blockchain.new_block(proof)

for block in blockchain.chain:
    print(json.dumps(block, indent=4))

def check_product_history(blockchain, product_name):
    history = []
    for block in blockchain.chain:
        for transaction in block['transactions']:
            if transaction['product'] == product_name:
                history.append(transaction)
    return history

product_history = check_product_history(blockchain, "Sản phẩm B")
print("\nLịch sử của Sản phẩm B:")
print(json.dumps(product_history, indent=4))
