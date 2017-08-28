'''
            LISTS: GREETING FOR LEVELS, BLANKS & PARAGRAPHS
'''


levels = "Type the level you prefer: easy, medium or hard  "


easy_blanks = [
          ["___1___", "___2___", "___3___","___4___", "___5___", "___6___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___", "___9___", "___10___", "___11___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___"]
          ]

medium_blanks = [
          ["___1___", "___2___", "___3___","___4___", "___5___", "___6___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___", "___9___", "___10___", "___11___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___"]
          ]

hard_blanks = [
          ["___1___", "___2___", "___3___","___4___", "___5___", "___6___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___", "___9___", "___10___", "___11___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"],
          ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___"]
          ]

answer_key = [['procedural thinking','technological empathy','abstract thinking','backus-naur','precisely','concise'],
              ['variable','letters','numbers','underscore','letter','underscore','variables','string','characters','quotes','double'],
              ['index','characters','character','index','zero','negative','counting'],
              ['find','method','target string','position','search string','target string','target string','-1']
              ]

pg_level = ['''3 of the 5 ways you can think as a programmers:\n
  ___1___ , ___2___ , ___3___ .  The purpose of ___4___ form is to be able to ___5___ describe exactly the\
 language in a way thats very simple and very ___6___.''','''The ___1___ name can be ___2___ or ___3___ \n
___4___ or a mix of all, as long as it starts with a ___5___ or ___6___.  ___7___ can vary.  ___8___ is \
a sequence of ___9___ surrounded by ___10___ - single or ___11___.''', '''An ___1___ refers to position within an \
ordered list. Python strings can be thought of as list of  ___2___; each ___3___ is given an ___4___ from \
___5___ to the end of the string. We can use ___6___ numbers which will start ___7___ from the end of the string''','''___1___ is a ___2___ \
built in Python. When the ___3___ number its given, which gives the first ___4___ in ___5___ where the ___6___ appears. If ___7___ is not \
found, its given an ___8___.''',' ']

mult_choices = ['a.computing empathy  b.artificial thinking  c.abstract thinking \n d.technological empathy  e.procedural thinking d.backus-naur\n\
 e.congnitive  f.arithmetically  g.precisely  h.concise', ' ', ' ',' ',' ']

msg_to_follow = ['Choose your answer from the following list for ','Choose your answer from the following\
 list for blank ','Type your answer for the following blank ','Type your answer for the following blank ','Type your answer for the following blank','\
Type your answer for the following blank ']

'''
              FUNCTIONS
'''


#         GREETING

def play(diff):
    i = 0
    while i != 4:
        print pg_level[i]
        print quiz_game(pg_level[i], diff[i], msg_to_follow[i], mult_choices[i],answer_key[i])
        i += 1
    return " YOU ARE DONE! " + user

def greeting(start_answer, pg_level):
    answer = raw_input(start_answer)
    if answer == "easy":
      return "\n" + play(easy_blanks)
    if answer == "medium":
      return "\n" + play(medium_blanks)
    if answer == "hard":
      return "\n" + play(hard_blanks)
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
  print "1st " + answer_key
  while answers != answer_key:
    answers = raw_input((11 * ' ') + 'WRONG!!!!!!! TRY AGAIN  ')
    print "answer varification " + answers
    if answers == answer_key:
        return answers
  return answers



#         REPLACING BLANKS WITH USERS WORDS

def quiz_game(pg_level, blanks, msg_to_follow, mult_choices, answer_key):
  final_pg = []
  i = 0
  pg_level = pg_level.split()
  for word in pg_level:
      replacement = paragraphs(word, blanks)
      if replacement != None:
          print "\n"
          user_input = raw_input(msg_to_follow + replacement + ": \n" + mult_choices + (4* " "))
          checked_answers = answer_verify(user_input,answer_key[i])
          i+= 1
          print "index number " + str(i)
          word = checked_answers
          final_pg.append(word)
#          if checked_answers != None:
#              word = checked_answers
#              final_pg.append(word)
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


print greeting(levels,pg_level)

