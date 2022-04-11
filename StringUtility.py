class StringUtility:

  def __init__(self,string=''):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    vowels = "aeiouAEIOU"
    count = 0
    for char in self.string:
        if char in vowels:
            count = count + 1
            if count >= 5:
              return 'many'
    return str(count)

  
  def bothEnds(self):
    if len(self.string)<= 2:
      return ''
    else:
      return self.string[0:2] + self.string[-2:]
    
  
  def fixStart(self):
    if len(self.string) <= 1: 
      return ''
    else:
     return self.string[0] + self.string[1:].replace(self.string[0],'*')
    

  #def asciiSum(self):
   #return s
    

  def cipher(self):
    for i in self.string:
      
  
  

  
    