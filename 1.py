price = 1260
n = 0

coin_types = [500,100,50,10]

for coin in coin_types:
	n += price // coin
	price %= coin

print(n)

# �׸���˰��� : ���� ��Ȳ���� ���� ���� ���� �͸� ���� ���
# ���� ���� ��� ������ ������ ����� �׸��� �˰����� �����ߴ� ����