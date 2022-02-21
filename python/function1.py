# def add(a, b):
#     return a + b

# print(add(5,3))

# ===================================================================

# 2교시     매개변수와 인수

# def add(a, b):
#     return a + b

# a = 3
# b = 4
# c = add(a, b)
# print(c)

# def say():
#     return 'Hi'

# a = say()
# print(a)


# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a,b,a+b))

# add(5,3)

# def say():
#     print('Hi')

# say()

# def add(a, b):
#     result = a + b
#     return result

# result = add(a=5,b=3)
# print(result)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# result = 0
# args = [1,2,3,4,5]
# for i in args:
#     result = result + i
# print(result)    
    
    

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# result = add_many(1,2,3)      /// 튜플로 만들어 주기 때문에 수정 안됨
# print(result)
    
    

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3,4,5,6,7,8,9,10)     
print(result)





















#====================================================================================================

#           5교시                  

# def add_and_mul(a,b):
#     return  a+b, a*b

# result = add_and_mul(3,4)
# print(result)
# print(type(result))


def add_and_mul(a,b):
    return  a+b, a*b

result1, result2 = add_and_mul(3,4)
print(result1)
print(type(result1))
