# test_list = ["one", "two", "three"]
# for i in test_list:
#     print(i)

# a = [(1,2), (3,4), (5,6)]       /// [  ]는 리스트, (   )는 튜플
# for (first, last) in a:
#     print(first + last)

# a = [(1,2), (3,4), (5,6)]   
# for i in a:
#     print(i)
    
# a = [(1,2), (3,4), (5,6)]   
# for i, j in a:
#     print(i, j)
    
# a = [(1,2), (3,4), (5,6)]   
# for i, j in a:
#     print(i + j)
# ===================================================================================================================================================
#                         @ 5교시 @

# a = [(1,2), (3,4), (5,6)]   
# for i in a:
#         print(i, "-->", type(i))

# a = [(1,2), (3,4), (5,6)]   
# for first, last in a:
#     print (first + last)

# marks = [90, 25, 67, 45, 80]        /// 점수

# number = 0                  /// 누적연산, 0 이라는 값을 clear 해주는 것
# for mark in marks: 
#     number = number +1      /// number += 1, 
#     if mark >= 60: 
#         print("%d번 학생은 합격입니다." % number)
#     else: 
#         print("%d번 학생은 불합격입니다." % number)

# marks = [90, 25, 67, 45, 80]

# number = 0 
# for mark in marks: 
#     number = number +1 
#     if mark < 60:
#         continue 
#     print("%d번 학생은 합격입니다. " % number)


# a = [1,2,3,4,5,6,7,8,9,10]
# b = range(1, 11)

# for i in a:
#     print(i)

# for i in b:
#     print(i)


# a = [1,2,3,4,5,6,7,8,9,10]
# b = range(1, 11)

# for i in a:
#     print(i, end=' ')
# print()             /// 줄바꿈 용도 (\n : 개행문자는 생략,줄 바꿔서 맨 처음으로)
# for i in b:
#     print(i, end=' ')


# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60: 
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# ====================================================================================================================================================

                                        # @ 6교시 @

# for i in range(2, 10):
#     for j in range(1,10):
#         print(i*j, end=' ')
#     print()   

# for i in range(1, 10):
#     for j in range(2,10):
#         print(i,"*",j,"=",i*j, end='  ')
#     print()           


# for i in range(1, 10):
#     for j in range(2,10):
#         print(j,"*",i,"=",i*j, end='  ')
#     print()           


# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)
    
# print(result)                                                                

# a= [1,2,3,4]
# result = [num * 3 for num in a]
# print(result)

# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

