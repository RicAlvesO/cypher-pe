import getpass
import os.path

print("\n  .================.\n /                  \\\n*       CYPHER       *\n \\                  /\n  '================'\n")

usr = list(input("User: "))
us=''.join(usr)
pss = list(getpass.getpass("Password: "))
ps=''.join(pss)
keyl=[]

while True:
    try:
        keyl.append(usr.pop(0))
        keyl.append(pss.pop(0))
    except IndexError:
        if len(usr)>0:
            keyl.append(usr.pop(0))
        elif len(pss)>0:
            keyl.append(pss.pop(0))
        else:
            break

key=''.join(keyl)
key=''.join(str(ord(c)) for c in key)
l=len(key)

sf='./Profiles/.'+us+'.txt'

tch=us+' : '+ps+' (Cypher)'
j=0
check=''
for d in tch:
    h=ord(d)+(int(key[j])*(int(key[j])-1))
    if h>126:
        h-=94
    check+=chr(h)
    j+=1
    if j==l:
        j=0

if os.path.isfile(sf):
    f = open(sf,'r')
    f.seek(0)
    c=f.readline()
    j=0
    m=''
    for d in c:
        h=ord(d)-(int(key[j])*(int(key[j])-1))
        if h<32:
            h+=94
        m+=chr(h)
        j+=1
        if j==l:
            j=0
    f.close()
    if m[:-1]!=tch:
        quit()
else:
    f = open(sf,'w')
    f.write(check)
    f.write('\n')
    f.close()


i=-1
while i!=0:
    i=int(input("\n1) Add Credentials\n2) Show Credentials\n0) Exit\n\n-> "))
    if i==1:
        j=0
        f = open(sf,'a')
        name = input("\nLogin: ")
        secret = getpass.getpass("Password: ")
        note = input("Note: ")
        tcrp=name+' : '+secret+' ('+note+')'
        c=''
        for d in tcrp:
            h=ord(d)+(int(key[j])*(int(key[j])-1))
            if h>126:
                h-=94
            c+=chr(h)
            j+=1
            if j==l:
                j=0
        c+='\n'
        f.write(c)
        f.close()
    
    elif i==2:
        f = open(sf,'r')
        for c in f:
            j=0
            m=''
            for d in c:
                h=ord(d)-(int(key[j])*(int(key[j])-1))
                if h<32:
                    h+=94
                m+=chr(h)
                j+=1
                if j==l:
                    j=0
            print(m[:-1])
        f.close()
