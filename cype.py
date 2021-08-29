from os import system, name
import getpass
import os.path

#Clear Function
def clear():
    #Windows
    if name == 'nt':
        _ = system('cls')
    #Posix
    else:
        _ = system('clear')
    print("\n  .================.\n /                  \\\n*       CYPHER       *\n \\                  /\n  '================'\n")
    

#Main Menu
def menu(sf,key,l):
    clear()
    i=int(input("\n1) Add Credentials\n2) Show Credentials\n0) Exit\n\n-> "))
    #Credentional Adder
    if i==1:
        adder(sf,key,l)
    #Show Credentials
    elif i==2:
        looker(sf,key,l)
    #Quit Program
    elif i==0:
        clear()
        quit()
    #Loop Menu
    else:
        menu(sf,key,l)

#Check Authentication Method
def checklog(sf,key,tch,l):
    #Login Authenticator Key
    j=0
    check=''
    #Encrypt Login Key
    for d in tch:
        h=ord(d)+(int(key[j])*(int(key[j])+1))
        if h>126:
            h-=94
        check+=chr(h)
        j+=1
        if j==l:
            j=0
    #Check if Profile exists
    if os.path.isfile(sf):
        f = open(sf,'r')
        f.seek(0)
        c=f.readline()
        j=0
        m=''
        #Decrypt Profile Login Key
        for d in c:
            h=ord(d)-(int(key[j])*(int(key[j])+1))
            if h<32:
                h+=94
            m+=chr(h)
            j+=1
            if j==l:
                j=0
        f.close()
        #Verify Login
        if m[:-1]==tch:
            menu(sf,key,l)
        #Wrong Login
        else:
            clear()
            quit()
    #Create new user Profile
    else:
        f = open(sf,'w')
        f.write(check)
        f.write('\n')
        f.close()
        menu(sf,key,l)

#Add new Credentials to user Profile
def adder(sf,key,l):
    clear()
    j=0
    #Get New Credentials
    f = open(sf,'a')
    name = input("\nLogin: ")
    secret = getpass.getpass("Password: ")
    note = input("Note: ")
    tcrp=name+' : '+secret+' ('+note+')'
    c=''
    #Credential Encoder
    for d in tcrp:
        h=ord(d)+(int(key[j])*(int(key[j])+1))
        if h>126:
            h-=94
        c+=chr(h)
        j+=1
        if j==l:
            j=0
    c+='\n'
    #Save Credentials to File
    f.write(c)
    f.close()
    menu(sf,key,l)

#Look up the Profile Credentials
def looker(sf,key,l):
    clear()
    f = open(sf,'r')
    #Credentional Decoder
    for c in f:
        j=0
        m=''
        for d in c:
            h=ord(d)-(int(key[j])*(int(key[j])+1))
            if h<32:
                h+=94
            m+=chr(h)
            j+=1
            if j==l:
                j=0
        #Show Credential
        print(m[:-1])
    getpass.getpass('')
    f.close()
    menu(sf,key,l)


#Login Menu
def start():
    clear()
    #Get User Login Info
    usr = list(input("User: "))
    us=''.join(usr)
    pss = list(getpass.getpass("Password: "))
    ps=''.join(pss)
    keyl=[]
    
    #Profile Key Generation Process
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
    
    #Profile file location
    sf='./Profiles/.'+us+'.txt'
    tch=us+' : '+ps+' (Cypher)'

    checklog(sf,key,tch,l)

#Program Start
start()