def choose_optimal(n, m):
    return n if n<=m else n%(m+1) if n%(m+1)!=0 else 1

k = int(input("k : "))

bins = [[k]]
win = 0
total = 0
for _ in range(k):
    n, m = map(int, input("n and m :").split())
    total += n
    if n%(m+1) != 0:
        bins.append([n, m, True])
        win += 1
    else:
        bins.append([n, m, False])
print(bins, win)

turn = 'u'
index, no = 0, 0
while total>0:
    if turn == 'u':
        index, no = map(int, input("Enter index & no : ").split())
        while index<1 or index >k or no <=0 or no>bins[index][0] or no >bins[index][1]:
            index, no = map(int, input("Invalid Entry!Enter again : ").split())
            
        bins[index][0] -= no
        total -= no
        
        if bins[index][0] == 0:
            bins[0][0] -= 1
#         print([i[0] for i in bins[1:]])
        print(bins, win)
        if bins[0][0] == 0:
            print("User Won")
        turn = 'c'
    else:
#         User picked and now update true false and win count
        if bins[index][0]%(bins[index][1]+1) == 0:
            if bins[index][2] == True:
                win -= 1
            bins[index][2] = False
        else:
            if bins[index][2] == False:
                win += 1
            bins[index][2] = True
#         If win == n , Comp will win, So choose any thing, Doesn't matter
        if win == n or win == 0:
#             Choose any bin and pick
            for i in range(1, k+1):
                if bins[i][0]>0:
                    break
            t = choose_optimal(bins[i][0], bins[i][1])
            bins[i][0] -= t
            total -= t
            
            if bins[i][0] == 0:
                bins[0][0] -= 1

#         If win ==0, Comp will loose, So choose random same as before

#         Choose any win bin and pick
        else:
            for i in range(1, k+1):
                if bins[i][0]>0 and bins[i][2] == True:
                    break
            t = choose_optimal(bins[i][0], bins[i][1])
            bins[i][0] -= t
            total -= t
            
            if bins[i][0] == 0:
                bins[0][0] -= 1
        
#         print([i[0] for i in bins[1:]])
        print(bins, win)
        if bins[0][0] == 0:
            print("Comp Won")
        turn = 'u'
    
