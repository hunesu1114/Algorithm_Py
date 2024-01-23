def solutions():
    return 0

"""
문제 1 : 숫자의 합 구하기
N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.

==========Params==========
num1 : 숫자의 개수
num2 : 공백 없이 주어진 num1개의 숫자
==========================
"""
def solution1():
    a=int(input("num1 : "))
    b=int(input("num2 : "))
    answer=0
    for i in range(0,a):
        answer+=b%10
        b=(b-b%10)/10
    print(int(answer))

"""
문제 2 : 평균 구하기
세준이는 기말고사를 망쳤다. 그래서 점수를 조작해 집에 가져가기로 결심했다. 일단 세준이는 자기 점수 중 최댓값을 골랐다. 그런 다음 최댓값을
M이라 할 때 모든 점수를 (점수)/M*100 으로 고쳤다. 예를 들어 세준이의 최고점이 70점, 수학 점수가 50점이라면 수학 점수는 50/70*100 이므로
71.43점이다. 세준이의 성적을 이 방법으로 계산했을 때 새로운 평균을 구하는 프로그램을 작성하시오.

==========Params==========
numbers : 각 과목의 시험 성적 list
==========================
"""
def solution2():
    values=list(map(int,input("점수들을 입력 : ").split()))
    maxValue=max(values)
    temp=sum(values)
    print(temp/maxValue*100/len(values))

"""
문제 3 : 구간 합 구하기 1
수 N 개가 주어졌을 때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램을 작성하시오.

==========Params==========
numbers : N 개의 수 list
i : 구간 합의 시작
j : 구간 합의 마지막
==========================

==========Example==========
numbers = [1,2,3,4,5]
i = 1
j = 3
인 경우 6을 return
===========================

"""
def solution3(numbers, i, j):
    answer = 0

    return answer