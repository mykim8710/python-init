# 변수 - 문자열

str_var = 'This is my python code.'
str_multi_line_var = """I'm backend developer.
I use python.
Thank you"""

print(str_var)
print(str_multi_line_var)


# 문자열 더하기(곱하기)
inum1 = 12
inum2 = 34

print(inum1 + inum2)    # 46

snum1 = "12"
snum2 = "34"

print(snum1 + snum2)    # 1234
print(snum1 * 3)        # 121212


# indexing
print(str_var[11])  # p
print(str_var[-1])  # .
print(str_var[-5])  # c


# slicing
print(str_var[11:17])   # python
print(str_var[11:-6])   # python
print(str_var[:10])     # This is my


# isalpha
print(str_var.isalpha())        # False >> space, .(특수문자)은 alphabat이 아니다
print(str_var.replace(" ", "").replace(".", "").isalpha()) # True


# isdecimal
print(snum1.isdecimal())  # True


# upper(), swapcase()
print(str_var.upper())     # THIS IS MY PYTHON CODE.
print(str_var.swapcase())  # tHIS IS MY PYTHON CODE.


# Format String
weather = "맑음"
temp = 25.7

# 1) % code(%s, %f, %d)
result = "[%s / %f도] 오늘 날씨는 %s 이며 기온은 %f 입니다." %(weather, temp, weather, temp)
print(result)

# 2) .format()
result2 = "[{0} / {1}도] 오늘 날씨는 {0} 이며 기온은 {1} 입니다.".format(weather, temp)
print(result2)

# 3) f""
result3 = f"[{weather} / {temp}도] 오늘 날씨는 {weather} 이며 기온은 {temp} 입니다."
print(result3)


# 문자열 입력받기
input_num = input("숫자를 입력해주세요. >> ")   # 숫자 타입이 아니라 문자열 타입이다.
print("입력받은 숫자는 {0} 입니다.".format(input_num))

input_num_plus_1 = int(input_num) + 1
print("input_num + 1 = {0}".format(input_num_plus_1))


