# Enter your code here. Read input from STDIN. Print output to STDOUT

str = raw_input()

result = ""

for letter in str:
    if letter.isupper():
         result += letter.lower()
    else:
        result += letter.upper()


print result
            
