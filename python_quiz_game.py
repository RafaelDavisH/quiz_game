'''
            LISTS: GREETING FOR LEVELS, BLANKS & PARAGRAPHS
'''

levels = ['Type Start to begin!' + (3*' '),
          'Type Start to begin level2'+ (3*' '),
          'Type Start to begin level3'+ (3*' '),
          'Type Start to begin level4'+ (3*' '),
          'Type Start to begin level5'+ (3*' '),
          'Type Start to begin level6'+ (3*' '),
          'Type Start to begin level7'+ (3*' '),
          'Type Start to begin level8'+ (3*' ')
          ]


blanks = [
          ["___1___", "___2___", "___3___", "___4___"],
          ["___1___", "___2___", "___3___", "___4___"]
          ]

pg_level = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
            '''This is the second paragraph. You specify the inputs a ___1___ takes by
adding ___2___separated by commas between the parentheses.''']

mult_answers = ['a.Function  b.Perimenters  c.None  or  d.List','a.blah  b.blahs  c.None  or  d.List']



'''
              FUNCTIONS
'''


#         GREETING
start_list = ["Start","start"]
def greeting(answer, start_list,pg_level):

  answer = raw_input(answer)
  for pos in start_list:
    if pos in answer:
      return "\n"+ pg_level
    
#         PASSING BLANKS IN paragraphs FUNCTION

def paragraphs(word,blanks):
  for pos in blanks:
    if pos in word:
      return pos
  return None

#         REPLACING BLANKS WITH USERS WORDS

def quiz_game(ml_string, blanks,mult_answers):
  final_pg = []
  ml_string = ml_string.split()
  for word in ml_string:
      replacement = paragraphs(word,blanks)
      if replacement != None:
          print "\n"
          user_input = raw_input("Choose your answer from the following for blank " + replacement + ": \n" + mult_answers + (3* " "))
          word = word.replace(replacement, user_input)
          final_pg.append(word)
      else:
          final_pg.append(word)
  final_pg = " ".join(final_pg)
  return "\n" + (3 * " ") + final_pg + "\n\n"



'''
                  GAME START
'''

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

print greeting(levels[0], start_list,pg_level[0]) + "\n"

print quiz_game(pg_level[0], blanks[0],mult_answers[0])

print greeting(levels[1],start_list,pg_level[1])

print quiz_game(pg_level[1],blanks[1],mult_answers[1])
