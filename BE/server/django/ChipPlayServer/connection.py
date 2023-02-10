class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls._instance[cls]
    
class SocketConnection(metaclass=Singleton):
    def __init__(self) -> None:
        self.no = 0

    def get(self):
        self.no += 1
        return self.no
