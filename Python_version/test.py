from block import Block

newBlock = Block(1, '2020', '0001', 'foo')


print(type(newBlock))
print(newBlock)

print('-------------------')

def genesis():
    """
    Generate the genesis block.
    """
    return Block(1, 'genesis_last_hash', 'gensis_hash', [])





aList = [genesis()]

print(type(aList))
print(aList)