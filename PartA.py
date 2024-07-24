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

     except UnicodeEncodeError:
        raise ValueError("File contains non-English characters")

     except Exception as e:
        print(f"Error reading file: {e}")
        return []
#============================================================
#  Map<Token,Count> computeWordFrequencies(List<Token>)
# this method counts the number of occurrences of each token in the token list.
#
#Run Time Complexity:
# The time complexity for computing the world frequencies is O(n) since we
# are using a for loop to iterate through every element of a list
# in order to dtermine if it already exists in the dictionary or not
#============================================================
def computeWordFrequencies(tokenList) -> dict:

    # create an empty dictionary
    myDictionary = dict();

    # iterate through every element in the tokenlist,
    # if element is already in our dictionary, increase count by 1
    # if it is not in our dictionary, add them to the dictionary and set the occurance to 1
    for element in tokenList:
        if element in myDictionary:
            myDictionary[element] += 1
        else:
            myDictionary[element] = 1

    return myDictionary

#=====================================================================
#   void print(Frequencies<Token, Count>)
# this method prints out the word frequency counts onto the screen.
# The print-out should be ordered by decreasing frequency.Resolve ties alphabetically and in ascending order
#
# Run Time Complexity:
#    python's built-in sorting function, sorted() is based on timsort algorithm
#    and the run time complexity for timsort algorithm is O(nlogn)
#    where n is the number of elements in the dictionary.
#    source : https://medium.com/@bhargavacharanreddy/do-you-know-the-time-complexity-of-pythons-sorted-function-1ae9e7d712b1
#    for printing the key,value pairs in our dictionary,
#    we are using a for loop to iterate through  every element of the dictionary
#    so the run time complexity is O(n) where n is num of key-value pairs in dictionary
#    in conclusion, the overall time complexity of print_frequency() method is O(nlogn)
#====================================================================
def print_frequency(dictionary):

    # The code for sorting the dictionary is derived from the following link
    # https://stackoverflow.com/questions/15371691/how-to-sort-a-dictionary-by-value-desc-then-by-key-asc
      sorted_dictionary = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))

      for token, count in sorted_dictionary:
          print(f'{token}\t {count}')
#============================================================
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("in the terminal, type : \n python PartA.py file1.txt")
        sys.exit(1)

    # get the text file as a command line argument
    TextFilePath = sys.argv[1]

    try:
        tokens = tokenize(TextFilePath)
        word_frequencies_dict = computeWordFrequencies(tokens)
        print_frequency(word_frequencies_dict)

    except ValueError as ve:
        pass
    except FileNotFoundError:
        print(f"Error: File '{TextFilePath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")