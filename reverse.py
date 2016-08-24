import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help = "input a file to display the file's lines in reverse")
args = parser.parse_args()
f = open(args.file)
out = []
for line in f:
    out.append(line)
f.close()
for t in range(0,len(out)):
    if '\n' in out[len(out)-t-1]:
        out[len(out)-t-1],sep,empty =out[len(out)-t-1].partition('\n')
    print(out[len(out)-t-1])
