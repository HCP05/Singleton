#example
class Singleton:
   __instance = None

   @staticmethod
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self


#Se pot instantia 2
a=Singleton()
print(a._Singleton__instance)
# Singleton._Singleton__instance=None
a1=Singleton.getInstance()
print(a1._Singleton__instance)
Singleton._Singleton__instance=None
b=Singleton()

print(b._Singleton__instance,"daw")




class SingletonMeta(type):
   """
   The Singleton class can be implemented in different ways in Python. Some
   possible methods include: base class, decorator, metaclass. We will use the
   metaclass because it is best suited for this purpose.
   """


   _instances = {}

   def __call__(cls,*args,**kwargs):
      """
      Possible changes to the value of the `__init__` argument do not affect
      the returned instance.
      """
      if cls not in cls._instances:
         instance = super().__call__(*args,**kwargs)
         cls._instances[cls] = instance
         print(instance)
      return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
   def some_business_logic(self):
      """
             Finally, any singleton should define some business logic, which can be
             executed on its instance.
             """
      # ...

class Service(Singleton):
   def __init__(self):
      print("Is in service")
      name="test"


if __name__ == "__main__":
   # The client code.

   s1 = Singleton()
   SingletonMeta._instances.pop(s1.__class__)
   s2 = Singleton()

   serv1=Service()
   serv2=Service()



   if id(s1) == id(s2):
      print("Singleton works, both variables contain the same instance.")
   else:
      print("Singleton failed, variables contain different instances.")

   if id(serv1) == id(serv2):
      print("Singleton works, both variables contain the same instance.")
   else:
      print("Singleton failed, variables contain different instances.")
