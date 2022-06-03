# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
avg = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else :
        count = count + 1
        
        split_str_by_space = line.split(':')
        
        for ind, word in enumerate(split_str_by_space) :
            if ind == 1 :
                floating = float(word)
                avg += floating
        
print(f'Average spam confidence: {avg / count}')