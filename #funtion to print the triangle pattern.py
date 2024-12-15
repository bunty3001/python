#funtion to print the triangle pattern
def print_triangle(n):
    for i in range(1,n+1):
        #print leading spaces
        print(" "*(n-i),end=" ")

        #print increasing numbers
        for j in range(i,2*i):
            print(j,end=" ")

        #print decreasing numbers
        for j in range(2*i-2,i-1,-1):
            print(j,end=" ")

        #make to the next line
        print()

#Numbers of rows for thw pattern
n=5
print_triangle(n)
