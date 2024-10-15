def josephus(n, k):
    # 迭代法解約瑟夫問題，n是總人數，k是報數時要退出的人數
    last_position = 0  # 當只有一個人時，位置是 0 (這裡用 0-based 編號)
    for i in range(2, n + 1):
        last_position = (last_position + k) % i
    return last_position + 1  # 轉換成 1-based 編號

# 測試：QA 部門有 n 個人，報數到 3 的人退出
n = int(input("請輸入參與團康活動的人數: "))
k = 3  # 報數到 3 的人退出

# 計算最後留下的同事的順位
last_person = josephus(n, k)
print(f"最後留下的是第 {last_person} 位同事")
