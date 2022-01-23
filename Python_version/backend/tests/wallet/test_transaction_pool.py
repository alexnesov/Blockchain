from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet
from backend.blockchain.blockchain import Blockchain


def test_set_transaction():
    transaction_pool = TransactionPool()
    transaction      = Transaction(Wallet(), 'recipient', 1)

    transaction_pool.set_transaction(transaction)

    assert transaction_pool.transaction_map[transaction.id] == transaction


    
def test_clear_blockchain_transactions():
    transaction_pool    = TransactionPool()
    tranasction_1       = Transaction(Wallet(), 'recipient', 1)
    tranasction_2       = Transaction(Wallet(), 'recipient', 2)

    transaction_pool.set_transaction(tranasction_1)
    transaction_pool.set_transaction(tranasction_2)

    blockchain = Blockchain()
    blockchain.add_block([tranasction_1.to_json(), tranasction_2.to_json()])

    assert tranasction_1.id in transaction_pool.transaction_map
    assert tranasction_2.id in transaction_pool.transaction_map

    transaction_pool.clear_blockchain_transactions(blockchain)

    assert not tranasction_1.id in transaction_pool.transaction_map
    assert not tranasction_2.id in transaction_pool.transaction_map
