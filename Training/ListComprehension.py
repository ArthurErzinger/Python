#LIST COMPREHENSION

#Array of Tuples
students = [
    ["Harry", 3.5, 3, True],
    ["Ron", 2.7, 2, True],
    ["Hermione", 3.9, 1, False],
    ["Dumbledore",2.9, 4, True],
    ["Snape", 3.1, 4, False],
]

#ANATOMY OF A LIST COMPREHENSION -> ["returned value" for "item" in "source list" if "condition"]

#GOAL: Get the name of every student
names = [student[0] for student in students]
print(names)

#GOAL: Get the lenght of the name of each student
name_length = [len(student[0]) for student in students]
print(name_length)

#GOAL: Get the name of every student who's in the 4th year  
fourth_years = [student[0] for student in students if student[2] == 4]
print(fourth_years)

#GOAL: Get the data type of each data piece in "students" (NESTED LIST COMPREHENSIONS)
data_type = [[type(item) for item in student] for student in students]
print(data_type)

#GOAL: Get the square of each even intenger between 2 and 10
print([i**2 for i in range(2, 11, 2)])

#Exercises (https://bbookman.github.io/Python-list-comprehension1/)

#GOAL: Get all numbers divisible by 7 between 1 and 1000
print([i for i in range (0, 1001) if i % 7 == 0])

#GOAL: Get all number that have 3 in them between 1 and 1000
print([number for number in range(0, 1001) if "3" in str(number)])

#GOAL: Count the number of whitespaces in a string
string = 'Salve o corinthians, o campeão dos campeões, eternamente dentro dos nossos corações'
spaces = [s for s in string if s == " "]
print(len(spaces))

#GOAL: Create a list of all the consonants,
#in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
stri = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
print([letter for letter in stri if letter not in('a,e,i,o,u," "')])

#GOAL: Get the index and the value as a tuple,
#for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)


#GOAL: Find common numbers in 2 lists
listA = [1, 2, 3, 4]
listB = [2, 3, 4, 5]
print([number for number in listA if number in listB])

#GOAL: Get only the numbers in the sentence
sentence =  'In 1984 there were 13 instances of a protest with over 1000 people attending'
print([number for number in sentence if number.isdigit() == True ])

#GOAL: Given numbers = range(20), produce a list containing the word ‘even’ if a number,
#in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’



#GOAL: Produce a list of tuples consisting of only the matching numbers,
#in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)]
lista = 1, 2, 3,4,5,6,7,8,9
listb = 2, 7, 1, 12
print([(number, number) for number in lista if number in listb])

#GOAL: Find all of the words in a string that are less than 4 letters
print([word for word in string.split() if len(word) < 4])

#GOAL: Use a nested list comprehension to find all,
#of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
x = range(2,10)
print([number for number in range(0, 1001) if number % x == 0])