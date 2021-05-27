import hashlib
import json


def stringify(data):
    return json.dumps(data)

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given argument.
    """
    stringified_args = map(stringify, args)
    print(f'args: {args}')
    joined_data = ''.join(args)

    print(f'joined_data: {joined_data}')
    
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('one','two','three'): {crypto_hash('one','two','three')}")


if __name__ == '__main__':
    main()
