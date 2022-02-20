
def is_groupword(chars):
    dictlist = {}
    for i in chars:
        if i in dictlist:
            dictlist[i] += 1 
        else:
            dictlist[i] = 1
    new_list =[]

    for i in list(dictlist.keys()):
        for _ in range(dictlist[i]):
            new_list.append(i)

    for i in range(len(chars)):
        if new_list[i] == chars[i]:
            if i == len(chars)-1:
                return 1
        else:
            return 0
            break

N = int(input())

total = 0
sentences = [input() for _ in range(N)]
for sentence in sentences:
    total += is_groupword(sentence)
print(total)