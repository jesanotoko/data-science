my_list = [1,2,3]
my_list.append(4)
print(my_list)



my_list = [5,6,7]
another_list = [12,3,4]
my_list.extend(another_list)
print(my_list)



my_list = [1,2,3]
a_tuple = (6,7,8)
my_list.extend(a_tuple)
print(my_list) # output : [1,2,3,6,7,8]



my_list = [1,2,3]
a_string = "hello"
my_list.extend(a_string)
print(my_list) # output : [1,2,3,'h','e','l','l','o']



my_list = [1,2,3,4]
my_list.insert(0,'start')
print(my_list)   # output : ['start',1,2,3,4]



my_list = [1,2,3,4]
my_list.insert(len(my_list),'end')
print(my_list) # output : [1,2,3,4,'end']



my_list = [1,2,3,4]
elements_to_insert = ['a','b','c']
# Inserting elements at specific indices using a loop
for index, element in enumerate(elements_to_insert, start=2):
    my_list.insert(index,element)
print(my_list)   # output : [1,2,'a','b','c',3,4]



my_list = [1,2,3,4]
element_to_insert = ['x','y','z']
# Inserting elelments in reverse order using negative indices
for index, element in enumerate(reversed(element_to_insert), start =1):
    my_list.insert(index,element)
print(my_list)   # output : [1,'z','y','x',2,3,4]



my_list = [1,2,3,4,2]
my_list.remove(2)
print(my_list)  # output : [1,3,4,2]  This will be remove first occurance from the list 'my_list'



fruits = ['apple','banana','orange','banana']
fruits.remove('banana')
print(fruits)   #ouput : ['apple','orange','banana']



my_list = [1,2,3,4,5]
removed_element = my_list.pop(2)  #index no 2
print(removed_element) # 3
print(my_list) # [1,2,4,5]


numbers = [10,20,30,40,50]
last_number = numbers.pop() 
print(last_number) # 50
print(numbers) # [10,20,30,40]



colors = ['red','blue','green','yellow']
last_color = colors.pop()
print(last_color) # yellow
print(colors) # ['red','blue','green']



numbers = [1,2,3,4,5]
numbers.clear()
print(numbers)  # output : []



my_list = ['apple','banana','orange','banana']
index = my_list.index('banana')
print(index)  # output : 1 (index of the first occurance of 'banana')



numbers = [10,20,30,40,30,50]
index = numbers.index(30,3,5)
print(index)  # output : 4 (index of the first occurance of '30' between index 2 and 5)



letters = ['a','b','c']
try:
    index = letters.index('d')
    print(index)
except ValueError:
    print("Element 'd' is not it the list")



numbers = [1,3,5,7,9]
try:
    index = numbers.index(4) # 4 is not present in the list
    print(index) # This line won't be executed as valueError will be raised
except ValueError:
    print("Element not found in the list.") # this is output



my_list = [1,2,2,3,2,4,6]
count_of_two = my_list.count(2)
print(count_of_two) # output : 3 (number of occurances of '2' in the list)



numbers = [3,2,8,1,6]
numbers.sort()
print(numbers)  # output : [1,2,3,6,8]



fruits = ['apple','banana','orange','grape']
fruits.sort(reverse=True)
print(fruits) # output : ['orange','grape','banana','apple']



data = [('John',28),('Alice',23),('Bob',30)]
data.sort(key=lambda x: x[1]) #sort based on the second element of each tuple
print(data) # output : [('Alice',23),('John',28),('Bob',30)]



students = [
    {'name': 'Alice', 'scores':[90,85,88]},
    {'name': 'Bob', 'scores':[75,80,92]},
    {'name': 'Charlie','scores':[88,92,78]},
    {'name': 'David', 'scores' : [85,90,85]}
]

# Sort the student based on their average score

students.sort(key=lambda student: sum(student['scores'])/len(student['scores']),reverse = True)

# Print the sorted list of students
# for student in students:
#     print(f"name: {student['name']},Average Score: {sum(student['scores'])/len(student['scores'])}")



class student:
    def __init__(self,named,aged,graded):
        self.named = named
        self.aged = aged
        self.graded = graded

    def __repr__(self):
        return f"named: {self.named}, aged: {self.aged}, Graded: {self.graded}"
    
# Creating instance of the student class

students = [
    student('Alice',20,80),
    student('Bob',18,92),
    student('charlie',21,85),
    student('David',19,88)
]

# Sorting the list of students based on the grade and age
students.sort(key=lambda x: (x.graded, x.aged))

# Printing the sorted list of students
for student in students:
    print(student)



class book:
    def __init__(self,title,author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"
    
# Creating instances of the book class

books = [
    book('Python Crash course','Eric Matthes',2015),
    book('Deep Learning','Ian Goodfellow', 2016),
    book('The Alchemist','Paulo Coelho',1988),
    book('Design Patterns','Erich Gamma',1994)
]

# Sort the list of books by publication year in descending order
books.sort(key=lambda x: x.publication_year,reverse=True)

# Printing the sorted list of book
for book in books:
    print(book)




my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list)



original_list = [1,2,3,4,5]
copied_list = original_list.copy()
print(copied_list)




# Original list with nested lists
original_nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# Creating a shallow copy of the original list
copied_nested_list = original_nested_list.copy()
# Modifying an inner list in the copied list
copied_nested_list[0][0] = 10
# Displaying both original and copied list
print("Original nested list:", original_nested_list)
print("Copied nested list:",copied_nested_list)



