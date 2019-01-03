import ast
import json

#open the text file, w for write, r for read, r+ for read/write
dataset = open("Dataset.txt",'w')

#the dict that gonna be use and the dict need to be in string
val1 = json.dumps({'created_at':'5 feb', 'text':'Hello World1'})
val2 = json.dumps({'created_at':'6 feb', 'text':'Hello World2'})
val3 = json.dumps({'created_at':'7 feb', 'text':'Hello World3'})

#write val1,val2,val3 line by line with "\n"
dataset.write(val1 +'\n')
dataset.write(val2 +'\n')
dataset.write(val3 +'\n')

#close the text file
dataset.close()

#open for reading
dataset = open("Dataset.txt",'r')

#every line as a list of a string ['*']
line_list = dataset.readlines()

for line in line_list:

    #convert the Dictionary string to Dictionary "{}"-> {}
    data = ast.literal_eval(line)
    #accessing as normal dictionary
    print(data['created_at'])
    
#close the text file
dataset.close()
