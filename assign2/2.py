
import random

def bit_xor(split):
    res = 0
    for i in split:
        for j in i:
            res = res^j
    return res

def update_bin(bins, index, draw):
    bins[index][1] -= draw
    if bins[index][1] == 0:
        bins.pop(index)

def choose_random(bins):
    k = len(bins)-1
    index = random.randint(0,k)
    while(bins[index][1] == 0):
        index = random.randint(0,k)

    m, n = bins[index][0], bins[index][1]
    draw = random.randint(1, min(m, n))
    return index, draw

def optimal_draw(split, nim_sum):
    for i in range(len(split)):
        for j in range(len(split[i])):
            tmp = split[i][j]
            if (tmp^nim_sum) < tmp:

                comp_n = tmp - (tmp^nim_sum)
                return i, comp_n

def isvalid_input(bins, index, draw):
    k = len(bins)
    if index-1 not in range(0, k):
        print("Index out of range.", end = " ")
        return True

    m = bins[index-1][0]
    n = bins[index-1][1]
    if draw not in range(1, 1+min(m,n)):
       
        print("Can't draw these many.", end = " ")
        return True
    return False
       
def take_input(bins):
    k = int(input("k : "))
    total = 0
    for _ in range(k):
        n, m = map(int, input("n and m :").split())
        total += n
        bins.append([m, n])
    return total

def splitted_bins(bins):
    split = []
    for i in bins:
        m, n = i[0], i[1]
        tmp = [m] * (n//m)
        if n%m != 0:
            tmp.append(n%m) 
        split.append(tmp)
    return split

def random_inputs(bins):
    k = random.randint(2,20)
    total = 0
    for _ in range(k):
        n = random.randint(1, 200)
        k = random.randint(0, 3)
        m = random.randint(1, n) if k != 3 else random.randint(n+1, n+10)
        total += n
        bins.append([m, n])
    return total

def show(bins, total):
    print("Balls Left: ", total, end = " ,Bins(limit): ")
    for i in bins:
        print('{}({})'.format(i[1], i[0]), end = " ")

    print("\n")


def game():
    bins = []
    total = take_input(bins)
    # total = random_inputs(bins)
    show(bins, total)

    turn = 'u'

    while(total):

        if turn == 'u':
            index, draw = map(int, input("Enter your move user(index, draw) : ").split(" "))

            while isvalid_input(bins, index, draw):
                index, draw = map(int, input("Invalid Entry!!Enter your move user(index, draw) : ").split(" "))

            update_bin(bins, index-1, draw)
            print("\nUser removed", index, draw)
            total -= draw
            show(bins, total)

            # print(bins)
            turn = 'c'
        else:
            split = splitted_bins(bins)
            nim_sum = bit_xor(split)

            if nim_sum != 0:
                index, draw = optimal_draw(split, nim_sum)
                update_bin(bins, index, draw)
                print("\nComp removed", index+1, draw)

                total -= draw
                show(bins, total)
            else:
                index, draw = choose_random(bins)
                update_bin(bins, index, draw)
                print("\nComp removed", index+1, draw)

                total -= draw
                show(bins, total)
            # print(total, bins)
            turn = 'u'

    # Result
    if turn == 'u':
        print("\nYES")
    else:
        print("\nNOn")

game()