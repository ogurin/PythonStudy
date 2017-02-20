words = ["空", "秘密", "電柱", "ひらけごま", "海", "ギター"]

s = input("文字列を入力してください：　")

try:
    index = words.index(s)
    print('"{0}"のインデックスは{1}です'.format(s, index))
except ValueError:
    print('"{0}"は見つかりませんでした'.format(s))
finally:
    print(s in words)
