import random

answer = random.randint(1, 10)

guess = int (input("1～10の数字を入力: "))

if guess == answer:
  print("正解")
else:
  print("不正解。答えは", answer)
