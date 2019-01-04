import yaml

#open for reading
dataset = open("test.txt",'r')

#split every string ended with '\n' into a list of a string ['*']
line_list = dataset.read().split('\n')


for line in line_list:

    #convert stringed dict into dict "*" -> {*:**}
    line_dict = yaml.load(line)
    #accessing the key
    print(line_dict['created_at'])

    
#close the text file
dataset.close()


