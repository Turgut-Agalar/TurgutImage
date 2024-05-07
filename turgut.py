import inspect

def HelloWorld(f):
  getattr(__builtins__, f)(inspect.stack()[0][3])

HelloWorld(print)
