from hashlib import sha256
MAX_NONCE = 1000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Nice! Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} iterations")

if __name__ == '__main__':
    transactions = '''
    Dario->Gino->20
    Adrian->Dario->5
    '''
    difficulty = 6
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, '0000000xf9cd5049c4af2b462735457e4d3baf130bcbb87f389e349fbaeb20b9', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)