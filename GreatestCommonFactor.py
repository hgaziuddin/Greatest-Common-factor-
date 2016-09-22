print("Print the 1st number of the set of numbers you want to find the GCD ( or GCF) of.")
a = raw_input()
c = a
a = int(a)
print("Print the 2nd number of the set of numbers you want to find the GCD (or GCF) of.")
b = raw_input()
d = b
b = int(b)

while a != 0 and b != 0:

    rem = a % b
    a = b
    b = rem

a = str(a)
print("The GCD (or GCF) of " + c + " and " + d + " is " + a)
