
def drill(a):
    drill=[]
    c=0
    for i in range(0,a):
        number=int(input('enter your numbers:-'))
        drill.append(number)
    print(drill)
    for i in drill:
        c=c+i
    print(c)

def activate_drill():
    a=int(input('enter thr total number for the drill:-'))
    drill(a)

activate_drill()
