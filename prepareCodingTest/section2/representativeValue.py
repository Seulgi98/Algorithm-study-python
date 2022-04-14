import sys
sys.stdin=open("input4.txt", "rt")
# 대표값
n=int(input()) #n명의 학생
a=list(map(int, input().split())) #수학성적
ave=round(sum(a)/n) #평균
#round : 소수 첫째자리에서 반올림
#sum : a리스트의 값을 모두 합쳐줌
min=2147000000 # 큰 값으로 선언하고 최소값 비교

for idx, x in enumerate(a): #idx:학생번호, x:성적
    # enumerate:리스트의 인덱스와 값을 쌍으로 대응시켜줌(idx를 인덱스, x를 값으로 )
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1 #idx는 0번부터니까 +1해준다
    elif tmp==min: #같은 거리를 갖는 성적
        if x>score:
            score=x
            res=idx+1 #점수가 더 큰학생의 번호로

print(ave, res) #평균, 학생번호