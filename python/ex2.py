# Q1
# from pickle import SHORT_BINSTRING


# a = "Life is too short, you need python"

# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

# 답은 shirt 

# 첫 번째 조건: "wife"라는 단어는 a 문자열에 없으므로 거짓이다.
# 두 번째 조건: "python"이라는 단어는 a 문자열에 있지만 "you" 역시 a 문자열에 있으므로 거짓이다.
# 세 번째 조건: "shirt"라는 단어가 a 문자열에 없으므로 참이다.
# 네 번째 조건: "need"라는 단어가 a 문자열에 있으므로 참이다.
# 가장 먼저 참이 되는 것이 세 번째 조건이므로 "shirt"가 출력된다


# Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1
#     print(result)        
     
# Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자. 
# result = 0
# i = 1
# while i <= 5:
#     if i 



# Q4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# i = 
# for i < 100: 
#     i = i + 1

# print(i)




# Q5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

number = 0
avg = (number/10)
for mark in marks:
    number = number +1
    print(number)
    





# Q6
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
