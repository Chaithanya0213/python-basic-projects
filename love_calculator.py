Your_name=input("Enter your name: ").lower()
Partner_name=input("Enter your partner name: ").lower()
data=Your_name + Partner_name

t = data.count('t')
r = data.count('r')
u = data.count('u')
e = data.count('e')
true=str(t + r + u + e)

l = data.count('l')
o = data.count('o')
v = data.count('v')
e = data.count('e')
love=str(l+ o + v + e)


love_score=int(str(true + love))

if love_score<10 or love_score>90:
    print(f"Your love score is {love_score}%")
elif love_score>=40 and love_score<=60:
    print(f"Your love score is {love_score}% you both are alright together")
else:
    print(f"Your love score is {love_score}%")
