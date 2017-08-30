'''
            LISTS: GREETING FOR LEVELS, BLANKS, ANSWER KEY & PARAGRAPHS
'''


levels = "Type the level you prefer: easy, medium or hard  "


blanks = [
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

paragraphs = ['''3 of the 5 ways you can think as a programmers:\n
  ___1___ , ___2___ , ___3___ .  The purpose of ___4___ form is to be able to ___5___ describe exactly the\
 language in a way thats very simple and very ___6___ .''','''The ___1___ name can be ___2___ , ___3___ , \n
___4___ or a mix of all, as long as it starts with a ___5___ or ___6___.  ___7___ can vary.  ___8___ is \
a sequence of ___9___ surrounded by ___10___ - single or ___11___ .''', '''An ___1___ refers to position within an \
ordered list. Python strings can be thought of as list of  ___2___; each ___3___ is given an ___4___ from \
___5___ to the end of the string. We can use ___6___ numbers which will start ___7___ from the end of the string''','''___1___ is a ___2___ \
built in Python. When the ___3___ number its given, which gives the first ___4___ in ___5___ where the ___6___ appears. If ___7___ is not \
found, its given an ___8___ .''',' ']


#           MULTIPLE CHOICES EASY AND MEDIUM ** NO CHOICES FOR HARD LEVEL - ONLY INSTRUCTIONS

easy_mult = ['a.abstract thinking  b.technological empathy  c.procedural thinking \n\
d.backus-naur  e.congnitive  f.arithmetically  g.precisely  h.concise', 'a.variables  b.underscore  c. numbers  d.letter  e.variables  f.letters  g.quotes \
h.characters  i.string  j.double', 'a.counting  b.zero  c.index  d.characters  e.negative  f.character','a.target string  b.-1 \
c.position  d.method  e.find  f.search string ']

medium_mult = ['a.abs_____ _____ing  b.tech_____ical ____thy  c.pro_______ thi_____ d.____us-__ur\n\
 e._____sely  h.co_____', 'a.____ables  b.under_____  c. ____ers  d.___ter  e.___iab___  f.let____  g.q___es \
h.cha____ers  i.st____  j.do____', 'a.co___ing  b.__ro  c.____x  d.c_____ters  e.ne_____e  f.__aract__','a.ta___t ___ing  b. -_ \
c.po____on  d.__tho_  e.__nd  f.se___h s__in_ ']

no_mult = ['***the first 3 blanks must be in order to get them correctly*** ',' ',' ',' ']



#           MESSAGES FOR EACH LEVEL

easy_msg = 'Choose your answer from the following list for blank  '

<<<<<<< HEAD
medium_msg = 'Choose your answer from the following clues for blank  '

hard_msg = 'Type your answer for the following blank '

=======
questions = ['Choose your answer from the following list for ','Choose your answer form the following\
list for blank ']
>>>>>>> master

'''
              FUNCTIONS
'''


#         GREETING

def greeting(start_answer):
    answer = raw_input(start_answer)
    if answer == "easy":
      return "\n" + play(easy_msg, easy_mult)
    if answer == "medium":
      return "\n" + play(medium_msg, medium_mult)
    if answer == "hard":
      return "\n" + play(hard_msg, no_mult)
    else:
      return greeting(start_answer)


#         PASSING BLANKS IN paragraphs FUNCTION

def check_blank(word, blanks):
  for pos in blanks:
    if pos in word:
      return pos
  return None


<<<<<<< HEAD
#         ANSWER VERIFICATION

def answer_verify(answers, answer_key):
  while answers != answer_key:
    answers = raw_input((11 * ' ') + 'WRONG!!!!!!! TRY AGAIN  ')
    if answers == answer_key:
        return answers
  return answers



#         REPLACING BLANKS WITH USER'S ANSWERS

def quiz_game(paragraphs, blanks, msg_to_follow, mult_choices, answer_key):
  final_paragraph = []
  i = 0
  paragraphs = paragraphs.split()
  for word in paragraphs:
      replacement = check_blank(word, blanks)
      if replacement != None:
          print "\n"
          user_input = raw_input(msg_to_follow + replacement + ": \n" + mult_choices + (4* " "))
          checked_answers = answer_verify(user_input,answer_key[i])
          i+= 1
          word = checked_answers
          final_paragraph.append(word)
=======
def quiz_game(ml_string, blanks,questions,mult_answers):
  final_pg = []
  ml_string = ml_string.split()
  for word in ml_string:
      replacement = paragraphs(word,blanks)
      if replacement != None:
          print "\n"
          user_input = raw_input(questions + replacement + ": \n" + mult_answers + (3* " "))
          word = word.replace(replacement, user_input)
          final_pg.append(word)
>>>>>>> master
      else:
          final_paragraph.append(word)
  final_paragraph = " ".join(final_paragraph)
  return "\n\n" + (3 * " ") + final_paragraph + "\n\n\n\n"


<<<<<<< HEAD
#         LOOP FOR PARAGRAPHS

def play(msg_to_follow,mult_choices):
    i = 0
    while i != 4:
        print paragraphs[i]
        print quiz_game(paragraphs[i], blanks[i], msg_to_follow, mult_choices[i],answer_key[i])
        i += 1
    return " YOU ARE DONE! " + user


=======
>>>>>>> master
'''
                  GAME START
'''

print (80 * '-')
print " "* 25 + "Welcome! to 'POP QUIZ TIME' "
print (80 * '-')
print
user = raw_input("Enter your Name or Username" + (5*' '))
print
print 'Alright '+ user + "here is your chance to check if you know some basic keywords in Python!"
print
print "The following is a fill in the blank quiz. You'll be first prompt with \
paragraphs that will contain numbered blanks. These numbered blanks are keywords \
from 'Introduction to Serious Programming'."
print

<<<<<<< HEAD

print greeting(levels)

 
=======
print greeting(levels[0], start_list,pg_level[0]) + "\n"

print quiz_game(pg_level[0], blanks[0],questions[0],mult_answers[0])

print greeting(levels[1],start_list,pg_level[1]) + "\n"

print quiz_game(pg_level[1],blanks[1],questions[1],mult_answers[1])
>>>>>>> master
