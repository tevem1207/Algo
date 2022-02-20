# - - , + + 연속해서 나오는 것들은 의미가 없음. 괄호랑 연관 X이고, - +가 나올경우 +를 우선 계산하는게 유리

sik= input().split('-')
print(sik)

result = 0
plus_result = 0
for i in sik[0].split('+'):
    plus_result += int(i)

for i in sik[1:]:
    for j in i.split('+'):
        result+=int(j)
    plus_result -= result

print(plus_result)