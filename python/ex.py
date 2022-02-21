# 01
# jumsu = [80, 75, 55]
# total = 0
# for i in jumsu:
#     total = total + i      /// 같은 뜻으로  total += i
#     count = count + i
# avg = total / 3         /// 같은 뜻으로 avg = total / len(jumsu)
# print(f"평균은 {avg}점 입니다.")


# total = 80 +75 +55
# print(total/3)

# 02
# su = int(input("숫자를 입력하세요:"))  ///   input 명령어는  문자열로 받아서  꼭 숫자로 할려면 int(정수)를 적어줄 것
# if su % 2 == 0

# f 13 % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
    
# 03
#         01234567890123 
# pin  = "881120-1068234"
# ymd = pin[:6]
# num = pin[7:]
# print(ymd)
# print(num)

# 04
# pin = "881120-1068234"
# if pin[7] == "1":           /// 문자라서 1 이 아닌 "1" 로 적어야됨
#     print("남자")
# else:
#     print("여자")
       
# print(pin[7])

# Q05
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b)

# Q06
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)

# Q07
# a = ['Life', 'is', 'too','short']
# result = " ".join(a)        // join 함수 사용
# print(result)

# Q08
# a = (1, 2, 3)
# a = a + (4,)                //   튜플로 만들기 위해서 (4,) 라고 적음. 값이 한개 일때는 (,) 적어줌
# pirnt(a)

# Q09
# 딕셔너리는 키랑 밸류로 구성
# 키는 변하지 않는 값. 
# 1번은 문자열은 가능
# 2번은 튜플은 수정,삭제가 안되니 사용가능
# 3번은 리스트라서 사용 못함
# 4번은 상수,숫자라서 가능

# Q10
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')         /// pop 은 하나 뽑아내는 것
# print(a)
# print(result)

# Q11
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)                   /// 집합과 딕셔너리는 {   }  중괄호 사용 , 집합은 값이 중복 안됨.
# b = list(aSet)              /// 집합을 리스트로 만들어서 b 에 넣음
# print(b)

# Q12
# a = b = [1, 2, 3]           /// 주기억장치에 주소가 동일하게 나옴

# print(id(a))
# print(id(b))


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)