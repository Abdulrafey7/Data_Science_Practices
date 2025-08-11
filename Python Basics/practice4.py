import random
c1 = "101101"
c2 = "101111"

m_rate = 0.5
def mutate(c):
    listing=list(c)
    for x in range(len(listing)):
        if random.random()<m_rate:
            if listing[x]=='0':
                listing[x]='1'
            else:
                listing[x]='0'
    return "".join(listing)


print(help(zip))