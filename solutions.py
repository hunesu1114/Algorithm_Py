from queue import PriorityQueue

"""
문제 1 : 숫자의 합 구하기
N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.

==========Params==========
num1 : 숫자의 개수
num2 : 공백 없이 주어진 num1개의 숫자
==========================
"""
def solution1():
    a = int(input("num1 : "))
    b = int(input("num2 : "))
    answer = 0
    for i in range(0, a):
        answer += b % 10
        b = (b - b % 10) / 10
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
    values = list(map(int, input("점수들을 입력 : ").split()))
    maxValue = max(values)
    temp = sum(values)
    print(temp / maxValue * 100 / len(values))


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
    given = list(map(int, input("데이터의 개수 & 질의 개수 : ").split()))
    numbers = list(map(int, input("numbers : ").split()))
    partialSum = [0]
    answer = []
    temp = 0
    # 구간 합
    for i in range(given[0]):
        temp += numbers[i]
        partialSum.append(temp)

    for i in range(given[1]):
        question = list(map(int, input("질의 : ").split()))
        answer.append(partialSum[question[1]] - partialSum[question[0] - 1])

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
    given = list(map(int, input("2차원 배열 크기 & 구간 합 질의 개수 : ").split()))
    matrix = []
    answer = []

    for i in range(given[0]):
        matrix.append(list(map(int, input("row : ").split())))

    sum_matrix = matrix
    for i in range(given[0]):
        for j in range(given[0]):
            if (i == 0 and j == 0):
                continue
            elif (i == 0):
                sum_matrix[i][j] = sum_matrix[i][j - 1] + matrix[i][j]
            elif (j == 0):
                sum_matrix[i][j] = sum_matrix[i - 1][j] + matrix[i][j]
            else:
                sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + matrix[i][j]
    print(sum_matrix)
    for i in range(given[1]):
        cordinate = list(map(int, input("좌표 : ").split()))
        if (cordinate[0] == 1 and cordinate[1] == 1):
            answer.append(sum_matrix[cordinate[2] - 1][cordinate[3] - 1])
        elif (cordinate[0] == 1):
            answer.append(
                sum_matrix[cordinate[2] - 1][cordinate[3] - 1]
                - sum_matrix[cordinate[2] - 1][cordinate[1] - 2]
            )
        elif (cordinate[1] == 1):
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


"""
문제 5 : 나머지 합 구하기
N개의 수 A1, A2, ..,AN이 주어졌을 때 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
즉, Ai+...+Aj (i<=j)의 합이 M으로 나누어 떨어지는 (i,j) 쌍의 개수를 구하시오.

1번째 줄에 N과 M(1<=N<=106, 2<=M<=103), 2번째 줄에 N개의 수 A1,A2,...,AN이 주어진다.(0<=Ai<=109) 
==========Example==========                                                    
           input                           output
  5 3                                        7
  1 2 3 1 2                                   
===========================
"""
def solution5():
    given = list(map(int, input("N과 M 입력 : ").split()))
    numbers = list(map(int, input("numbers : ").split()))
    answer = 0
    sum_list = []
    temp = 0
    for i in range(given[0]):
        temp += numbers[i]
        sum_list.append(temp)
        if (temp % given[1] == 0):
            answer += 1

    for i in range(given[0]):
        for j in range(i + 1, given[0]):
            if ((sum_list[j] - sum_list[i]) % given[1] == 0):
                answer += 1

    # 정석 : 합동식 이용하여 sum_list의 원소들을 M으로 나눈 나머지로 간단히 해놓고 접근
    print(answer)


"""
문제 6 : 연속된 자연수의 합 구하기
어떠한 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 당신은 어떤 자연수 N(1<=N<=10,000,000)을 몇 개의 연속된 자연우싀 합으로 
나타내는 가짓수를 알고 싶다. 이때 사용하는 자연수는 N이어야 한다. 예를 틀어 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5이다. 
반면 10을 나타내는 방법은 10, 1+2+3+4이다. N을 입력받아 연속된 자연수의 합으로 나타내는 가짓수를 출력하는 프로그램을 작성하시오.

1번째 줄에 정수 N이 주어진다.
==========Example==========                                                    
  input                           output
  15                                4
===========================
"""
def solution6():
    given = int(input("자연수 : "))
    l_pointer = 0
    r_pointer = 0
    answer = 1
    temp = 0

    while r_pointer < given:
        if temp < given:
            r_pointer += 1
            temp += r_pointer
        elif temp > given:
            l_pointer += 1
            temp -= l_pointer
        else:
            answer += 1
            r_pointer += 1
            temp += r_pointer

    print(answer)


