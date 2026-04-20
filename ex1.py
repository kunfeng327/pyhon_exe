import random

def catch_fox():
    # 1. 初始化游戏
    holes = [1, 2, 3, 4, 5]  # 5个洞口
    fox_pos = random.choice(holes)  # 狐狸初始位置
    max_attempts = 7  # 最多抓7次，可修改
    attempts = 0

    print("=== 抓狐狸游戏 ===")
    print(f"一共有5个洞口（1-5），你最多有 {max_attempts} 次机会！")
    print("没抓到的话，狐狸会跳到隔壁洞口哦！\n")

    # 2. 游戏循环
    while attempts < max_attempts:
        attempts += 1
        print(f"第 {attempts} 次抓狐狸！")

        # 输入玩家选择，带异常捕获
        while True:
            try:
                player = int(input("请打开洞口（输入1-5）："))
                if player in holes:
                    break
                else:
                    print("只能输入1-5的数字！")
            except ValueError:
                print("输入错误！请输入数字！")

        # 3. 判断是否抓到
        if player == fox_pos:
            print(f"\n🎉 恭喜！你在第 {attempts} 次抓到了狐狸！它在洞口 {fox_pos}！")
            return

        # 没抓到，狐狸移动
        print(f"😮 没抓到！狐狸不在洞口 {player}")
        if fox_pos == 1:
            fox_pos = 2
        elif fox_pos == 5:
            fox_pos = 4
        else:
            # 中间洞口随机往左或往右跳
            fox_pos += random.choice([-1, 1])

    # 4. 次数用完
    print(f"\n❌ 游戏结束！{max_attempts} 次都没抓到狐狸，你失败了！")

# 启动游戏
catch_fox()