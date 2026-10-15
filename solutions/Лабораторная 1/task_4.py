student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
#1
print (student[0], student[3])
#2
print (student[:4], '\n', student[4:])
#3
print (student.upper(), student.lower())
#4
print(f'{student[0]}. {student[5]}.')
#5
print(course[::-1])
#6
percent=completed/total*100
#6.1
ans="%s - %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
print (ans)
#6.2
ans = "{} - {} : {}/{} ({:.1f}%)" .format(student, course, completed, total, percent)
print (ans)
#6.3
ans = f'{student} - {course}: {completed}/{total} ({percent:.1f}%)'
print (ans)

#7:
symbol = "Я"
symbol_code = ord(symbol)
print(symbol_code, chr(symbol_code), symbol.encode("utf-8"), len(symbol.encode("utf-8")))

#8:
# str='abcd'
# str[0]='j'
# TypeError: 'str' object does not support item assignment