"""
문제 7 : 주몽의 명령
주몽은 철거군을 양성하기 위한 프로젝트에 나섰다. 그래서 야철대장에게 철기군이 입을 갑옷을 만들라고 명령했다. 야철대장은 주몽의 명령에 따르기 위해 
연구에 착수하던 중 갑옷을 만드는 재료들은 각각 고유한 번호가 있고, 갑옷은 2개의 재료로 만드는 데 2가지 재료의 고유한 번호를 합쳐 M(1<=M<=10,000,000)이
되면 갑옷이 만들어진다는 사실을 뱔견했다. 야철대장은 자신이 만들고 있는 자료로 갑옷을 몇 개난 만들 수 있는지 궁금해졌다. 야철대장의 궁금증을 
풀어 주기 위해 N(1<=N<=15,000)개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

1번째 줄에 재료의 개수 N(1<=N<=15,000), 
2번째 줄에 갑옷을 만드는 데 필요한 수 M(1<=M<=10,000,000)이 주어진다. 
3번째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 고유한 번호는 100,000보다 작거나 같은 자연수이다.
==========Example==========                                                    
  input                                     output
  6            재료의 수                        2
  9            갑옷이 완성되는 번호의 합
  2 7 4 1 5 3  재료들
===========================
"""
def solution7():
    answer = 0
    material = int(input("재료의 수 : "))
    complete_num = int(input("완성 번호 : "))
    numbers = list(map(int, input("재료들 : ").split()))
    numbers.sort()
    l_pointer = 0
    r_pointer = len(numbers) - 1
    temp = numbers[0] + numbers[r_pointer]
    while l_pointer < r_pointer:
        if temp < complete_num:
            temp -= numbers[l_pointer]
            l_pointer += 1
            temp += numbers[l_pointer]
        elif temp > complete_num:
            temp -= numbers[r_pointer]
            r_pointer -= 1
            temp += numbers[r_pointer]
        else:
            answer += 1
            l_pointer += 1
            r_pointer -= 1
            temp = numbers[l_pointer] + numbers[r_pointer]

    print(answer)


"""
문제 8 : '좋은 수' 구하기
주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 '좋은 수'라고 한다. N개의 수 중 좋은 수가 총 몇 개인지 출력하시오.

1번째 줄에 수의 개수 N(1<=N<=2,000),
2번째 줄에 N개의 수의 값(Ai)이 주어진다 (|Ai|<=1,000,000,000 , A는 정수)
==========Example==========                                                    
  input                                         output
  10                     수의 개수                  2
  1 2 3 4 5 6 7 8 9 10
===========================
"""
def solution8():
    answer = 0
    given = int(input("수의 개수 : "))
    numbers = list(map(int, input("수 : ").split()))
    numbers.sort()
    for i in range(2, given):
        l_pointer = 0
        r_pointer = i - 1
        temp = numbers[l_pointer] + numbers[r_pointer]
        while r_pointer < i:
            if temp < i:
                temp -= numbers[l_pointer]
                l_pointer += 1
                temp += numbers[l_pointer]
            elif temp > i:
                temp -= numbers[r_pointer]
                r_pointer -= 1
                temp += numbers[r_pointer]
            else:
                answer += 1
                break

    print(answer)


"""
문제 9 : DNA 비밀번호
DNA 문자열은 모든 문자열에 등장하는 문자가 ('A', 'C', 'G', 'T')인 문자열을 말한다. 예를 들어 "ACKA"는 DNA 문자열이 아니지만, "ACCA"는 
DNA문자열이다. 민호는 임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분 문자열을 비밀번호로 사용하기로 마음먹었다. 

하지만 민호는 이 방법에는 큰 문제가 있다는 것을 발견했다. 임의의 DNA 문자열의 부분 문자열을 뽑았을 때, "AAAA"와 같이 보안에 취약한 비밀번호가 
만들어질 수 있기 때문이다. 그래서 민호는 부분 문자열에서 등장하는 문자의 개수가 특정 개수 이상이어야 비밀번호로 사용할 수 있다는 규칙을 만들었다.
예를들어 임의의 DNA 문자열이 "AAACCTGCCAA"이고, 민호가 뽑을 부분 문자열의 길이를 4라고 가정해보자. 그리고 부분 문자열에 'A'는 1개 이상, 'C'는
1개 이상, 'G'는 1개 이상, 'T'는 0개 이상 등장해야 비밀번호로 사용할 수 있다고 가정해 보자. 예를들어 "ACCT" 사용할 수 없고, "GCCA"는 사용할
수 있다. 

민호가 만든 임의의 DNA 문자열과 비밀번호로 사용할 부분 문자열의 길이 그리고 ('A', 'C', 'G', 'T')가 각각 몇 번 이상 등장해야 비밀번호로 사용
할 수 있는지, 순서대로 주어졌을 때 민호가 만들 수 있는 비밀번호의 종류의 수를 구하는 프로그램을 작성하시오.

단, 부분 문자열이 등장하는 위치가 다르면 부분 문자열의 내용이 같더라도 다른 문자열로 취급한다.

1번째 줄에 민호가 임의로 만든 DNA 문자열의 길이 |S|와 비밀번호로 사용할 부분 문자열의 길이 |P|가 주어진다. (1<=|P|<=|S|<=1,000,000). 
2번째 줄에 민호가 임의로 만든 DNA 문자열이 주어진다. 
3번째 줄에 부분 문자열에 포함돼야 할 ('A', 'C', 'G', 'T')의 최소 개수가 공백문자를 사이에 두고 각각 주어진다. 
각각의 수는 |S|보다 작거나 같은 음이 아닌 정수로 총합은 |S|보다 작거나 같다는 것이 보장된다.
==========Example===========                                                 
  input                                               output
  9 8        DNA 문자열의 길이, 부분 문자열의 길이            0
  CCTGGATTG  DNA 문자열
  2 0 1 1    A,C,G,T의 최소 개수
============================
"""
def solution9():
    answer = 0
    given = list(map(int, input("문자열 길이 & 부분 문자열 길이 : ").split()))
    givenString = input("문자열 : ")
    condition = list(map(int, input("A,C,G,T 최소개수 : ").split()))
    endIndex = given[1] - 1
    startIndex=endIndex-given[1]+1

    temp = givenString[startIndex:endIndex + 1]
    checkCondition = [0] * 4
    for s in temp:
        if s == 'A':
            checkCondition[0] += 1
        elif s == 'C':
            checkCondition[1] += 1
        elif s == 'G':
            checkCondition[2] += 1
        else:
            checkCondition[3] += 1

    if (condition[0] <= checkCondition[0] and
        condition[1] <= checkCondition[1] and
        condition[2] <= checkCondition[2] and
        condition[3] <= checkCondition[3]):
        answer+=1

    while endIndex < given[0] - 1:
        outChar=givenString[startIndex]
        inChar=givenString[endIndex+1]

        if outChar == 'A':
            checkCondition[0] -= 1
        elif outChar == 'C':
            checkCondition[1] -= 1
        elif outChar == 'G':
            checkCondition[2] -= 1
        else:
            checkCondition[3] -= 1

        if inChar == 'A':
            checkCondition[0] += 1
        elif inChar == 'C':
            checkCondition[1] += 1
        elif inChar == 'G':
            checkCondition[2] += 1
        else:
            checkCondition[3] += 1

        startIndex+=1
        endIndex+=1

        if (condition[0] <= checkCondition[0] and
            condition[1] <= checkCondition[1] and
            condition[2] <= checkCondition[2] and
            condition[3] <= checkCondition[3]):
            answer += 1

    print(answer)


