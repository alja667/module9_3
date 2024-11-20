first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
z = zip(first,second)

first_result = (len(x[0]) - len(x[1]) for x in z  if len(x[0])!=len(x[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)) )



print(list(first_result))
print(list(second_result))