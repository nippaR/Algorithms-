# Insertion Sort Algorithm
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

# Selection Sort Algorithm
def selectionSort(B):
    n = len(B)
    for z in range (n-1):
        smallest = z
        for a in range(z+1, n):
            if B[a] < B[smallest]:
                smallest = a
        B[z], B[smallest] = B[smallest], B[z]

B = [64, 25, 12, 22, 11]
print(B)
selectionSort(B)
print(B)
    
A = []

#Function to find the range of the marks
def findRange(A):
   range = A[-1] - A[0]

   return range

#Function to find the average of the marks
def findAverage(A):
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
    avg = sum / len(A)
    return avg

#Get the marks from the user
for i in range(1, 10):
    A.append(int(input(f"Enter Your Mark {i}:")))


#Median Calculation
def findMedian(A):
    n = len(A)
    if n % 2 == 0:
        median1 = A[n//2]
        median2 = A[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = A[n//2]
    return median

insertionSort(A)
print (A)

print("Range Is : ",findRange(A))

print("Average Is : ",findAverage(A))

print("Median Is : ",findMedian(A))




#BUBBLE SORT ALGORITHS

def bubbleSort(B):
    for i in range (len(B)):
        for j in range (i+1, len(B)):
            if B[i] > B[j]:
                B[i],B[j] = B[j],B[i]

B = []

for a in range (1 , 9):
    B.append(int(input(f"Enter your input no.{a}: ")))

print("Befor Sorting: ",B)

bubbleSort(B)

print("After Sorting:",B)