"""
문제 10 : 최솟값 찾기 1
N개의 수 A1,A2,...AN 과 L이 주어진다. A(i-L+1)~Ai 중 최솟값을 Di라고 할 때 D에 저장된 수를 출력하는 프로그램을 작성하시오.
이때 i<=0인 Ai는 무시하고 D를 구해야 한다.

1번째 줄에 N과 L(1<=L<=N<=5,000,000),
2번째 줄에 N개의 수 Ai가 주어진다
==========Example==========                                                    
  input                                                         output
  12 3                      숫자의 개수, 슬라이딩 윈도우 크기         1 1 1 2 2 2 2 2 3 3 2 2
  1 5 2 3 6 2 3 7 3 5 2 6
===========================
"""
def solution10():
    # 정렬 안쓰고 deque로 풀어보기
    answer = []
    given=list(map(int, input("숫자 개수 & 윈도우 크기 : ").split()))
    numbers=list(map(int, input("수 : ").split()))
    endIdx=1
    startIdx=endIdx-given[1]
    while endIdx<=given[0]:
        if startIdx<0:
            temp=numbers[0:endIdx]
            temp.sort()
            answer.append(temp[0])
        else:
            temp = numbers[startIdx:endIdx]
            temp.sort()
            answer.append(temp[0])

        endIdx+=1
        startIdx+=1

    print(answer)


"""
문제 11 : 스택으로 수열 만들기
1부터 n까지의 수를 스택에 저장하고 출력하는 방식으로 하나의 수열을 만들 수 있다. 이때 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다.
수열이 주어졌을 때 이러한 방식으로 스택을 이용해 주어진 수열을 만들 수 있는지 확인하고 만들 수 있다면 어떤 순서로 push와 pop을 수행해야 하는지
확인하는 프로그램을 작성해 보자.

1번째 줄에 수열의 개수 n(1<=n<=100,000)이 주어진다.
2번쨰 줄에는 수열을 이루는 1이상 n이하의 정수가 1개씩 순서대로 주어진다. 이때 같은 정수가 두 번 이상 나오지는 않는다.

수열을 만들기 위한 연산 순서를 출력한다. push연산은 +, pop연산은 -로 출력하고, 불가능할 때는 NO를 출력한다.
==========Example==========                                                    
  input                             output
  8                수열의 개수        ++++--++-++-----
  4 3 6 8 7 5 2 1

  5                수열의 개수         NO
  1 2 5 3 4
===========================
"""
def solution11():
    answer = ""
    given=int(input("수의 개수 : "))
    numbers=list(map(int, input("수열 : ").split()))
    stack=[]
    elt=1
    for i in range(given):
        while True:
            if elt<numbers[i]:
                stack.append(elt)
                answer+='+'
                elt+=1
            elif elt==numbers[i]:
                answer+="+-"
                elt+=1
                break
            else:
                if stack.pop()==numbers[i]:
                    answer+='-'
                else:
                    answer="NO"
                break
        if answer=="NO":
            break

    print(answer)


