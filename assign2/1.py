# Logic : Whoever will have k(m+1) balls before his tern, he will loose.
# So computer tries to leave k(m+1) balls for the user always.
# If user leaves k(m+1) balls for Comp, then comp uses 1(could be anything) as this is a trap position.
# Complete invalid cases are not checked. We assume the constraint, user will input digits only as input

n, m = map(int, input("Enter n and m : ").split())
turn = 'u'
while n>0:
    if turn == 'u':
        t = int(input("User Enter the number : "))
        while t not in range(1, 1+min(m,n)):
            t = int(input("Invalid input! Enter again: "))
        
        n -= t
        print("Coins Left=",n, end = " ,")
        if n==0:
            print("NO")
        turn = 'c'
    else:
        t = n if n<=m else n%(m+1) if n%(m+1)!=0 else min(m,n)
        print("Computer chose", t, end = " ,")
        n -= t
        print("Left coins =",n)
        if n==0:
            print("YES")
        turn = 'u'
