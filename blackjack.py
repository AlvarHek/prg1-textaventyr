import random
A = "A"
kort = random.choice([2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,A,A,A,A,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
dkort1 = random.choice([2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
dkort2 = random.choice([2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
kort1 = random.choice([2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,A,A,A,A,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])

beslut = input("vill du spela jack black? ").lower()
if beslut=="ja":
    print("bra! du ska få två kort värt 2 - 10 eller ett A som är antingen värt 1 eller 11. Dealern kommer få 2 kort men du fårt bara se denna ena. målet är att få mer dealern men inte mer än 21 ")
else:
    exit("honungs puffar")
dtotal = dkort1 + dkort2
if kort == A:
    A = input(f"du fick A och {kort1} vill du att A ska vara värt 1 eller 11? ")
if A == "1":
    A = 1
    kort = A
elif A == "11":
    A = 11
    kort = A
if kort1 == A:
    A = input(f"du fick A och {kort} vill du att A ska vara värt 1 eller 11? ")
if A == "1":
    A = 1
    kort1 = A
elif A == "11":
    A = 11
    kort1 = A


while con =! "nej":
stotal = kort1 + kort
print(f"Du fick {stotal + kort} och dealern fick {dkort1} och ?.  ")


kort = random.choice([2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,A,A,A,A,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])

con = input("vill du dra mer kort, ja eller nej")


