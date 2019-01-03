import ast

#open the text file, r for read
dataset = open("Dataset.txt",'r')

#every line as a list of a string ['*']
line_list = dataset.readlines()

for line in line_list:

    #convert the Dictionary string to Dictionary "{}"-> {}
    data = ast.literal_eval(line)
    #accessing as normal dictionary
    print(data['created_at'])
    

dataset.close()