# Initalizing an empty list as a queue
queu = []

#Enqueueing elements to the queue
queu.append('Apple')
queu.append('Orange')
queu.append('Banana')
print("Initial Queue: ",queu)

# Dequeueing elements from the queue
removed_item = queu.pop(0)
print("Remove item:", removed_item)
print("Updated Queue:",queu)  



squares = [x**2 for x in range(10)]
print(squares) #output : [0,1,4,9,16,25,36,49,81]



even_numbers = [x for x in range(10) if x % 2 ==0]
print(even_numbers) # output : [0,2,4,6,8]



even_odd_pairs = [(x,x+1) for x in range(0,10,2)]
print(even_odd_pairs) # output : [(0,1),(2,3),(4,5),(6,7),(8,9)]



text = "This is a sample text within some words."
words = text.split()
long_words = [word for word in words if len(word) > 3]
print(long_words) 



matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [element for row in matrix for element in row]
print(flattened) 



# Function to check if a number is prime
def is_pirme(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True



# Generating a list of prime numbers from 2 to 100 using list comprehension
prime_numbers = [x for x in range(2,101) if is_pirme(x)]

print(prime_numbers)



# Generating a 3*3 matrix with nested list comprehension
matrix = [[j for j in range(3)] for i in range (3)]
print(matrix)

 

my_list = [1,2,3,4,5]
del my_list[2]  # Remove the item at index 2(value: 3)
print(my_list)



my_list = [1,2,3,4,5]
del my_list[1:3] # Remove elements from index 1 to index 2 (excluding index 3)
print(my_list)


my_dict = {'a': 1, 'b':2,'c':3}
del my_dict['b'] # Removes the key 'b' and its associated value from the dictionary
print(my_dict)



# Creating a set
my_set = {1,2,3,4}
print(my_set) # output : {1,2,3,4}
# Adding elements to a set 
my_set.add(5)
print(my_set) # output : {1,2,3,4,5}
# Removing elements form a set
my_set.remove(3)
print(my_set) # output : {1,2,4,5}



# Creating Sets
set_a = {1,2,3,4,5}
set_b = {3,4,5,6,7}

# Union of sets (combining unique elements from both sets)
Union_set = set_a | set_b  #Alternatively: union_set = set_a.union(set_b)
print("Union:",Union_set) # output : {1,2,3,4,5,6,7}

#Intersection of sets (common elements in both sets)
intersection_set = set_a & set_b # Alternatively : intersection_set = set_a.intersection(set_b)

# Difference between sets (elements in set_a but not in set_b)
difference_set = set_a - set_b # Alternatively : difference_set = set_a.difference(set_b)
print("Difference(set_a - set_b):", difference_set)

# Symmetric difference (elements present in either set, but not in both)
symmetric_differnece_set  = set_a ^ set_b #Alternatively: symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_differnece_set)

# Checking for subset and superset
subset_check = {1,2}.issubset(set_a) #  Checking if {1,2} is a subset of set_a
print("{1,2} is a subset of set_a:",subset_check) # Output : True

superset_check = set_a.issuperset({1,2}) # Checking if set_a is a superset of {1,2}
print("set_a is a superset of {1,2}:",superset_check)



# Student involved in various extracurricular activities
football_club = {'Alice','Bob','Charlie','David','Eva'}
chese_club = {'Alice','Frank','David','Grace','Helen'}

# Student involved in both football and chess clubs(Intersection)
both_clubs = football_club & chese_club
print("Student involved in both clubs:", both_clubs)

#Students unique to each club(Symmtric Difference)
unique_to_football = football_club - chese_club
unique_to_chese = chese_club - football_club
print("Student unique to football club:", unique_to_football)
print("Students unique to chese club:",unique_to_chese)

#Students involved in at least one club(union)
involved_in_any_club = football_club | chese_club
print("Student involved in at least one club:",involved_in_any_club)



# Creating a dictionary
my_dict = {'name':'Alice','age':25,'city':'New York'}

# Accessing values using keys
print(my_dict['name']) # Output : 'Alice'
print(my_dict['age']) # Output : 25

#Adding a new key-value pair
my_dict['email'] = 'alice@example.com'
print(my_dict) # output : {'name':'Alice','age':25,'city':'New York','email':'alice@gmail.com'}

#Modifying a value
my_dict['age'] = 26
print(my_dict)

# Removing a key-value pair
del my_dict['city']
print(my_dict)



# Dictionary representing student information
students = {
    'Alice':{
        'age':20,
        'subjects':{
            'Math': 85,
            'physics': 90,
            'Englilsh': 78
        }
    },
    'Bob':{
        'age': 18,
        'subjects':{
            'Math': 92,
            'physics': 88,
            'English':85
        }
    },
    'Charlie':{
        'age': 21,
        'subjects': {
            'Math': 78,
            'Physics': 80,
            'English': 75
        }
    }
}
# Accessing specific information
print("Alice's age:",students['Alice']['age'])
print("Bob's Physics grade:", students['Bob']['subjects']['physics'])

# Calculating average grades for each student
for student, info in students.items():
    grades= info['subjects'].values()
    average_grade = sum(grades)/len(grades)
    print(f"{student}'s average grade:", round(average_grade,2))