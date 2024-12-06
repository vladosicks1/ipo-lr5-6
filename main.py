string  = open('text.txt','r',encoding='utf-8') #открытие файла для чтения
out = open('output.txt','w',encoding='utf-8') #открытие файла для записи

i = 1 #номер строки 


for line in string: 
   
    out.write(str(i) + " ") # запись номера строки
    out.write(line) # запись самой строки
    i+=1 #переход к новому номеру строки

string.close() #закрытие файлов
out.close()