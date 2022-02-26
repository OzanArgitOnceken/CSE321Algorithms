class lessons:
        def __init__(self,name,s,f):
            self.name=name
            self.s=s
            self.f=f
        def __lt__(self,other):
            return self.f<=other.f
def greedy(n,s,f):
    les=[]
    for i in range(len(f)):
        les.append(lessons(n[i],s[i],f[i]))
    les.sort(reverse=False)
    names=[]
    names.append(les[0].name)
    j=0
    for i in range(len(les)):
        if les[i].s>=les[j].f:
            names.append(les[i].name)
            j=i
    return names

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
n=["English","Mathematics","Physics","Chemistry","Biology","Geography"]
names=greedy(n,s,f)
print(names)