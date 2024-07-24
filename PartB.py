import sys
#======================================================================================
#  List<Token> tokenize(TextFilePath)
#  this method that reads in a text file and returns a list of the tokens in that file.
#
#  Run Time Complexity:
#  reading from a file is O(n) because we iterate through every character in the file
#  and read them
#  converting to lowercase 0(n) because we iterate through every character in the file
#  and convert each one to lowercase
#  iterating through every character and adding them to an empty string if they are
#  ascii && alphanumerical is O(n) since we are using a for loop to iterate through every
#  character in the text.
#  splitting a string whenever a whitespace char is encountered is 0(n) because each
#  char in the string is iterated.
#======================================================================================
def tokenize(TextFilePath):
     try:
        #opening a file
        with open(TextFilePath, 'r', encoding='utf-8') as inFile:

           # reading from input file and converting all characters to lowercase
           text = inFile.read().lower()

           # iterate through every character in the text and add them to an empty string
           # if they are ascii & alphanumerical. if not, add a whitespace char instead.
           result_string = ''
           for char in text:
               if char.isascii() and char.isalnum():
                   result_string += char
               else:
                   result_string += ' '

           # now spliting the string using a space as a separator
           tokenList = result_string.split()

        return tokenList

    # except UnicodeEncodeError:
        #raise ValueError("File contains non-English characters")

     except Exception as e:
        print(f"Error reading file: {e}")
        return []
#======================================================================================
# <int> countCommonToken(file1,file2)
# this method return number of common tokens among 2 files.
#
# Run Time Complexity:
# converting a list to a set is 0(n) since we are iterating through every element of a
# list and adding it to a set.
# finding intersection of 2 sets is O(min(len(s), len(t))), according to python wiki
# https://wiki.python.org/moin/TimeComplexity
#======================================================================================
def countCommonToken(file1, file2):

    # the code for finding common elements of 2 list is derived from the link:
    # https://www.geeksforgeeks.org/python-print-common-elements-two-lists/

    # converting both lists to set
    set1 = set(tokens1)
    set2 = set(tokens2)

    intersection = (set1.intersection(set2))
    return (len(intersection))


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("in the terminal, type : \n python PartB.py fileName1.txt fileName2.txt")
        sys.exit(1)

    # get the text file as a command line argument
    TextFilePath1 = sys.argv[1]
    TextFilePath2 = sys.argv[2]

    try:
        tokens1 = tokenize(TextFilePath1)
        tokens2 = tokenize(TextFilePath2)

        print(countCommonToken(TextFilePath1,TextFilePath2))

    except ValueError as ve:
        pass
    except FileNotFoundError:
        print(f"Error: File '{TextFilePath1}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")