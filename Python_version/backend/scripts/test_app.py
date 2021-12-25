import requests

BASE_URL = 'http://localhost:5000'


def get_blockchain():
    return requests.get(f'{BASE_URL}/blockchain').json()


def get_blockchain_mine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()


def post_wallet_transaction(recipient, amount):
    return requests.post(f'{BASE_URL}/wallet')


start_blockchain = get_blockchain()

print(f'start_blockchain: {start_blockchain}')






