# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#from hashlib import new


def read_file(filename):
        # [assignment] Add your code here
    open_file = open("./story.txt","r")
    read_file_content = open_file.read()
        #print(open_file)
    new = read_file.split()
        #print(new)
    count ={}
    for i in new:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    return count
print(read_file("./story.txt"))