# 변수 - 숫자 및 Boolean Type 

# 변수의 선언

integer_var = 40
print(integer_var)      # 40
print(integer_var + 20) # 60
print(integer_var - 10) # 30
print(integer_var * 5)  # 200
print(integer_var / 8)  # 5.0
print(integer_var // 6) # 6(몫)
print(integer_var % 6)  # 4(나머지)
print(integer_var ** 2) # 1600


integer_var2 = 42
print(integer_var < integer_var2)   # True
print(integer_var == integer_var2)  # False
print(integer_var != integer_var2)  # True


float_var = 3.14
print(float_var)       #3.14
print(float_var * 2)   #6.28
print(float_var / 2)   #1.57


is_true = True
is_false = False

print(is_true and is_true)     # True
print(is_true and is_false)    # False  
print(is_false and is_false)   # False
print(is_true or is_true)      # True
print(is_true or is_false)     # True  
print(is_false or is_false)    # False