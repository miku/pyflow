from multiprocessing import Pipe
a, b = Pipe()
a.send([1, 'hello', None])
b.recv()

b.send_bytes(b'thank you')
a.recv_bytes()

import array
arr1 = array.array('i', range(5))
arr2 = array.array('i', [0] * 10)
a.send_bytes(arr1)
count = b.recv_bytes_into(arr2)
assert count == len(arr1) * arr1.itemsize
arr2