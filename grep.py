#Anthony's problem 20 solution:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help = "input a file to display the file's lines in reverse")
parser.add_argument("key", help = "input a string to search for")
args = parser.parse_args()
f = open(args.file)
skey = args.key
#f = open('she.txt')
#skey = 'sure'
#The above lines should be comented out and the lines comented in to make it function as a program called
#by python grep.py she.txt sure
list_lines = []
for line in f:
    list_lines.append(line)  
f.close()
for i in range(0,len(list_lines)):
    list_lines[i],extra,extra2 = list_lines[i].partition('\n')
    if skey in list_lines[i]:
        print(list_lines[i])
