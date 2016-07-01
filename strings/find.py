# Enter your code here. Read input from STDIN. Print output to STDOUT

str = raw_input()
substr = raw_input()

times = 0

for i in range(len(list(str))):
    aux = list(str)[i:len(list(substr))+i]
    if len(aux) == len(list(substr)):
        goal = len(list(substr))
        for j in range(len(list(substr))):
            if aux[j] == list(substr)[j]:
                goal -= 1
            else:
                pass

        if goal == 0:
            times += 1
        else:
            pass

print times
