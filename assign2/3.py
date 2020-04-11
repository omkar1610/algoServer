arr = list(map(int, input("Enter Array : ").split()))
n = len(arr) 
LIS = [1 for i in range(n)] 
length = 0

# Find Longest Increasing Subseq and done 
for i in range(1, n): 
    for j in range(i): 
        if (arr[i]>arr[j] and (i-j)<=(arr[i]-arr[j]) ): 
            LIS[i] = max(LIS[i], LIS[j] + 1) 
            
    length = max(length, LIS[i])
print(n - length)