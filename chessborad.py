# count = 0
# for i in range(1,9):
#     for j in range(1,9):
#         if (i+j)%2==0:
#             print("W",end=' ')
#         else:
#             print("B",end=' ')
#     print()

# W B W B W B W B 
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,7):
#     for j in range(1,6-i+2):
#         print("*",end=" ")
#     print()

# o/p:
# * * * * * * 
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,5-i+2):
#         print("*",end=" ")

#     print()

#     * * * * * 
#       * * * *
#         * * *
#           * *
#             *

# N=5 
# for i in range(1,N+1):
#     for j in range(1,N-i+1):
#         print(" ", end=" ")
#     for j in range(1,i+1):
#         print("*", end=" ")

#     print()

#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

# N=5

# for i in range(1,N+1):
#     for j in range(1,N-i+1):
#         print(" ", end=" ")
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print()
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# N=5
# for i in range(1,N+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,2*(N-i)+2):
#         print("*",end=" ")
#     print()

# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# N=5
# for i in range(N):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,N):
#     for j in range(i,N):
#         print("*",end=" ")

#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# def Diamond(n):
#     count = 1
#     for i in range(1,n+1):
#         for j in range(1,(n-i)+1):
#             print(end=" ")

#         while count!= (i+1):
#             print("*",end=" ")
#             count = count + 1
#         count=1
#         print()
#     k=0
#     count=0
#     for i in range(1,n+1):
#         for j in range(1,k+1):
#             print(end=" ")
#         k=k+1
#         while count <= (n - i):
#             print("*", end = " ")
#             count = count + 1
#         count = 0
#         print()

# n = 5
# Diamond(n)

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# Function to display alphabet pattern
# def display(n):

#     # Outer for loop for number of lines
#     for i in range(n):

#         # Inner for loop for logic execution
#         for j in range((n // 2) + 1):

#             # prints two column lines
#             if ((j == 0 or j == n // 2) and i != 0 or

#                 # print first line of alphabet
#                 i == 0 and j != 0 and j != n // 2 or

#                 # prints middle line
#                 i == n // 2):
#                 print("*", end = "")
#             else:
#                 print(" ", end = "")
        
#         print()
    

# # Driver Function
# display(7)
#  ** 
# *  *
# *  *
# ****
# *  *
# *  *
# *  *

# Function for hollow square
# def hollowSquare(rows):

#     for i in range(1, rows + 1):
        
#         # Print stars for each solid rows
#         if (i == 1 or i == rows):
#             for j in range(1, rows + 1):
#                 print("*", end = "")

#         # stars for hollow rows
#         else:
#             for j in range(1, rows + 1):
#                 if (j == 1 or j == rows):
#                     print("*", end = "")
#                 else:
#                     print(end = " ")

#         # Move to the next line/row
#         print()

# # Function for Solid square
# def solidSquare(rows):

#     for i in range(1, rows):
        
#         # Print stars after spaces
#         for j in range(1, rows + 1):
#             print("*", end = "")

#         # Move to the next line/row
#         print()

# # Utility program to print all patterns
# def printPattern(rows):

#     print("Solid Square:")
#     solidSquare(rows)
    
#     print("\nHollow Square:") 
#     hollowSquare(rows)

# # Driver Code
# rows = 5
# printPattern (rows)

# Solid Square:
# *****
# *****
# *****
# *****

# Hollow Square:
# *****
# *   *
# *   *
# *   *
# *****



# def pattern(rows):
#     for i in range(rows):
#         # Print leading spaces
#         print("  " * i, end="")
        
#         # Print decreasing stars
#         for j in range(2 * (rows - i) - 1):
#             print("*", end=" ")
        
#         print()  # New line

# rows=5
# pattern(rows)

# rows = 5
# cols = 4

# for i in range(rows):
#     for j in range(cols):
#         print("*", end="  ")
#     print()

# n=5
# for i in range(n-1):

#     for j in range(i,n):
#         print(" ",end=" ")

#     for j in range(i):
#         print("*",end=" ")

#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):

#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
   
#     print()

# n=5
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i+1,n):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")    
#     for j in range(i+1):
#         print("*",end=" ")
    
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if(i==0 or j==0 or i==n-1 or j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n=5
for i in range(n):
    for j in range(i,n):
        if(i==0 or j==n-1  or i==j or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

