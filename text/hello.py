#! python2
# coding=utf-8

'''
注释
'''
"""
注释
"""

import sys


# input("\n\n按下 enter 键后退出。")

x='a'
a, b, c = 1, 2, "runoob"
print( c, end=" " )

#print ('\n python 路径为',sys.path)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))


def fibonacci(n): # 生成器函数 - 斐波那契
  a, b, counter = 0, 1, 0
  while True:
    if (counter > n):
      return
    yield a
    a, b = b, a + b
    counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
  try:
    print (next(f), end=" ")
  except StopIteration:
    sys.exit()