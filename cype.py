import getpass

print("\n  .================.\n /                  \\\n*       CYPHER       *\n \\                  /\n  '================'\n")

usr = list(input("User: "))
pss = list(getpass.getpass("Password: "))

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

sf='./.safe.txt'

i=-1
while i!=0:
    i=int(input("\n1) Add Credentials\n2) Show Credentials\n0) Exit\n\n-> "))
    if i==1:
        j=0
        f = open(sf,'a')
        name = input("\nName: ")
        secret = input("Pass: ")
        note = input("Note: ")
        tcrp=name+':'+secret+' ('+note+')'
        c=''
        for d in tcrp:
            h=ord(d)+int(key[j])
            if h>126:
                h-=94
            c+=chr(h)
            j+=1
            if j==l:
                j=0
        f.write(c)
        f.write('\n')
        f.close()
    
    elif i==2:
        f = open(sf,'a+')
        f.seek(0)
        j=0
        for c in f:
            m=''
            for d in c:
                h=ord(d)-int(key[j])
                if h<32:
                    h+=94
                m+=chr(h)
                j+=1
                if j==l:
                    j=0
            print(m)
        f.close()
