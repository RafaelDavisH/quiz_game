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

answer_key = [['procedural thinking','technological empathy','abstract thinking'],
              ['backus-naur','precisely','concise'],
              ['variable','letters','numbers','underscore','letter','underscore','variables'],
              ['string','characters','quotes','double'],
              ['index','characters','character','index','zero','negative','counting'],
              ['find','method','target string','position','search string','target string']
              ]

pg_level = ['''3 of the 5 ways you can think as a programmers:\n
***The order of your answer matters to get them correctly***\n
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

mult_choices = ['a.computing empathy  b.artificial thinking  c.abstract thinking  d.technological empathy  e.procedural thinking','a.backus-naur\
 b.congnitive  c.arithmetically  d.precisely  e.concise', ' ', ' ',' ',' ']

msg_to_follow = ['Choose your answer from the following list for ','Choose your answer from the following\
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

def paragraphs(word, blanks):
  for pos in blanks:
    if pos in word:
      return pos
  return None

#         ANSWER VERIFICATION

def answer_verify(answers, answer_key):
  for e in answer_key:
    if e in answers:
      return e
    return None


#         REPLACING BLANKS WITH USERS WORDS

def quiz_game(pg_level, blanks, msg_to_follow, mult_choices, answer_key):
  final_pg = []
  pg_level = pg_level.split()
  for word in pg_level:
      replacement = paragraphs(word, blanks)
      if replacement != None:
          print "\n"
          user_input = raw_input(msg_to_follow + replacement + ": \n" + mult_choices + (3* " "))
          checked_answers = answer_verify(user_input, answer_key)
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
print " "* 4 + "Welcome to a Quiz Game!"
print (30 * '-')
print
user = raw_input("Enter your First Name" + (3*' '))
print
print 'Alright '+ user + "here is your chance to check if you know some basic keywords in Python!"
print
print "The following is a fill in the blank quiz. You'll be first prompt with \
paragraphs that will contain numbered blanks. These numbered blanks are keywords \
from 'Introduction to Serious Programming'."
print

print greeting(levels[0], pg_level[0])

print quiz_game(pg_level[0], blanks[0], msg_to_follow[0], mult_choices[0],answer_key[0])

print pg_level[1]

print quiz_game(pg_level[1], blanks[1], msg_to_follow[1], mult_choices[1],answer_key[1])

print greeting(levels[1], pg_level[2]) + "\n"

print quiz_game(pg_level[2], blanks[2], msg_to_follow[2], mult_choices[2],answer_key[2])

print pg_level[3]

print quiz_game(pg_level[3], blanks[3], msg_to_follow[3], mult_choices[3],answer_key[3])

print greeting(levels[2], pg_level[4]) + "\n"

print quiz_game(pg_level[4], blanks[4], msg_to_follow[4], mult_choices[4],answer_key[4])

print pg_level[5]

print quiz_game(pg_level[5], blanks[5], msg_to_follow[5], mult_choices[5],answer_key[5])


print "GOOD JOB " + user + "! YOU ARE DONE"
