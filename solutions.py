def solutions():
    return 0

# 문제 1 : 숫자의 합 구하기
def solution1():
    a=int(input("num1 : "))
    b=int(input("num2 : "))
    answer=0
    for i in range(0,a):
        answer+=b%10
        b=(b-b%10)/10
    print(int(answer))

# 문제 2 : 평균 구하기
def solution2():
    values=list(map(int,input("점수들을 입력 : ").split()))
    maxValue=max(values)
    temp=sum(values)
    print(temp/maxValue*100/len(values))
