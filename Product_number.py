# Product of set of real numbers
n = int(input("Enter the number of elements to be inserted:"))
prod = 1
for i in range(0,n):
  x = int(input("Enter the number"))
  prod = prod*x
print("Product of numbers =", prod)
