String Definition:

ASCII vs UNICODE 

Check both
ASCII - includes latin,numbers and signs
UNICODE - global standard interperting text (all alphabets) and uspports moderns systems 

in Python all string objects are unicode by default, ASCII is  a part of unicode 

"" vs '' 

In pythoin if quotes are used inside a string they need to be different to the outer quotes

#wrong:
"He said "Hello""

#right
"He said 'Hello'"

'He said \'Hello\''

\ can be usd to escape a special symbol

id we have \to python will interpet \t as a tab ,so we need to escape \  as \\to

for multi prow input we use """ """

###Metohds
str() - transforms a variable into a s tring 
split() - splits a string by a delimiter into a list 

###string concat 
str1 = hello
str2 = " "
str3 = "Softuni"

string = str1 + str2 + str3
print(string) ## "hello Softuni"

###multiplication  -- ony for strigns * integers 
print(3 * 'hello')  ## hellohellohello

##String formatting 
name = 'Ivan'
age = 25

text = 'My name is %s and I amd %s years old'

###Substrings##
- slicing
text = "this is Softuni Fundamentals"
course = text[16:] ## fundamentsls
course = text[:-5]  ## fundamentsls (takes the last few letters)

text = 'Python Programming'

slice = text[0:10:2] #slices from the first ot the tenth letter, with step 2

print(slice) = Pro r

***String methods***

string = '12345'
string.isdigit() #True

string = 'Hello'
string.isdigit() #False

text = 'Hi'

print(text.center(10,"-"))
  ----Hi----  #makes the string lenght 10 and fills the balnks iwth --

text = banana
.find() #finds the occurnaces in a string 

text.find(na) #2 - finds num occurances of na in banana

print(' '.isspace()) #True

text = 'SoftUni'
print (text.istitle()) #True

lines = 'line1\nline2\nline3'
line1
line2
line3

line = lines.splitlines
# line = [line1,line2,line3] - slits the 3 lines into a list 

text = 'I like cats'
prtin(text.replace('cats','dogs')) # I like dogs
print(text.replace(' ','_',1)) #I_like dogs  - replaces only the first occurances

 #akways stire the replace as the changes are locally 