"""
문제 12 : 오큰수 구하기
크기가 N인 수열 A=A1,A2,...,An이 있다. 수열의 각 원소 Ai에 관련된 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 
수 중 가장 왼쪽에 있는 수를 의미한다. 이러한 수가 없을 때 오큰수는 -1이다. 예를 들어 A=[3,5,2,7]일 때 NGE(1)=5, NGE(2)=7, NGE(3)=7,
NGE(4)=-1 이다. A=[9,5,4,8]일 경우에는 NGE(1)=-1, NGE(2)=8, NGE(3)=8, NGE(4)=-1이다.

1번째 줄에 수열 A의 크기 N(1<=N<=1,000,000),
2번째 줄에 수열 A의 원소가 주어진다.(1<=원소<=1,000,000)
==========Example==========                                                    
  input                             output
  4                수열의 크기        5 7 7 -1
  3 5 2 7

  4                수열의 크기        -1 8 8 -1
  9 5 4 8
===========================
"""
def solution12():
    # 떠올리기 어려움...책 보고 함
    given=int(input("수열의 크기 : "))
    numbers=list(map(int, input("수열 : ").split()))
    stack=[]
    answer = [0]*given

    for i in range(given):
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()]=numbers[i]
        stack.append(i)

    for i in range(given):
        if answer[i]==0:
            answer[i]=-1

    print(answer)


"""
문제 13 : 카드 게임
N장의 카드가 있다. 각각의 카드는 차례로 1에서 N까지의 번호가 붙어 있으며, 1번 카드가 가장 위, N번 카드가 가장 아래인 상태로 놓여 있다.
이제 다음과 같은 동작을 카드가 1장 남을 때까지 반복한다.

먼저 가장 위에 있는 카드를 바닥에 버린다. 그다음 가장 위에 있는 카드를 가장 아래에 있는 카드 및으로 옮긴다. 예를 들어 N=4일 떄를 생각해 보자.
카드는 가장 위에서부터 1,2,3,4의 순서대로 놓여있다. 1을 버리면 2,3,4가 남는다. 여기서 2를 가장 아래로 옮기면 순서가 3,4,2가 된다. 3을 버리면 
4,2가 남고, 4를 밑으로 옮기면 순서가 2,4가 된다. 마지막으로 2를 버리면 카드 4가 남는다. N이 주어졌을 때 가장 마지막에 남는 카드를 구하는 
프로그램을 작성하시오.

1번째 줄에 정수 N이 주어진다.

남는 카드의 번호를 출력한다.
==========Example==========                                                    
  input                   output
  6      카드의 개수        4
===========================
"""
def solution13():
    answer = 0
    n=int(input("N : "))
    deque=[]
    # 0이면 버리고 1이면 아래로
    temp=0
    for i in range(1,n+1):
        deque.append(n-i+1)
    while len(deque)>1:
        if temp==0:
            deque.pop()
            temp+=1
        else:
            top=deque.pop()
            deque.insert(0,top)
            temp-=1

    print(deque[0])


"""
문제 14 : 절댓값 힙 구현하기
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조다.
    1) 배열에 정수 x(x!=0)을 넣는다.
    2) 배열에서 절댓값이 가장 작은 값을 출력한 후 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러 개일 경우에는 그중 가장 작은 수를 
       출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작한다. 절댓값 힙을 구현하시오.

1번째 줄에 연산의 개수 N(1<=N<=100,000)이 주어진다. 
2번째 줄에는 연산과 관련된 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 추가하고, x가 0이라면 배열에서 절댓값이 
가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 

입력해서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어있는데 절댓값이 가장 작은 값을 출력하라고 할 때는 0을 출력하면 된다. 
==========Example==========                                                    
  input                                         output
  18      연산의 개수                             -1 1 0 -1 -1 1 1 -2 2 0
  1 -1 0 0 0 1 1 -1 -1 2 -2 0 0 0 0 0 0 0
===========================
"""
def solution14():
    # PriorityQueue import
    answer = []
    given=int(input("N : "))
    numbers=list(map(int, input("numbers : ").split()))
    myQueue=PriorityQueue()

    for i in range(given):
        number=numbers[i]
        if number==0:
            if myQueue.empty():
                answer.append(0)
            else:
                answer.append(myQueue.get()[1])
        else:
            # 튜플 형식으로 저장 -> 정렬 기준 정할 수 있음
            myQueue.put((abs(number),number))

    print(answer)


"""
문제 15 : 수 정렬하기 1
N개의 수가 주어졌을 때 이를 오름차순 정렬하는 프로그램을 작성하시오.

1번째 줄에 수의 개수 N(1<=N<=1,000),
2번째 줄에 N개의 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수다. 수는 중복되지 않는다.
==========Example==========                                                    
  input                     output
  5          수의 갯수       1 2 3 4 5
  5 2 3 4 1
===========================
"""
def solution15():
    answer = 0
    n=int(input("N : "))
    numbers=list(map(int,input("numbers : ").split()))
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j + 1]
                numbers[j+1]=numbers[j]
                numbers[j]=temp

    print(numbers)


