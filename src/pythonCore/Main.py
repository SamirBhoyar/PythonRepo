from asyncio import __main__

from src.pythonCore.Generator import gencube

if __name__== __main__:
     for i in gencube(5):
      print(i)