import string 
ascii_letter = string.ascii_letters
print(ascii_letter) # all alphabet small and big character (abc etc, ABC etc)



lowercase_letters = string.ascii_lowercase
print(lowercase_letters) # all lowercase letter



uppercase_letter = string.ascii_uppercase
print(uppercase_letter)  # all uppercase letter



numeric_digits = string.digits
print(numeric_digits) # output : 0123456789



hexadecimal_digits = string.hexdigits
print(hexadecimal_digits) # output : 0123456789abcdefABCDEF 



octal_digits = string.octdigits
print(octal_digits) # 01234567



punctuation_symbols = string.punctuation
print(punctuation_symbols) # all punctuation character



printable_chars = string.printable
print(printable_chars)  # all ASCII Value character



whitespace_chars = string.whitespace
# print(whitespace_chars)   output : \t\n\r\x0b\x0c



formatter = string.Formatter()
formatted_string = formatter.format("Hello, {name}! It's {time}.", name = "Alice" , time = "morning")
print(formatted_string)



#using positional arguments
result = formatter.format("Hello, {}! Today is {}.","Alice","Monday")
print(result)



formatter = string.Formatter()
result_named = formatter.format("Hello, {name}! It's {day}", name = "bob", day = "Tuesday")
print(result_named)



format_string = string.Formatter()
format_string = "Today is {} and the temparature is {} degrees. "
result = format_string.format("Monday",25)
print(result)



name = "Alice"
age = 30
greeting = "Hello, {}! You are {} years old.".format(name,age)
print(greeting)



name = "Bob"
city = "New York"
message = f"Welcome to {city},{name}!"
print(message)



price = 123.4567
formatted_price = "The price is ${:.2f}".format(price)
print(formatted_price) 



name = "John"
score = 95
result = f"{name:^10} scored {score:>3} points."
print(result)



from datetime import datetime
current_date  = datetime.now()
formatted_date = f"Today's date is: {current_date:%A,%B,%d,%Y}"
print(formatted_date)



percentage = 0.82345
formatted_percentage = f"Percentage: {percentage:.4%}"
print(formatted_percentage)



def format_greeting(name,age):
    greeting = "Hello, {}! You are {} years old.".format(name,age)
    return greeting
# Calling the function using positional arguments
formatted_greeting_pos = format_greeting("Alice",30)
print(formatted_greeting_pos)
# Calling the function using keyword arguments
formatted_greeting_kw = format_greeting(age = 30, name = "Bob")
print(formatted_greeting_kw)



text = "hello world"
capitalized_text = text.capitalize() #first word capital
print(capitalized_text)



text = "Hello World!"
casefolded_text = text.casefold() # all letter small similar to str.lower() function
print(casefolded_text)



text = "Hello"
centered_text = text.center(20,'*')
print(centered_text)  # hello is within a width of 20 character and (*) works like a padding



#counting all occurrances of 'a' in the string
string = "banana"
count = string.count('a')
print(count)  # output : 3
#Counting occurrences of 'b' from index 2
count = string.count('b',2)
print(count) # output 0
#Counting occurrances of 'na' up to index 6
count = string.count('na',0,6)
print(count)



text = "This is a simple sentence."
check_end = text.endswith('sentence.')
print(check_end) # output True



text = "Hello World!"
#check if the string ends with 'world!' starting from index 7
check_end = text.endswith('World!',6)
print(check_end) # true
s = text.index('W')
print(s)
#check if the string ends with 'Hello' in a specific range
check_end3= text.endswith('Hello',0,5) # true
print(check_end3)



text = "This is a sample text for find method."
#Find the index of 'sample'
index_sample = text.find('sample')
print(index_sample) # output will be 10
#Find the index of 'text' starting from index 15
index_text = text.find('text',15)
print(index_text)  # output wil 17
#Find the index of 'method' in a specific rangtext
index_range = text.find('method',25,30)
print(index_range) # output : -1



