import random

count = 0
history = []

while True:
    cmd = input("Enterで抽選(終了はq) :")
    if cmd == "q":
        print("終了します")
        break

    # 通常抽選
    num = random.randint(1, 399)
    count += 1

    if num == 1:
        print("当選！！！")
        history.append("当たり")

        # ボーナス抽選（50%）
        bonus = random.choice([True, False])
        if bonus:
            print("ボーナス当選！🎉")
            history.append("ボーナス当たり")

            # 継続抽選（75%）
            while random.random() < 0.75:  # 0.75未満なら継続
                count += 1
                print("継続抽選！")
                cont_num = random.randint(1, 399)
                if cont_num == 1:
                    print("継続当選！！！")
                    history.append("継続当たり")
                else:
                    print("継続ハズレ")
                    history.append("継続ハズレ")
        else:
            print("ボーナスハズレ")
            history.append("ボーナスハズレ")

        break  # 最初の当たり後は一度ループ終了
    else:
        print("ハズレ")
        history.append("ハズレ")

print("---結果---")
print("総回転:", count)
print("履歴:", history)
