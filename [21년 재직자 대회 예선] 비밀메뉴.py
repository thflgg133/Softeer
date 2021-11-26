import sys

M, N, K = map(int, sys.stdin.readline().split())
secret_menu = ''.join(list(sys.stdin.readline().rstrip().split())) # join 함수를 이용해 리스트로 받은 secret_menu를 문자열화 시킴
button = ''.join(list(sys.stdin.readline().rstrip().split())) # join 함수를 이용해 리스트로 받은 button을 문자열화 시킴

if secret_menu in button:
    print('secret')

else:
    print('normal')