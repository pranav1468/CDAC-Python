

# function 1
def count_lines(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return len(lines)


# function 2
def count_characters(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return len(text)


# function 3
def test(filename):
    lines = count_lines(filename)
    characters = count_characters(filename)
    return lines, characters

#function 4
def count_word(filename):
    f = open(filename, 'r')
    word = f.readlines()
    word = word.split()
    f.close
    return len(word)
    
    



# Question 4

import mymod as mymod
if __name__ == "__main__":
    file = input("Enter the filename with path: ")
    print("Number of lines in the file:", mymod.count_lines(file))
    print("Number of characters in the file:", mymod.count_characters(file))
    print("Lines and characters:", mymod.test(file))
else:
    print("mymod module has been imported.")

#when you run my