#from SingletonCheck import _new_
from SingletonCheck import Singleton

#def test_new():
 #assert _new_() is not None, "The _new_ function should return a non-None value"

def test_singleton_instance():
    
    s1 = Singleton()
    s2 = Singleton()
    assert s1 is s2, "Singleton instances should be the same"