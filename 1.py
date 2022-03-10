price = 1260
n = 0

coin_types = [500,100,50,10]

for coin in coin_types:
	n += price // coin
	price %= coin

print(n)

# 그리디알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 위의 경우는 모든 동전의 종류가 배수라서 그리디 알고리즘이 가능했던 것임