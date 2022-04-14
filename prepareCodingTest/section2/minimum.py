# 최솟값 구하기
arr=[5, 3, 7, 9, 2, 5, 2, 6, 8]
arrMin=float('inf') #리스트의 최솟값이 저장되는 변수, inf는 파이썬에서 가장 큰 값
#arrMin=arr[0]으로 해도 똑같이 돌아감
#for i in range(1, len(arr)):
for i in range(len(arr)): #i는 인덱스번호
	if arr[i]<arrMin: #첫번째 수가 무조건 참이 된다
		# 5 < inf => arrMin=5
		arrMin=arr[i]
print(arrMin)