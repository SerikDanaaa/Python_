n, words, ans = int(input()), [], []
for i in range(n):
    words.append(input())
for char in words[0]:
    ok = True
    for i in range(n):
        if words[i].find(char) == -1:
            ok = False
            break
    if ok == True:
        ans.append(char)
if len(ans) != 0:
    print(*sorted(set(ans)))
else:
    print('NO COMMON CHARACTERS')
