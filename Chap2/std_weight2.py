height = float(input("身長を入力してください：　"))
bmi = 22
std_weight1 = bmi * (height / 100) ** 2
print("身長：　" + str(height) + "cm →", end = "")
print("標準体重：　" + str(std_weight1) + "kg")

std_weight1 = bmi * (((height ** 2) / (100 ** 2)))
print("身長：　" + str(height) + "cm →", end = "")
print("標準体重：　" + str(std_weight1) + "kg")
