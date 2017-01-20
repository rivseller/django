#пример работы py
import sys
import datetime

#получение параметра из jenkins
param_list=list()
for param in sys.argv:
    param_list.append(param)
	
print (param_list[1])

#переменные
name = param_list[1]
now = str(datetime.datetime.now())

#функции
def error_log(error):
	file_err=open(r"D:/python/py_error.txt", "a+")
	file_err.write(error)
	file_err.close()


print (now)

#логика
if name=="Савлук" :
	decision='APPROVE'
else:
	decision='DECLINE'

print (decision)

if decision=='DECLINE':
	error_text="Decline decision {}; \n".format(now)
	error_log(error_text)

