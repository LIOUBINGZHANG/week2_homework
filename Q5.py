n = int(input("輸入4個數字:"))

number = [(int(i)+7)%10 for i in str(n)]

print(f"{number[2]}{number[3]}{number[0]}{number[1]}")
