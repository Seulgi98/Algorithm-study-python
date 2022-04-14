import sys
sys.stdin=open("input1.txt", "rt")
# K번째 약수 문제
# input = 6 3 / output = 3

n, k=map(int, input().split())
# 띄워쓰기 되있어서 split 사용
# string 형이니까 int 형으로 바꾸고
# map시켜준다
cnt=0
for i in range(1, n+1): # n까지가 약수이니까 n+1로 범위지정
    if n%i==0: # i로 나눴을때 0이면 약수
        cnt+=1 # cnt=cnt+1
    if cnt==k: # k번째 약수일 때
        print(i)
        break
else: #약수를 발견하지 못했을 때
    print(-1)