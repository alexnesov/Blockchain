import hashlib

def crypto_hash(data):
    """
    Return a sha-256 hash of the given data.
    """
    return hashlib.sha256(data)


def main():
    print(f"crypto_hash('foo'): {crypto_hash('foo')}")

