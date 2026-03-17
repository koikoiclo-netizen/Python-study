import random

count = 0
history = []

while True:
  cmd = input("Enterで抽選(終了はq) :")

  if cmd == "q":
    print("終了します")
    break
  
  num = random.randint(1, 399)
  count += 1

  if num == 1:
    print("当選！！！")
    history.append("当たり")
    break
  else:
    print("ハズレ")
    history.append("ハズレ")

print("---結果---")
print("総回転:", count)
print("履歴:", history)
