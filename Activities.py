def insertionSort(A):
	for j in range(0, len(A)):
		key = A[j]
		i = j-1
		while i > 0 and A[i] > key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key 


# A = []

# for i in range(0, 10):
#     A.append(int(input(f"Enter the your integer no.{i} : ")))

# print(A)

# insertionSort(A)

# print(A)


# def floatInsertionSort(A):
# 	for j in range(0, len(A)):
# 		key = A[j]
# 		i = j-1
# 		while i >=0 and A[i] < key:
# 			A[i+1] = A[i]
# 			i = i-1
# 		A[i+1] = key 

# A = []

# for i in range(0,5):
# 	A.append(float(input("Enter your Float number")))

# print(A)

# floatInsertionSort(A)

# print(A)def selectingSort(A):



# def selectingSort(A):
# 	n = len(A)
# 	for j in range(n-1):
# 		smallest = j
# 		for i in range(j+1, n):
# 			if A[i] < A[smallest]:
# 				smallest = i
# 		A[j], A[smallest] = A[smallest], A[j]  # Swap the elements

# A = []

# for i in range(1, 8):
# 	n = (input("Enter your value: "))
# 	# if n >= 0:
# 	A.append(n)
# 	# else:
# 	# 	print("Enter the positive integers numbers only")
# 	# 	break
# print(A)

# selectingSort(A)

# print(A)


# def selectingSort(A):
# 	n = len(A)
# 	for j in range(n-1):
# 		smallest = j
# 		for i in range(j+1 , len(A)):
# 			if A[i] < A[smallest]:
# 				smallest = i
# 		A[j],A[smallest] = A[smallest],A[j]


# A = []

# for i in range(0, 5):
# 	n = (input("Enter your value here: "))
# 	A.append(n)

# print(A)

# selectingSort(A)

# print(A)


# def bubbleSort(S):
# 	for i in range(len(S)):
# 		for j in range (i+1, len(S)):
# 			if S[i] > S[j]:
# 				S[i], S[j] = S[j],S[i]
# def total(S):
# 	tot = 0 
# 	for x in range(0,len(S)):
# 		tot += S[x]
# 	return tot
		

	
# S = []

# for i in range(1,9):
# 	S.append(int(input(f"Enter the integers no.{i}: ")))


# print (S)

# bubbleSort(S)

# print(S)

# print("Total count of this list is : ",total(S))
# Function to perform Insertion Sort on the list of cubed values
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Step 1: Input a list of 6 integers
numbers = []
for i in range(6):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Step 2: Calculate the cube of each integer
cubed_values = [num ** 3 for num in numbers]

# Step 3: Sort the cubed values using Insertion Sort
insertion_sort(cubed_values)

# Step 4: Print the sorted list of cubed values
print("Sorted list of cubed values:", cubed_values)



