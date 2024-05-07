import inspect

def Bebekfurkan(f):
  getattr(__builtins__, f)(inspect.stack()[0][3])


Bebekfurkan("print")
