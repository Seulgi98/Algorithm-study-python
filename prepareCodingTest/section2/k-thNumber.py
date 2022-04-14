import sys
sys.stdin=open("input2.txt", "rt")
# K번째
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split()) # 첫번째 케이스 4가지 input 2번째 줄
    a=list(map(int,input().split())) # 한줄 통째로 읽고 리스트화
    a=a[s-1:e] #s번째(s-1)부터 e번째 까지 추출, 첫번째는 0이니까 s-1,인덱스 e는 e-1까지이니까 그대로 작성
    # a=a[1:5] 인덱스 1번부터 4번 인덱스 까지 추출
    a.sort() # 오름차순 정렬
    print("#%d %d" %(t+1, a[k-1]))# k번째 숫자 인덱스 = k-1
    # t => #%d에 대응, a[k-1] => %d에 대응
    # 0번부터 돌고있기 때문에 t+1