"""
문제 16 : 버블 정렬 프로그램 1
영식이는 다음과 같은 버블 정렬 프로그램을 C++로 작성했다.
    bool change = false;
    for(int i = 1; i <= n+1; i++) {
        change = false;
        for(int j = 1; j <= n-i; j++) {
            if(a[j] > a[j+1]) {
                change = true;
                swap(a[j], a[j+1]);
            }
        }
        if(change == false) {
            cout << i << '\n';
            break;
        }
    }

위 코드에서 n은 배열의 크기, a는 수가 들어있는 배열이다. 수는 배열의 1번 방부터 채운다. 위와 같은 코드를 실행시켰을 때 어떤 값이 출력되는지를 
구하는 프로그램을 작성하시오.

1번째 줄에 N이 주어진다. N은 500,000보다 작거나 같은 자연수다. 
2번째 줄에 A[1]부터 A[N]까지 1개씩 주어진다. A에 들어있는 수는 1,000,000보다 작거나 같은 자연수 또는 0이다.
==========Example==========                                                    
  input                     output
  5          배열의 크기        3
  10 1 5 2 3
===========================
"""
def solution16():
    # 버블 정렬 쓰면 안됨 -> 다시 풀기
    answer = 0
    n=int(input("N : "))
    numbers=list(map(int,input("numbers : ").split()))
    for i in range(n):
        change=False
        for j in range(n-i-1):
            if numbers[j]>numbers[j+1]:
                temp=numbers[j+1]
                numbers[j+1]=numbers[j]
                numbers[j]=temp
                change=True
        if change==False:
            answer+=1

    print(answer)


"""
문제 17 : 내림차순으로 자릿수 정렬하기
배열을 정렬하는 것은 쉽다. 수가 주어지면 그 수의 각 자릿수를 내림차순으로 정렬하시오.

1번째 줄에 정렬할 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수다.
==========Example==========                                                    
  input           output
  2 1 4 3         4 3 2 1       
===========================
"""
def solution17():
    numbers=list(map(int,input("numbers : ").split()))
    numbers.sort()
    print(numbers)

"""
문제 18 : ATM 인출 시간 계산하기
==========Example==========                                                    
  input           output
  5               32
  3 1 4 3 2       
===========================
"""
def solution18():
    answer=0
    given=int(input("N : "))
    numbers=list(map(int,input("numbers : ").split()))
    numbers.sort()
    for i in range(given):
        answer+=numbers[i]*(given-i)
    print(answer)


"""
문제 19 : K번째 수 구하기
==========Example==========                                                    
  input           output
  5 2              2
  4 1 2 3 5      
===========================
"""
def solution19():
    given=list(map(int,input("N & index : ").split()))
    numbers=list(map(int, input("numbers : ").split()))
    numbers.sort()
    print(numbers[given[1]-1])

"""
문제 20 : 수 정렬하기 2
==========Example==========                                                    
  input           output
  5               1 2 3 4 5
  5 4 3 2 1       
===========================
"""
def solution20():
    answer=0
    # sort()
    print(answer)


"""
문제 21 : 버블 정렬 프로그램 2
==========Example==========                                                    
  input             output
  8                 11
  3 2 8 1 7 4 5 6       
===========================
"""
def solution21():
    given=int(input("N : "))
    numbers = list(map(int, input("numbers : ").split()))
    answer=0
    for i in range(given):
        for j in range(given-i-1):
            if(numbers[j]>numbers[j+1]):
                temp=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
                answer+=1
    print(answer)

"""
문제 22 : 수 정렬하기 3
==========Example==========                                                    
  input                                             output
  11 
  215 15 344 372 294 100 8 145 24 198 831           8 15 24 100 145 198 215 294 344 372 831
===========================
"""
def solution22():
    answer=0
    # sort()
    print(answer)

"""
문제 23 : 연결 요소의 개수 구하기
방향 없는 그래프가 주어졌을 때 연결 요소의 개수를 구하는 프로그램을 작성하시오.

1번째 줄에 노드의 개수 N 과 엣지의 개수 M,
2번째 줄부터 M개의 줄에 엣지의 양끝 점 u와 v (u!=v)가 주어진다. 같은 엣지는 한번만 주어진다.
==========Example==========                                                    
#1  
  input                                             output
  6 5       노드의 개수, 엣지 개수                      2 
  1 2
  2 5
  5 1
  3 4
  4 6

#2
  input                                             output
  6 8       노드의 개수, 엣지 개수                      1 
  1 2
  2 5
  5 1
  3 4
  4 6
  5 4
  2 4
  2 3
===========================
"""
def solution23():
    # DFS -> 인접리스트, 재귀함수, 방문리스트 선언부터
    answer=0
    n, e=map(int,input("노드의 개수 & 엣지 개수 : ").split())
    nList=[[] for _ in range(n+1)]
    vList=[False]*(n+1)

    # 재귀함수로 탐색!
    def DFS(v):
        vList[v]=True
        for i in nList[v]:
            if not vList[i]:
                DFS(i)

    for i in range(e):
        nodes=list(map(int,input("인접 노드 : ").split()))
        nList[nodes[0]].append(nodes[1])
        nList[nodes[1]].append(nodes[0])

    print("nList : {0}".format(nList))

    for i in (1,len(vList)-1):
        if not vList[i]:
            answer+=1
            DFS(i)

    print(answer)

