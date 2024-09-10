def good():
    return ['Harry','Ron','Hermione']

print(good())

def get_odds():
    for x in range(1,10,2):
        yield x

cnt=1
for x in get_odds():
    if cnt==3:
        break
    cnt+=1

print("number is",x)
