import os 
import json

def main(): 
    directory = ''
    title = ''
    with open('info.txt') as json_file:
        data = json.load(json_file)
        directory = data['directory']
        title = data['title']

    for filename in os.listdir(directory):
        extension = ''
        extension = filename.split(".")[-1]
        my_dest = title + filename
        my_source =directory + filename
        my_dest =directory + my_dest
        os.rename(my_source, my_dest)

if __name__ == '__main__': 
    main() 