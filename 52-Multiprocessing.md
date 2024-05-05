# Multiprocessing

> multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.

* various start methods, but not all available on all platforms
* Pool

Communication over:

* Queue (put, get)
* Pipe (duplex connection)

Locking:

* Lock.acquire, Lock.release
* use case for try .. finally

Shared memory:

* Value, Array

Alternatively, more complete data structures through a manager:

> Managers provide a way to create data which can be shared between different processes, including sharing over a network between processes running on different machines. A manager object controls a server process which manages shared objects. Other processes can access the shared objects by using proxies.