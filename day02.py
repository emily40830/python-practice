x = 5

print(x == 5)
print(x != 5)
print(x > 2)
print(x < 2)

lower = [];upper = [];

for i in range(10):
	if i < 5:
		lower.append(i)
	else:
		upper.append(i)
print(lower)
print(upper)

rain = input('有沒有下雨：')

if rain == 'yes':
	print('umbrella')