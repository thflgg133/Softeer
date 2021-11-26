import sys

N, K = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))

for _ in range(K):
    A, B = map(int, sys.stdin.readline().split())

    avaerage_score = sum(score[A-1:B]) / (B-A+1) # 슬라이싱을 이용해 학생들의 총점수를 구한 후 학생수로 나누어 평균을 구함
    print("{:.2f}".format(avaerage_score)) # 소수점 셋째자리에서 반올림