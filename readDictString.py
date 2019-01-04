import yaml

# open for reading
with open("Dataset(sep29-aug30).txt", 'r') as dataset:

    # split every string ended with '\n' into a list of a string ['*']
    line_list = dataset.read().split('\n')

    #for the end of line
    end = ''

    for line in line_list:
        if line != end:
            # convert stringed dict into dict "*" -> {*:**}
            line_dict = yaml.load(line)
            # accessing the key
            print(line_dict['created_at'])
        else:
            break
            
    # close the text file
    dataset.close()
