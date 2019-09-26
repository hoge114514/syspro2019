

def check(p):
    for i in range(2,p):
        if(p%i==0):
            return
    return True

def main():
    pn = 10000
    while(1):
        pn += 1
        if(check(pn)==True):
            print(pn)

if __name__ == '__main__':
    main()
