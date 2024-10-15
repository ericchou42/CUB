from collections import Counter
import string

def count_letters(text):
    # 將字母轉為小寫，並移除非字母的字符
    text = text.lower()
    # 過濾出只包含英文字母的字符
    letters_only = [char for char in text if char in string.ascii_lowercase]
    
    # 計算字母出現次數
    letter_count = Counter(letters_only)
    return letter_count

# 國泰銀行六十周年的字母
text = "Hello welcome to Cathay 60th year anniversary"

# 計算字母出現次數
letter_count = count_letters(text)

# 輸出結果
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