"""
문제 24 : 신기한 소수 찾기
소수 7331은 733도 소수, 73도 소수, 7도 소수다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자릿수 모두 소수다. 이런 숫자를 신기한 소수라 하자.
N(1<=N<=8)의 자리의 숫자 중 신기한 소수를 모두 찾는 코드를 구현하시오.
 
==========Example==========                                                    
  input                       output
  4                           2333 2339 2393 2399 2939 3119 3137 3733 3739 3793 3797 5939 7193 7331 7333 7393
===========================
"""
def solution24():
    answer=[]
    n=int(input("자릿수 : "))

    # 소수 판별
    def primeCriteria(n):
        for i in range(2, int(n**(1/2)+1)):
            if n%i==0:
                return False
        return True

    def DFS(v):
        for i in range(10):
            number = v*10+i
            if primeCriteria(number):
                if number//(10**(n-1)) > 0:
                    if number//(10**(n-1))>9:
                        break
                    else:
                        answer.append(number)
                else :
                    DFS(number)

    for i in range(2,10):
        if primeCriteria(i):
            DFS(i)

    print(answer)


"""
문제 25 : 친구 관계 파악하기
총 N(5<=N<=2000) 명의 사람이 있다. 사람들은 0번 부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구다. 이때, 다음과 같은 친구 관계를 가진
사람 A,B,C,D,E가 존재하는지 구해보려고 한다.
    - A는 B와 친구다.
    - B는 C와 친구다.
    - C는 D와 친구다.
    - D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 여부를 구하는 프로그램을 작성하시오.

1번째 줄에 사람의 수 N과 친구 관계의 수(1<=M<=2000),
2번째 줄부터 M개의 줄에 정수 a와 b가 주어진다. a와 b는 친구라는 뜻이다. 같은 친구 관계가 2번 이상 주어지지는 않는다.
문제의 조건에 맞는 A,B,C,D,E가 존재하면 1, 없으면 0을 출력한다.
==========Example==========                            
#1                                          #2
  input                       output        input                       output
  8 8                         1             5 5                         1
  1 7                                       0 1
  3 7                                       1 2
  4 7                                       2 3
  3 4                                       3 0
  4 6                                       1 4
  3 5
  0 4
  2 7
  
#3                                          #4
  input                       output        input                       output
  6 5                         0             5 4                         1
  0 1                                       0 1
  0 2                                       1 2
  0 3                                       2 3
  0 4                                       3 4
  0 5
===========================
"""
def solution25():
    answer = 0
    n,m=map(int, input("사람수 & 관계수 : ").split())
    nList=[[] for _ in range(n)]
    vList=[False]*n

    def DFS(v,depth):
        print(depth)
        nonlocal answer
        if depth==5:
            answer=1
        vList[v]=True
        for i in nList[v]:
            if not vList[i]:
                DFS(i,depth+1)

    for i in range(m):
        a, b=map(int,input("사람 번호 두개 : ").split())
        nList[a].append(b)
        nList[b].append(a)

    print("nList : {0}".format(nList))

    for i in range(n):
        print("i : {0}".format(i))
        DFS(i,1)
        # 각 노드에서 최대 길이를 잴거라서 visit 초기화 해줘야 함
        vList = [False] * n

    print("answer : {0}".format(answer))


"""
문제 26 : DFS와 BFS 프로그램
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 노드가 여러 개일 경우에는 노드 번호가
작은 것을 먼저 방문하고 더 이상 방문할 수 있는 노드가 없을 때 종료한다. 노드 번호는 1에서 N까지다(1<=N<=1000).

1번째 줄에 노드의 개수 N, 엣지의 개수 M(1<=M<=10000), 탐색을 시작할 노드의 번호 V가 주어진다.
그다음 M개의 줄에는 엣지가 연결하는 두 노드의 번호가 주어진다. 어떤 두 노드 사이에 여러 개의 엣지가 있을 수 있다.
입력으로 주어지는 엣지는 양방향이다.

DFS와 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
==========Example==========                                                    
#1
  input                       output
  4 5 1                       1 2 4 3
  1 2                         1 2 3 4
  1 3
  1 4
  2 4
  3 4

#2
  input                       output
  5 5 3                       3 1 2 5 4
  5 4                         3 1 4 2 5
  5 2
  1 2
  3 4
  3 1
===========================
"""
def solution26():
    answer = [[],[]]
    n,m,s=map(int,input("노드 개수 & 엣지 개수 & 시작 번호 : ").split())
    nList=[[] for _ in range(n+1)]
    vList1=[False]*(n+1)
    vList2=[False]*(n+1)

    def DFS(v):
        answer[0].append(v)
        vList1[v]=True
        for i in nList[v]:
            if not vList1[i]:
                DFS(i)

    for i in range(m):
        a,b=map(int,input("노드 번호 : ").split())
        nList[a].append(b)
        nList[b].append(a)
        nList[a].sort()
        nList[b].sort()

    myQueue=[s]
    vList2[s] = True
    while myQueue:
        node=myQueue.pop()
        answer[1].append(node)
        for i in nList[node]:
            if not vList2[i]:
                myQueue.insert(0, i)
                vList2[i]=True


    DFS(s)
    print(answer)


