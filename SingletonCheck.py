import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
            if cls._instance is None:
                with cls._lock:
                    if cls._instance is None:
                        cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance

    @staticmethod
    def add (a, b):
        return a + b

s1 = Singleton()
s2 = Singleton()
p = s1.add (4,3)

print (s1 is s2)  
print (p)