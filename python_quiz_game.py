'''
            LISTS: GREETING FOR LEVELS, BLANKS & PARAGRAPHS
'''


levels = ['Type "Start" to begin!' + (3*' '),
          'Type "Start" to begin level2'+ (3*' '),
          'Type "Start" to begin level3'+ (3*' '),
          'Type "Start" to begin level4'+ (3*' '),
          'Type "Start" to begin level5'+ (3*' '),
          'Type "Start" to begin level6'+ (3*' ')
          ]


blanks = [
          ["__________", "__________", "__________"],
          ["___1___", "___2___", "___3___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"],
          ["___1___", "___2___", "___3___", "___4___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___"]
          ]

answer_key = ['Procedural Thinking','Technological Empathy','Abstract Thinking']

pg_level = ['''3 of the 5 ways you can think as a programmers:\n
  1.__________\n
  2.__________\n
  3.__________\n''','''The purpose of ___1___ form is to be able to ___2___ describe exactly the\
 language in a way thats very simple and very ___3___.''','''The ___1___ name can be ___2___ or ___3___ \n
___4___ or a mix of all, as long as it starts with a ___5___ or ___6___. ___7___ can vary.''', '''___1___ is \
a sequence of ___2___ surrounded by ___3___ - single or ___4___.''', '''An ___1___ refers to position within an \
ordered list. Python strings can be thought of as list of  ___2___; each ___3___ is given an ___4___ from \
___5___ to the end of the string. We can use ___6___ numbers which will start ___7___ from the end of the string''','''___1___ is a ___2___ \
built in Python. When the ___3___ number its given, which gives the first ___4___ in ___5___ where the ___6___ appears. If ___7___ is not \
found, its given an ___8___.''']

mult_answers = ['a.Computing Empathy  b.Artificial Thinking  c.Abstract Thinking  d.Technological Empathy  e.Procedural Thinking','a.Backus-Naur\
 b.Congnitive  c.Arithmetically  d.Precisely  e.Concise', ' ', ' ',' ',' ']

questions = ['Choose your answer from the following list for ','Choose your answer from the following\
 list for blank ','Type your answer for the following blank ','Type your answer for the following blank ','Type your answer for the following blank','\
Type your answer for the following blank ']

'''
              FUNCTIONS
'''


#         GREETING

def greeting(start_answer, pg_level):
    answer = raw_input(start_answer)
    if answer == "Start":
      return "\n" + pg_level
    if answer == "start":
      return "\n" + pg_level
    else:
      return greeting(start_answer, pg_level)
    
  
#         PASSING BLANKS IN paragraphs FUNCTION

def paragraphs(word,blanks):
  for pos in blanks:
    if pos in word:
      return pos
  return None

#         ANSWER VERIFICATION

def answer_verify(answers,answer_key):
  for e in answer_key:
    if e in answers:
      return e
    return None

#         REPLACING BLANKS WITH USERS WORDS

def quiz_game(ml_string, blanks,questions,mult_answers):
  final_pg = []
  ml_string = ml_string.split()
  for word in ml_string:
      replacement = paragraphs(word,blanks)
      if replacement != None:
          print "\n"
          user_input = raw_input(questions + replacement + ": \n" + mult_answers + (3* " "))
          checked_answers = answer_verify(user_input,answer_key)
          if checked_answers != None:
            word = word.replace(replacement, checked_answers)
            final_pg.append(word)
          else:
            checked_answers = "WRONG"
            word = word.replace(replacement, checked_answers)
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

print greeting(levels[0], pg_level[0])

print quiz_game(pg_level[0], blanks[0], questions[0], mult_answers[0])

print pg_level[1]

print quiz_game(pg_level[1], blanks[1], questions[1], mult_answers[1])

print greeting(levels[1], pg_level[2]) + "\n"

print quiz_game(pg_level[2], blanks[2], questions[2], mult_answers[2])

print pg_level[3]

print quiz_game(pg_level[3], blanks[3], questions[3], mult_answers[3])

print greeting(levels[2], pg_level[4]) + "\n"

print quiz_game(pg_level[4], blanks[4], questions[4], mult_answers[4])

print pg_level[5]

print quiz_game(pg_level[5], blanks[5], questions[5], mult_answers[5])
