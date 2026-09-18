
class Singleton:
    """
    Singleton Design Pattern in Python

    A Singleton ensures that only one instance of a class is created and provides a global access point to that instance. 
    This is commonly used for loggers, configuration managers, database connections, and caches.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def show_message(self):
        print("Hello from Singleton")


# Usage
s1 = Singleton()
s2 = Singleton()

s1.show_message()

print(s1 is s2)   # True
