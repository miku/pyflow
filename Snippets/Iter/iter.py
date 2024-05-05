from functools import partial


with open('data.file', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        # process_block(block)
        print(block)
