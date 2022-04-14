import sys
sys.stdin=open("input5.txt", "r")
# 정다면체
n, m=map(int, input().split())
cnt=[0]*(n+m+3) # 눈의합이 n+m까지, +3은 넉넉하게 cnt리스트는 0으로 초기화되면서 n+m+3만큼 크기가 생긴다
max=-2147000000

for i in range(1, n+1): # 1~n까지
    for j in range(1, m+1): # 1~m까지
        cnt[i+j]+=1 # 눈의 합이 나올때마다 +1씩 증가
#나타나는 빈도수 최대값 찾기
for i in range(n+m+1): #n+m+1까지
    if cnt[i]>max:
        max=cnt[i] #최대값 찾기
for i in range(n+m+1):
    if cnt[i]==max: #가장 큰 빈도수 눈의 합
        # i 가 숫자
        print(i, end=' ') # 한칸 띄워서 출력