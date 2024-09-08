title_hymn = "lolec nignog: jedna dva tri styri pat sest sedem ostem devet desat jedenast dvanast"

possible_title, sep, hymn = ['','',title_hymn] if title_hymn.partition(':')[2] == '' else  title_hymn.partition(':')

kek1 = hymn.split()[0:-3:3]

kek2 = ','.join(kek1)

print(kek2)

print(sep)
print(possible_title)