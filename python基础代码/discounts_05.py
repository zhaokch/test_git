count = 5
def myFun():
  global count
  count = 10
  print('函数内部输出的count: ', count)
myFun()
print('函数外部输出的count: ', count)
