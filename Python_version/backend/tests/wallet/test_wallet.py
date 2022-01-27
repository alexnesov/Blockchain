from backend.config import STARTING_BALANCE
from backend.wallet.wallet import Wallet
from backend.blockchain.blockchain import Blockchain



def test_verify_valid_signature():
    data        = {'foo': 'test_data'}
    wallet      = Wallet()
    signature   = wallet.sign(data)

    assert Wallet.verify(wallet.public_key, data, signature)


def test_verify_invalid_signature():
    data = {'foo':'test_data'}
    wallet = Wallet()
    signature = wallet.sign(data)

    assert not Wallet.verify(Wallet().public_key, data, signature)

def test_calculate_balance():
    blockchain  = Blockchain()
    wallet      = Wallet()

    assert Wallet.calculate_balance(blockchain, wallet.address) == STARTING_BALANCE