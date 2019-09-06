# Problem Set 4B
# Name: <Andy Shen>
# Collaborators: N/A
# Time Spent: x:xx

import string

#constants
ASCII_LOWERCASE_START = 97
ASCII_UPPERCASE_START = 65

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
WORD_LIST = load_words(WORDLIST_FILENAME)

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = WORD_LIST

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shift_dict = {}
        #separate loops for lower/uppercase letters for readability
        for letter in string.ascii_lowercase:
            #to ensure that resultant ascii representation of char is within the range(lowercase start:end), modulo 26 is used
            new_ascii = (ord(letter) - ASCII_LOWERCASE_START + shift) % 26
            shift_dict[letter] = chr(new_ascii + ASCII_LOWERCASE_START)
        
        #same logic as lowercase loop, just with a different constant 
        for letter in string.ascii_uppercase:
            new_ascii = (ord(letter) - ASCII_UPPERCASE_START + shift) % 26
            shift_dict[letter] = chr(new_ascii + ASCII_UPPERCASE_START)

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher = self.build_shift_dict(shift)
        message = self.get_message_text()
        encrypted = ""
        #build encrypted message one letter at a time according to the cipher
        for letter in message:
            #non alphabetical letters are ignored, pursuant to the spec
            if letter in cipher:
                encrypted += cipher[letter]
            else:
                encrypted += letter

        return encrypted
        
    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def findWordHelper(self, shift):
        '''
        Returns the number of valid words after applying a shift to an encrypted message
                
        shift (int): the number to shift by 
        '''
        #applies shift onto message and separates into individual words
        words = self.apply_shift(shift).split()
        #appends shifted word to list of words if valid
        valid = [word for word in words if is_word(self.valid_words, word)]
        return len(valid)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #list storing number of valid words for every shift from 0-25
        numWords = [self.findWordHelper(alpha) for alpha in range(26)]
        #shift number is implicitly store in the index of each entry in numWords
        bestShift = numWords.index(max(numWords))
        return (bestShift, self.apply_shift(bestShift))
            

if __name__ == '__main__':
    #TODO: WRITE YOUR TEST CASES HERE
    # m = Message("foo bar")
    # print(m.get_message_text())
    # print(m.build_shift_dict(2))
    # print(m.apply_shift(2))

    # n = PlaintextMessage("foo bar", 2)
    # print(n.get_message_text())
    # print(n.get_shift())
    # print(n.get_encryption_dict())
    # print(n.get_message_text_encrypted())
    # n.change_shift(1)
    # print(n.get_shift())
    # print(n.get_encryption_dict())
    # print(n.get_message_text_encrypted())

    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    plaintext2 = PlaintextMessage('jasmine', 1)
    print('Expected Output: kbtnjof')
    print('Actual Output:', plaintext2.get_message_text_encrypted())

    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    ciphertext2 = CiphertextMessage('kbtnjof')
    print('Expected Output:', (25, 'jasmine'))
    print('Actual Output:', ciphertext2.decrypt_message())

    #TODO: best shift value and unencrypted story 
    story = CiphertextMessage(get_story_string())
    print(story.decrypt_message())
    
    #best shift:
    # 12
    #story: 
    # Jack Florey is a mythical character created on the spur of a moment to help cover an 
    # insufficiently planned hack. He has been registered for classes at MIT twice before, 
    # but has reportedly never passed aclass. It has been the tradition of the residents of 
    # East Campus to become Jack Florey for a few nights each year to educate incoming students 
    # in the ways, means, and ethics of hacking.