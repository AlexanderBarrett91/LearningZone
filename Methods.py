#defining vlaues
def Values():
  return '!', '@', '#', '$','%','^'
a,b,c,d,e,f = Values()
#printing using spaces 1
print('1_'* 40)
###################################

print((10 * '1')+(' 0 ')+(10 * '1'))
print((9 * '1')+('  0  ')+(9 * '1'))
print((8 * '1')+('   0   ')+(8 * '1'))
print((7 * '1')+('    0    ')+(7 * '1'))
print((6 * '1')+('     0     ')+(6 * '1'))
print((5 * '1')+('      0      ')+(5 * '1'))
print((4 * '1')+('       0       ')+(4 * '1'))
print((3 * '1')+('        0        ')+(3 * '1'))
print((2 * '1')+('         0         ')+(2 * '1'))
print((1 * '1')+('          0          ')+(1 * '1'))
print((2 * '1')+('         0         ')+(2 * '1'))
print((3 * '1')+('        0        ')+(3 * '1'))
print((4 * '1')+('       0       ')+(4* '1'))
print((5 * '1')+('      0      ')+(5 * '1'))
print((6 * '1')+('     0     ')+(6 * '1'))
print((7 * '1')+('    0    ')+(7 * '1'))
print((8 * '1')+('   0   ')+(8 * '1'))
print((9 * '1')+('  0  ')+(9 * '1'))
print((10 * '1')+(' 0 ')+(10 * '1'))

#printing inline statements
print('2_'* 40)
###################################

print(a * 23)
print(a * 10,b,a * 10)
print(a * 8,c,b,c, a * 8)
print(a * 7,c * 2,b,c *2, a * 7)
print(a * 6,c * 3,b,c *3, a * 6)
print(a * 5,c * 4,b,c *4, a * 5)
print(a * 4,c * 5,b,c *5, a * 4)
print(a * 3,c * 6,b,c *6, a * 3)
print(a * 2,c * 7,b,c *7, a * 2)
print(a,c * 8,b,c *8, a)
print(a * 2,c * 7,b,c *7, a * 2)
print(a * 3,c * 6,b,c *6, a * 3)
print(a * 4,c * 5,b,c *5, a * 4)
print(a * 5,c * 4,b,c *4, a * 5)
print(a * 6,c * 3,b,c *3, a * 6)
print(a * 7,c * 2,b,c *2, a * 7)
print(a * 8,c * 1,b,c *1, a * 8)
print(a * 10,b,a * 10)
print(a * 23)

#print without a new line end='' 3
print('3_'* 40)
###################################
alist = [12,11,10,9,8,7,6,5,4,3,2]


for i in alist:
        print(a*i, end=b),
        print(c)

#while loop test low to high
print('4_'*40)
###################################
counter = 1
while counter < 12:
        print(b*counter)
        counter = counter + 1

#inverse counter using negatives in while loops high to low
print('5_'*40)
###################################
counter = 12
while counter > 0:
        print(c*counter)
        counter = counter -1

# for loop using a range to accomplis the same thing high to low
print('6_'*40)
##################################
for y in range(12,0,-1):
    for x in range(y):
        print(d, end="")
    print()

# this is the inverse of 6
print('7_'*40)
###################################
for x in range(0,12,+1):
    for y in range(x):
        print(e, end="")
    print()