data = {'name' : 'Alice' , 'age' : 30}
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_string)


# Find the index of 'method' in a specific range
text= "this is a sample text for index method." #
index_method = text.index('index') # 26= first index and 32 = last index)
print(index_method) # 26



text1 = "Hello123"
text2 = "Hello 123"
text3 = "Special_characters!"

print(text1.isalnum()) # Output : true (All character are alphahumeric)
print(text2.isalnum()) # output : flase (Contain space)
print(text3.isalnum()) # output : false (contain special characters)



text1 = "Hello"
text2 = "Hello123"
text3 = "123"

print(text1.isalpha()) # output : True (all chracter are alphabetic)
print(text2.isalpha()) # output : False (contain digit)
print(text3.isalpha()) # output : flase (contain digit)



text1 = "Hello123"
text2 = "specila_char\!4rej;op[|]"
print(text1.isascii(), text2.isascii()) # output  both true ; 0-127 is ascii character other string is not ascii character



text1 = "12345"
text2 = "12.34"
text3 = "IV"
text4 = "agd"
print(text1.isdecimal()) # outpt: True (All character are decimal)
print(text2.isdecimal()) # output: False (contain a period)
print(text3.isdecimal()) # output: False (Roman numeral isn't a decimal digit)



text1 = "12345"
text2 = "12.22"
print(text1.isdigit) # output : True (All character are digit)
print(text2.isdigit()) # output : False(contain a period) same as isnumeric() function



# `str.isidentifer()` 1. It must start with either a letter ('a-z', 'A-Z') or an underscore('_')
# 2. the remaining chareacter can be letters underscores or digits('0-9')
text1 = "variable"
text2 = "123variable"
text3 = "_varialble"

print(text1.isidentifier())  # output : True
print(text2.isidentifier())   # output : False(starts with a digit)
print(text3.isidentifier()) # output : True



text1 = "hello"
text2 = "Hello"
text3 = "hello123"
print(text1.islower()) # output : True (all character are lowercase)
print(text2.islower()) # output : False (contain uppercase character)
print(text3.islower()) # output : True (All alphabetic character are lowercase)




text1 = "Hello, World"
text2 = "Hello\nWorld"
print(text1.isprintable()) # output : True (all character are printable)
print(text2.isprintable()) # output : False (contain a non-printable character - newline)



text1 = "  "
text2 = " Hello "
text3 = "\n\t\r"
print(text1.isspace()) # output : True (All character are whitespace)
print(text2.isspace()) # output : False (contains non whitespace chracter)
print(text3.isspace()) # output : true (all character are whitespace)



text1 = "Hello World"
text2 = "Hello world"
text3 = "Hello world 123"
text4 = "Hello"
text5 = "HELLO"
print(text1.istitle()) # output : True (each word start with an uppercase character)
print(text2.istitle()) # output : False (second word start with lowercase)
print(text3.istitle()) # output : False (contains digits)
print(text4.istitle()) # output : True (single word start with uppercase)
print(text5.istitle()) # outpt : False (all uppercase_)



text1 = "HELLO"
text2 = "hello"
text3 = "12345"
print(text1.isupper()) # output : True (all chracter are uppercase)
print(text2.isupper()) # output : False (contains lowercase characters)
print(text3.isupper()) # output : False (no alphabetic characters)



numbers = [1,2,3,4,5]
result = "-".join(map(str,numbers))
print(result)



mixed_tuple = ('apple',123, True, 'banana')
result = ",".join(map(str,mixed_tuple))
print(result)



text = "Hello"
padded_text = text.ljust(10,'*')
print(padded_text)  # output : "Hello*****"



text = "Hello World"
lower_text = text.lower()
print(lower_text)   # outptut : hello world



text = "-------!Hello-------!"
stripped_text = text.lstrip("-!")
print(stripped_text)  #output Hello------!



translation_table = str.maketrans('ab','xy')
text = "alphabet"
translation_text = text.translate(translation_table)
print(translation_text)



