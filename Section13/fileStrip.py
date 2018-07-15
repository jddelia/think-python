''' This program reads a file, breaks each line
    to words, strips punctuations, and makes it lower
    case. '''

fin = open('words3.txt')
line = fin.readline()
word = line.strip

def file_format():
    word_lst = [line.strip().lower() for line in fin]
    return word_lst

print(file_format())