"""
문제 27 : 미로 탐색하기
4x6 크기의 배열로 표현되는 다음과 같은 미로가 있다.
                            1 0 1 1 1 1
                            1 0 1 0 1 0
                            1 0 1 0 1 1
                            1 1 1 0 1 1
미로의 각 칸에 들어 있는 숫자 중 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸을 나타낸다. 한 칸에서 다른 칸으로 이동할 때는 서로 인접한 
칸으로만 이동할 수 있다. 이동한 칸을 셀 때는 시작 위치와 도착 위치를 포함한다. 즉, (1,1)에서 (4,6)으로 이동하려면 총 15칸을 지나야 한다.
NxM 크기의 미로가 주어질 때 (1,1)에서 출발해 (N,M)의 위치로 이동하기 위해 지나야 하는 칸 수의 최솟값을 구하는 프로그램을 작성하시오.

1번째 줄에 두 정수 N,M(2<=N, M<=100), 그 다음 N개의 줄에는 미로의 내용이 M개의 정수로 주어진다. 각각의 수들은 붙어서 입력된다.

지나야 하는 칸 수의 최솟값을 출력한다. 항상 도착 위치로 이동할 수 있을 때만 입력으로 주어진다.
==========Example==========                                                    
#1                                          #2
  input                       output        input                       output
  4 6                         15            4 6                         9
  101111                                    110110
  101010                                    110110
  101011                                    111111
  111011                                    111101
    
#3                                          #4
  input                       output        input                       output
  2 25                        38            7 7                         13
  1011101110111011101110111                 1011111
  1110111011101110111011101                 1110001
                                            1000001
                                            1000001
                                            1000001
                                            1000001
                                            1111111
                                            
===========================
"""
def solution27():
    answer = 0
    print(answer)


"""
문제 28 : 트리의 지름 구하기
트리의 지름은 트리를 구성하는 노드 중 두 노드 사이의 거리가 가장 긴 것을 말한다. 트리의 지름을 구하시오.

1번째 줄에서는 트리의 노드 개수 V(2<=V<=100,000),
2번째 줄부터 V개의 줄에 걸쳐 엣지의 정보가 주어진다. 
먼저 노드 번호가 주어지고, 그 다음으로 연결된 엣지의 정보를 의미하는 정수가 2개씩(연결된 노드 번호, 거리) 주어진다. 거리는 10,000 이하의 자연수다.

예를 들어 2번째 줄에 3 1 2 4 3 -1이 주어질 때 노드 3은 노드 1과 거리가 2인 엣지로 연결돼 있고, 노드 4는 거리가 3인 엣지로 연결돼 있다는 뜻이다.
-1은 더이상 노드가 없으므로 종료한다는 의미다.

트리의 지름을 출력한다.
==========Example==========                                                    
  input                       output
  5                           11
  1 3 2 -1
  2 4 4 -1
  3 1 2 4 3 -1
  4 2 4 3 3 5 6 -1
  5 4 6 -1
===========================
"""
def solution28():
    answer = 0
    print(answer)


"""
문제 29 : 원하는 정수 찾기
N개의 정수 A[1], A[2], ...,A[N]이 주어져 있을 때 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

1번째 줄에 자연수 N,
그 다음 줄에 N개의 정수가 주어진다.
그 다음 줄에 M,
그 다음 줄에 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2^31이상 2^31이하다.

존재하면 1, 않으면 0을 출력한다.
==========Example==========                                                    
  input                       output
  5        데이터의 개수        1
  4 1 5 2 3                   1
  5                           0
  1 3 7 9 5                   0
                              1
===========================
"""
def solution29():
    answer = 0
    print(answer)


"""
문제 30 : 블루레이 만들기
블루레이에는 총 N개의 영상이 들어가는데, 블루레이를 녹화할 때 영상의 순서가 바뀌면 안된다. i,j번 영상을 같은 블루레이에 녹화하려면 i와 j 사이의
모든 영상도 같은 블루레이에 녹화해야 한다. 블루레이 제작 개수를 최소화 하려고 한다. M개의 블루레이에 모든 영상을 녹화하기로 하였을 때, 블루레이의
크기(녹화할 수 있는 길이)는 최소, M개의 블루레이는 모두 같은 크기로 만드려고 한다. 각 영상의 길이가 분 단위(자연수)로 주어질 때 가능한 블루레이의
크기 중 최솟값을 구하는 프로그램을 작성하시오.

1번째 줄에 영상의 수 N 과 블루레이의 수 M,
2번째 줄에 영상 길이가 영상 순서대로 분 단위로 주어진다.
==========Example==========                                                    
  input                       output
  9 3   영상 수, 블루레이 수     17
  1 2 3 4 5 6 7 8 9
===========================
"""
def solution30():
    answer = 0
    print(answer)


"""
문제 31 : 배열에서 K번째 수 찾기
세준이는 크기가 NxM인 배열 A를 만들었다. 배열에 들어있는 수는 A[i][j]=i*j이다. 이 수를 1차원 배열 B에 넣으면 B의 크기는 NxM이 된다.
B를 오름차순 정렬했을 때, B[k]를 구하라. (배열 A와 B의 인덱스는 1부터 시작한다.)

1번째 줄에 배열의 크기 N이 주어진다. N은 10^5 보다 작거나 같은 자연수다. 
2번째 줄에 k가 주어진다. k는 min(10^9, N^2)보다 작거나 같은 자연수다.
==========Example==========                                                    
  input                       output
  3                           6
  7
===========================
"""
def solution31():
    answer = 0
    print(answer)

