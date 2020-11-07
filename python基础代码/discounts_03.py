def discounts(price, rate):
  final_price = price * rate
  print('这里试图打印全局变量old_price的值: ', old_price)
  return final_price
    
old_price = float(input('请输入原价: '))
rate = float(input('请输入折扣率: '))
new_price = discounts(old_price, rate)
print('打折后价格是: ', new_price)