translation_table = str.maketrans('123','abc')
text = "123 apples are 456 oranges"
translation_text = text.translate(translation_table)
print(translation_text)



text = "apple,banana,grape"
parts = text.partition(",")
print(parts)



sentence = "Hello! How are you?"
parts = sentence.partition(" ")
print(parts)



text = "Python is awesome"
parts = text.partition(",")
print(parts)



file = "document.pdf"
filename, separator , extension = file.partition(".")  # spilting the string at the first occurrance
print("Filename:", filename)
print("Extension:",extension)



text = "HelloWorld"
new_text = text.removeprefix("Hello")
print(new_text)



text = "HelloWorld.jpg"
new_text = text.removesuffix(".jpg")
print(new_text)



text = "apples are tasty, apples are juicy"
new_text = text.replace("apples","oranges")
print(text)



text = "apples,orange,banana,orange,grape"
last_occurrance = text.rfind('orange')
print(last_occurrance)  # ouput 23
last_occurrance = text.rfind('water')
print(last_occurrance) # ouput : -1
text = "The quick brown fox jumps over the lazy dog"
index = text.rfind("fox",0,20) # output : 16
print(index)  # its similar function to str.rindex()



text = "hello"
justified_text = text.rjust(10,'*')
print(justified_text)        # output : *****hello



text = "apple,banana,grape,banana"
parts = text.rpartition(",") # it spilts the string at the last occurance
print(parts)
text = "watermelon"
parts = text.rpartition(",")
print(parts)



text = "apple,banana,grape,orange"
split_text = text.rsplit(",",2)
print(split_text)



text = "This is a sentence"
split_text = text.rsplit()
print(split_text)



texts = ["apple,banana,grape,orange","one-two-three-four","alpha-beta-gamma-delta-epsilon"]

for text in texts:
    result = text.rsplit("-",2)
    print("Split result:" ,result)




text ="    HEllo   "
stripped_text = text.rstrip()
print(stripped_text)  # output = "    Hello"



text = "Hello!!!"
stripped_text = text.rstrip('!')
print(stripped_text)   # output : Hello



text = "Hello!World!Python!Programming"
split_text = text.split("!")
print(split_text) # output : ['Hello','World','Python','Programming']



text = "apple,banana,grape,orange"
split_text = text.split(",",2)
print(split_text) # output : ['apple','banana','grape,orange']



multiline_text = "Hello\nHow are you\nGoodbye"
split_line = multiline_text.split("\n")
print(split_line)



text = "Hello\nHow are you?\rGoodbye\r\nsee you leter"
split_lines = text.splitlines()
print(split_lines) # output : ['Hello','How are you?,'Goodbye','see you leter']



text = "Hello\nHow are you?\rGoodbye\r\nsee you leter"
split_lines_with_ends = text.splitlines(keepends=True)
print(split_lines_with_ends)



empty_text = ""
split_empty = empty_text.splitlines()
print(split_empty)



text = "Hello,how are you"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello) #  OUtput : True



text = "Hello, How are you?"
check = text.startswith("How",7,15)
print(check) # ouput : True


text = "Hello, How are you?"
starts_with_hi = text.startswith("Hi")
print(starts_with_hi) # output : False



text = "    Hello    "
stripped_text = text.strip()
print(stripped_text) # output : Hello



text = "----------------------HEllo--------------"
stripped_text = text.strip('-')
print(stripped_text)



text = "Hello World"
swapped_text = text.swapcase()
print(swapped_text)   #output : hELLO wORLD



text = "Hello world"
title = text.title()
print(title)  #output : Hello World



text1 = "Hello"
translation_table = text1.maketrans("lo","ip")
translated_text1 = text1.translate(translation_table)
print(translated_text1)  # output : Heiip



text = "42"
padded_text = text.zfill(5)
print(padded_text)  # output : 00042


text = "python"
padded_text = text.zfill(10)
print(padded_text)  # output : 00000python