"""
문제 32 : 동전 개수의 최솟값 구하기
동전은 총 N종류이고, 각 동전의 개수가 많다. 동전을 적절히 사용해 그 가격의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하라

1번째 줄에 N과 K,
2번째 줄부터 N개의 줄에 동전의 가격 Ai가 오름차순으로 주어진다. (Ai는 Ai-1의 배수)
==========Example==========                                                    
#1
  input                           output
  10 4200     동전 수, 목표 금액     6
  1
  5
  10
  50
  100
  500
  1000
  5000
  10000
  50000
  
#2
  input                           output
  10 4790     동전 수, 목표 금액     12
  1
  5
  10
  50
  100
  500
  1000
  5000
  10000
  50000
===========================
"""
def solution32():
    answer = 0
    print(answer)


"""
문제 33 : 카드 정렬하기
정렬된 두 묶음의 숫자 카드가 있다. 각 묶음의 카드의 개수가 A,B일 때 보통 두 묶음을 합쳐 1개로 만드려면 A+B번 비교해야 한다.
예를 들어, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다고 가정해보다. 이들을 두 묶음씩 골라 서로 합쳐 나가면 고르는 순서에 따라 비교 횟수가 달라진다.
예를 들어, 10장,20장,40장의 묶음이 있다면 10장과 20장을 합친 후 합친 30장 묶음과 40장을 합치면 (10+20)+(30+40) = 100번의 비교가 필요하다.
그러나 10장과 40장을 합친 후 합친 50장 묶음과 20장을 합치면 (10+40)+(50+20) = 120번의 비교가 필요하므로 덜 효율적이다.
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때 최소 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

1번째 줄에 N이 주어진다. 
그다음 N개의 줄에 걸쳐 숫자 카드의 묶음의 각각의 크기가 주어진다. 숫자카드 묶음의 크기는 1000보다 작거나 같은 양의 정수다. 
==========Example==========                                                    
  input                       output
  3      카드 묶음의 수          100
  10
  20
  40
===========================
"""
def solution33():
    answer = 0
    print(answer)


"""
문제 34 : 수를 묶어서 최댓값 만들기
길이가 N인 수열이 주어질 때 수열의 합을 구하려고 한다. 그런데 수열의 합을 구하기 전에 먼저 수열 안에 있는 임의의 두 수를 묶으려 한다.
위치에 상관없이 두 수를 묶을 수 있다. 단, 같은 위치에 있는 수(자기 자신)를 묶을 수는 없다. 묶인 두 수는 수열의 합을 구할 때 서로 곱한 후 
계산한다. 수열의 모든 수는 각각 한 번씩만 묶을 수 있다. 예를 들어 어떤 수열이 {0,1,2,4,3,5}일 때 그냥 이 수열의 합을 구하면 15이다.
하지만 2와 3을 묶고, 4와 5를 묶으면 0+1+(2*3)+(4*5) = 27이 되어 최댓값이 나온다. 주어진 수열의 각 수를 적절히 묶어 그 합을 최대로 만드는
프로그램을 작성하시오.

1번째 줄에 수열의 크기 N이 주어진다. N은 10,000보다 작은 자연수다.
2번째 줄에 수열이 주어진다. 수열의 수는 -10000이상 10000이하인 정수다.
==========Example==========                                                    
  input                       output
  9     수의 개수               62
  -1 -8 2 1 3 6 -5 0 1
===========================
"""
def solution34():
    answer = 0
    print(answer)


"""
문제 35 : 회의실 배정하기
1개의 회의실에서 N개의 회의를 진행하기 위해 회의실 사용표를 만드려고 한다. 각 회의마다 시작 시간과 끝나는 시간이 주어질 때 회의 시간이 겹치지
않으면서 회의를 가장 많이 진행하려면 최대 몇 번까지 할 수 있는지 알아보자. 단, 회의를 시작하면 중간에 중단할 수 없고, 한 회의를 끝내는 것과
동시에 다음 회의를 시작할 수 있다. 회의의 시작 시간과 끝나는 시간이 같을 수도 있는데, 이때는 시작하자마자 끝나는 것으로 생각하면 된다.

1번째 줄에 회의의 수 N, 
2번째 줄부터 N+1줄까지는 각 회의의 시작 시간과 끝나는 시간이 주어진다.
==========Example==========                                                    
  input                       output
  11    회의 개수               4
  1 4
  3 5
  0 6
  5 7
  3 8
  5 9
  6 10
  8 11
  8 12
  2 13
  12 14
===========================
"""
def solution35():
    answer = 0
    print(answer)


"""
문제 36 : 최솟값을 만드는 괄호 배치 찾기
세준이는 양수와 +,- 그리고 괄호를 이용해 어떤 수식을 만들었다. 그리고 괄호를 모두 지우고, 다시 괄호를 적절히 넣어 이 수식의 값을 최소로 만드려고 한다.
이렇게 수식의 괄호를 다시 적절하게 배치해 수식의 값을 최소로 만드는 프로그램을 작성하시오.

1번째 줄에 식이 주어진다. 
==========Example==========                                                    
  input                          output
  100-40+50+74-30+29-45+43+11    -222
===========================
"""
def solution36():
    answer = 0
    print(answer)