class StringUtility:
  """a class to represent how the strings will be utilized in the code """

  def __init__(self,string=''):
    """the constructor for StringUtility class,takes a string as a parameter and stores it as an instance variable
    self: (str) represent an instance (object) of the given class
    string: (str) strings that are inputted into the code 
    Return: None"""
    self.string = string

  def __str__(self):
    """stores the internal string itself, unchanged
    self: (str), string inputted in the code
    return: (str) the internal string itself is returned unchanged"""
    internal_string = str(self.string)
    return internal_string

  def vowels(self):
    """counts the number of vowels in the string
    self: (str) is the inputted string in the code
    return: (str) returns the number of vowels in the string. If count is 5 or more, the word 'many' is returned instead"""
    vowels = "aeiouAEIOU"
    count = 0
    for letter in self.string:
        if letter in vowels:
            count = count + 1
            if count >= 5:
              return 'many'
    return str(count)

  
  def bothEnds(self):
    """function creates a string made of the first 2 and last 2 characters of the original string 
    self: (str) inputted string 
    return: (str) returns a string made of the first 2 and last 2 characters of the original string or if the string length is less than or equal to 2, an empty string is returned"""
    if len(self.string) <= 2:
      return ''
    else:
      return self.string[0:2] + self.string[-2:]
       
      
  def fixStart(self):
    """creates string where all of the occurrences of the first character of been changed to '*' except for the first character itself
    self: (str) inputted string
    return: (str) if the string length is 1 or less, return the string as it is. Otherwise, return a string where all occurences of the first character have been changed to '*' except the first character itself"""
    if len(self.string) <= 1: 
      return ''
    else:
     return self.string[0] + self.string[1:].replace(self.string[0],'*')
    

  def asciiSum(self):
    """creates an integer that is sum of all ascii values in the string
    self: (str) inputted string
    return: (int) returns an integer that is the sum of all ascii values in the string"""
    total = 0
    word = self.string
    for letter in word:
      total += ord((letter))
    return int(total)
      

  def cipher(self):
    """creates an encoded string by incrementing all letters by the length of the string which accounts for wrap arounds, uppercase, and lowercase
    self: (str) inputted string
    return: returns an encoded string by incrementing all letters by the length of the string. """
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    word = self.string
    cipher = ""
    space = " "
    for letter in word:
      if letter in alphabet.lower():
        newletters = chr(((ord(letter) + len(word) - 97) % 26) + 97)
        cipher += newletters
      elif letter in alphabet.upper():
        newletters = chr(((ord(letter) + len(word) - 65) % 26) + 65)  
        cipher += newletters
      elif letter in space: 
        cipher += letter 
    return cipher
      
      
      
    
      
  
  

  
    