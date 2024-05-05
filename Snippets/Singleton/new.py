# Straightforward implementation of the Singleton Pattern

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    
logger = Logger()
log2 = Logger()
