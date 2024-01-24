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
1번째 줄에 수의 개수 N(1<=N<=100000), 합을 구해야 하는 횟수 M(1<=M<=100000)
2번째 줄에 N개의 수가 주어진다. 각 수는 1000보다 작거나 같은 자연수다. 
3번째 줄 부터는 M개의 줄에 합을 구해야 하는 구간 i와 j가 주어진다.

==========Example==========
  input                                     output
  5 3        데이터의 개수, 질의 개수           12
  5 4 3 2 1  구간 합을 구할 대상 배열           9
  1 3                                        1
  2 4
  5 5
===========================
"""
def solution3():
    given=list(map(int,input("데이터의 개수 & 질의 개수 : ").split()))
    numbers=list(map(int, input("numbers : ").split()))
    partialSum=[0]
    answer=[]
    temp=0
    # 구간 합
    for i in range(given[0]):
        temp+=numbers[i]
        partialSum.append(temp)

    for i in range(given[1]):
        question=list(map(int,input("질의 : ").split()))
        answer.append(partialSum[question[1]]-partialSum[question[0]-1])

    print(answer)


"""
문제 4 : 구간 합 구하기 2
N x N개의 수가 N x N 크기의 표에 채워져 있다. 표 안의 수 중 (X1, Y1)에서 (X2, Y2)까지의 합을 구하여 한다. X는 행, Y는 열을 의미한다.
예를 들어 N=4이고, 표가 다음과 같이 채워져 있을 때를 살펴보자. (2,2)에서 (3,4)까지의 합을 구하면 3+4+5+4+5+6=27이고 (4,4)에서 (4,4) 
까지의 합을 구하면 7이다. 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오. (단, X1<  
                                        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
                                        | 1    2    3    4 |
                                        | 2    3    4    5 |
                                        | 3    4    5    6 |
                                        | 4    5    6    7 |
                                        ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
==========Example==========                                                    
                input                                       output
  4 3        2차원 배열의 크기, 구간 합 질의의 개수                27
  1 2 3 4    원본 배열 1번째 줄                                 6
  2 3 4 5    원본 배열 2번째 줄                                 64
  3 4 5 6    원본 배열 3번째 줄
  4 5 6 7    원본 배열 4번째 줄
  2 2 3 4    구간 합 (X1,Y1), (X2,Y2) 1번째 질의
  3 4 3 4    구간 합 (X1,Y1), (X2,Y2) 2번째 질의
  1 1 4 4    구간 합 (X1,Y1), (X2,Y2) 2번째 질의
===========================
"""
def solution4():
    given=list(map(int,input("2차원 배열 크기 & 구간 합 질의 개수 : ").split()))
    matrix=[]
    answer=[]

    for i in range(given[0]):
        matrix.append(list(map(int,input("row : ").split())))

    sum_matrix=matrix
    for i in range(given[0]):
        for j in range(given[0]):
            if(i==0 and j==0):
                continue
            elif(i==0):
                sum_matrix[i][j] = sum_matrix[i][j-1]+matrix[i][j]
            elif(j==0):
                sum_matrix[i][j] = sum_matrix[i-1][j] + matrix[i][j]
            else:
                sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1] + matrix[i][j]
    print(sum_matrix)
    for i in range(given[1]):
        cordinate=list(map(int, input("좌표 : ").split()))
        if(cordinate[0]==1 and cordinate[1]==1):
            answer.append(sum_matrix[cordinate[2]-1][cordinate[3]-1])
        elif(cordinate[0]==1):
            answer.append(
                sum_matrix[cordinate[2] - 1][cordinate[3] - 1]
                - sum_matrix[cordinate[2] - 1][cordinate[1] - 2]
            )
        elif(cordinate[1]==1):
            answer.append(
                sum_matrix[cordinate[2] - 1][cordinate[3] - 1]
                - sum_matrix[cordinate[0] - 2][cordinate[3] - 1]
            )
        else:
            answer.append(
                sum_matrix[cordinate[2] - 1][cordinate[3] - 1]
                - sum_matrix[cordinate[0] - 2][cordinate[3] - 1]
                - sum_matrix[cordinate[2] - 1][cordinate[1] - 2]
                + sum_matrix[cordinate[0] - 2][cordinate[1] - 2]
            )
    # 이거 1행 1열에 0 깔아놓으면 if문 쓸 필요 없음;;
    print(answer)