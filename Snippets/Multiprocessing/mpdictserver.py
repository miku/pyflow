import multiprocessing as mp
from multiprocessing.managers import SyncManager

manager = SyncManager(address=('', 50000), authkey=b'abc')
server = manager.get_server()
server.serve_forever()
