
print (30 * '-')
print " "* 4 + "Welcome to my Quiz!"
print (30 * '-')
print
user = raw_input("Enter your First Name" + (3*' '))
print
print 'Hello '+ user + "!"
print
print "The following is a fill in the blank quiz. You'll be first prompt with \
paragraphs that will contain numbered blanks. These numbered blanks are keywords \
from 'Introduction to Serious Programming'."
print


# The following its the paragraph to pass in to the quiz_game function.
sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The following its a fuction that will greet the user with a prompt "Press Y to Start"
levels = ["Type Start to begin!", "Type Start to begin level 2!"]

'''
     The function below DOES NOT give an error if the user does not type
     Start or start correctly. It skips to prompt user to the first question.
'''

level1 = "Type Start to begin!" + (3* " ")
level2 = "Type Start to begin level 2!" + (3 * " ")
levels = ['Type Start to begin!','Type Start to begin level2']
start_list = ["Start","start"]
def greeting(answer, start_list):
  answer = raw_input(answer)
  for pos in start_list:
    if pos in answer:
      if levels in answer 
      return "\n"+ 
    
print greeting(levels[1], start_list) + "\n"

'''
     Right after the paragraph its printed, the user will be prompt with questions,
     one at a time, for each of the blanks.safa
'''
# A list of key letters for the first paragraph to be passed in to the quiz_game function.
blanks1 = ["___1___", "___2___", "___3___", "___4___"]

def paragraphs(word,blanks1):
  for pos in blanks1:
    if pos in word:
      return pos
  return None
'''
    User is prompted to replace the numbered blanks in ml_string,
    which appear in select_answers with their own words.
    
    THINGS TO WORK ON:
    1. FILL IN THE ANSWER FOR ALL THE BLANKS THAT HAVE THE SAME NUMERICAL SEQUENCE.
    2. ANY WRONG ANSWERS WILL BE SHOWN AT THE END IN THE PARAGRAPH WITH THE WORD
       'WRONG' INSTEAD OF THE NUMERICAL BLANK.
'''
def quiz_game(ml_string, blanks1):
  final_pg = []
  ml_string = ml_string.split()
  for word in ml_string:
      replacement = paragraphs(word,blanks1)
      if replacement != None:
          print "\n"
          user_input = raw_input("Choose for the following for blank " + replacement + ": \n\
a.Function  b.Perimenters  c.None  or  d.List" + (3* " "))
          word = word.replace(replacement, user_input)
          final_pg.append(word)
      else:
          final_pg.append(word)
  final_pg = " ".join(final_pg)
  return "\n" + (3 * " ") + final_pg + "\n\n"

print quiz_game(sample, blanks1)

'''
    LEVEL 2
'''

print greeting(level2,start_list)
