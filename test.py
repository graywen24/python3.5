__author__ = 'wenwen'


the_word_is_flat=True
if the_word_is_flat:
    print("be careful not to fall off")
#else    print("test")

letter = ['a','b','c','d','e']
letter
print("letter length is ", len(letter))


square = ['0','1','2','3','4']
print(square[2])
square.append(5)
print("square value is",square)
print("square value is",square[5:])
#5

square.append(7**3)
print("the new square array is", square)
print("new square valuee 6 is", square[6:])

word = 'Python'
print(word[-6])
print(word[2:4])


a, b = 0, 1
while b<10:
    print(a,b)
    a,b=b, a+b




