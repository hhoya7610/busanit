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

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1              /// i = i +1

print(result)        
     
# Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자. 
i = 0
while True:
    i += 1
    i > 5: break
    print('*' * i)



# Q4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# i = 
# for i < 100: 
#     i = i + 1

# print(i)
for i in range(1, 101):
    ...    print(i)
print()    



# Q5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

# 총점
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score   # A학급의 점수를 모두 더한다.

average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print(average) # 평균 79.0이 출력된다.
for문을 사용하여 먼저 총 점수를 구한 후 총 점수를 총 학생 수로 나누어 평균 점수를 구한다.





# Q6
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

리스트 내포로 표현하면 다음과 같다.

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)
[2, 6, 10]
        
        

        
