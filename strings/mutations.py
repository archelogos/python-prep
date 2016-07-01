# Enter your code here. Read input from STDIN. Print output to STDOUT

string = raw_input()
second_line = raw_input().split(" ")

index = int(second_line[0])
letter = second_line[1]

aux = list(string)
aux[index]=letter

result = "".join(aux)

print result
