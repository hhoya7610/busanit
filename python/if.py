# # 논리값은 True, False  /// 첫 글자는 대문자로~
# money = True
# # if (조건문>:
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# =================================  6교시  =====================================================

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라") 

# [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]  
# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     pass    
# else:
#     pass


# pocket = ['paper', 'cellphone', 'money']
# if 'card' in pocket:
#     print("카드를 꺼내라")
# else:
#     if 'money' in pocket:
#         print("돈을 꺼내라") 
#     else:
#         print("걸어가라")
        
# pocket = ['paper', 'cellphone', 'money']
# if 'card' in pocket:
#     print("카드를 꺼내라")
# elif 'money' in pocket:
#      print("돈을 꺼내라") 
# else:
#      print("걸어가라")        

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket: pass              /// if 문에서 조건이 한줄 씩 일때는 붙여쓰기 가능
# else: print("카드를 꺼내라")

# score = 70
# if score >= 60:
#     message = 'success'
# else:
#     message = 'failure'
# print(message) 
   
# #         참인 경우 if 조건문      else 거짓인 경우
# message = "success" if score >= 60 else "failure"   
# print(message) 

# pocket = ['paper', 'cellphone', 'money']
# message = "택시를 타고 가라" if "money" in pocket else "걸어가라"
# print(message)

# ===========================   7교시  ==================================================

# treeHit = 0
# while treeHit < 10:
#     # treeHit += 1
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")
        

# prompt = """
#     1. Add
#     2. Del
#     3. List
#     4. Quit

#     Enter number: """  
    
# number = 0
# while number != 4:
#     print(prompt) 
#     number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    

    