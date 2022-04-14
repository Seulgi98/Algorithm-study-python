import sys
sys.stdin=open("input3.txt", "rt")
# K 번째 큰 수
n, k=map(int, input().split())
a=list(map(int, input().split()))
# 중복을 제거하는 자료구조 : set()
res=set()
# 3중 for 문
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m]) #set 자료구조는 add
res=list(res) #set에는 sort가 없어서 다시 리스트화
res.sort(reverse=True) #내림차순 정렬
print(res[k-1]) #k번째 = k-1