import random # 导入随机模块,用于电脑出拳
def play_rps():
    """石头剪刀布核心游戏逻辑"""
    choices=["石头","剪刀","布"]
    #1.电脑出拳
    computer_choice= random.choice(choices)

    #2.用户出拳 & 输入验证
    while True:
        user_choice=input("请出拳(石头/剪刀/布):").strip()
        if user_choice in choices:
             break #输入合法,退出循环
        print("输入无效!只能选:石头、剪刀、布")

    #3.展示结果
    print(f"\n💻电脑出拳:{computer_choice}")
    print(f"👤你出拳:{user_choice}")

    #4.胜负判定逻辑
    if user_choice==computer_choice:
       print("🤝平局！再来一局~")
    elif(user_choice=="石头"and computer_choice=="剪刀")or\
        (user_choice=="剪刀"and computer_choice=="布")or\
        (user_choice=="布"and computer_choice=="石头"):
        print("🎉你赢啦！真厉害~")
    else:
        print("😢你输啦！电脑太强啦~")
#调用函数才能运行游戏
play_rps()