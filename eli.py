"""
Autores:
Garcia Exposito, Antoni Lluis
Negro Carpintero, Raul
Sardon Ibanez, Yeray
Cao, Thi Huyen

Version de Python 2,7 o superior
"""
import re
import random

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

repeating= ["You've already said that",
            "Common, stop repeating yourself",
            "What are you trying to do by echoing the same sentense over and over",
            "I'm getting bored by this conversation",
            "Can't you think of something else to say",
            "If you keep repeating yourself, I'm going to have to stop this conversation",
            "I don't like that you keep repeating",
            "Why do you keep repeating yourself?",
            "I'm smart enough to know you are playing with me. Stop repeating yourself"]

no_response=["Please tell me something...",
            "Tell me more...",
            "Ok, continue, I'm still listening...",
            "Do you have any problem with keyboard? I didn't see what you typed",
            "Hey, don't you want to talk to me?",
            "Hey, I can't reply if you don't enter anything",
            "At least, take sometime to enter something meaningful",
            "I'm listening",
            "Nothing? Please say something to me",
            "I'm waiting for you"]

feelings = ["Do you often feel {0}?",
             "When do you usually feel {0}?",
             "When you feel {0}, what do you do?",
             "Tell me more about it."]

greetings= ["Nice to see you again!",
             "Hello again!",
             "Hello! How are you?",
             "Hello user, what is your name?",
             "Hello, who am I speaking with?",
             "Hi there, how can I help you?",
             "Anything you want to discuss today?",
             "Hi there... how are you today?",
             "Hello, how are you feeling today?",
             "Hello... I'm glad you could drop by today."]

father = ["Tell me more about your father.",
          "How did your father make you feel?",
          "How do you feel about your father?",
          "Does your relationship with your father relate to your feelings today?",
          "Do you have trouble showing affection with your family?"]

mother = ["Tell me more about your mother.",
          "What was your relationship with your mother like?",
          "How do you feel about your mother?",
          "How does this relate to your feelings today?",
          "Good family relations are important."]

child = ["Did you have close friends as a child?",
         "What is your favorite childhood memory?",
         "Do you remember any dreams or nightmares from childhood?",
         "Did the other children sometimes tease you?",
         "How do you think your childhood experiences relate to your feelings today?"]

question = ["Why do you ask that?",
            "Please consider whether you can answer your own question.",
      		"Perhaps the answer lies within yourself?",
      		"Why don't you tell me?"]

need = ["Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"]

whyCan = ["Do you think you should be able to {0}?",
      	  "If you could {0}, what would you do?",
	      "I don't know -- why can't you {0}?",
	      "Have you really tried?"]

iCan = ["How do you know you can't {0}?",
        "Perhaps you could {0} if you tried.",
        "What would it take for you to {0}?"]

iAm = ["Did you come to me because you are {0}?",
	   "How long have you been {0}?",
	   "How do you feel about being {0}?"
	   "How does being {0} make you feel?",
	   "Do you enjoy being {0}?",
	   "Why do you tell me you're {0}?",
	   "Why do you think you're {0}?"]

areYou = ["Why does it matter whether I am {0}?",
      	  "Would you prefer it if I were not {0}?",
     	  "Perhaps you believe I am {0}.",
      	  "I may be {0} -- what do you think?"]

whatAn = ["Why do you ask?",
          "How would an answer to that help you?",
     	  "What do you think?"]

howAn = ["How do you suppose?",
      	 "Perhaps you can answer your own question.",
      	 "What is it you're really asking?"]

becauseAn = ["Is that the real reason?",
      		 "What other reasons come to mind?",
      		 "Does that reason apply to anything else?",
      		 "If {0}, what else must be true?"]

sorryAn = ["There are many times when no apology is needed.",
           "What feelings do you have when you apologize?"]

iThink = ["Do you doubt {0}?",
          "Do you really think so?",
          "But you're not sure {0}?"]

computer = ["Are you really talking about me?",
      	    "Does it seem strange to talk to a computer?",
      		"How do computers make you feel?",
      		"Do you feel threatened by computers?"]

canYou = ["What makes you think I can't {0}?",
          "If I could {0}, then what?",
      	  "Why do you ask if I can {0}?"]

canI = ["Perhaps you don't want to {0}.",
        "Do you want to be able to {0}?",
        "If you could {0}, would you?"]

youAre = ["Why do you think I am {0}?",
       	  "Does it please you to think that I'm {0}?",
      	  "Perhaps you would like me to be {0}.",
      	  "Perhaps you're really talking about yourself?"]

idont = ["Don't you really {0}?",
         "Why don't you {0}?",
         "Do you want to {0}?"]

iHave = ["Why do you tell me that you've {0}?",
      	 "Have you really {0}?",
      	 "Now that you have {0}, what will you do next?"]

iWould = ["Could you explain why you would {0}?",
      	  "Why would you {0}?",
          "Who else knows that you would {0}?"]

iWant = ["What would it mean to you if you got {0}?",
      	 "Why do you want {0}?",
      	 "What would you do if you got {0}?",
      	 "If you got {0}, then what would you do?"]

quit = ["Thank you for talking with me.",
        "Good-bye.",
      	"Thank you, that will be $150.  Have a good day!"]

quits=["quit",
      "cancel",
      "stop"]


data = dict()
data[r'I feel(.*)'] = feelings
data[r'Hello(.*)'] = greetings
data[r'(.*) father(.*)'] =father
data[r'(.*) mother(.*)'] = mother
data[r'(.*) child(.*)'] = child
data[r'(.*)\?'] = question
data[r'I need (.*)'] = need
data[r'Why can\'?t I ([^\?]*)\??'] = whyCan
data[r'I can\'?t (.*)'] = iCan
data[r'I am (.*)'] = iAm
data[r'Are you ([^\?]*)\??'] = areYou
data[r'What (.*)'] = whatAn
data[r'How (.*)'] = howAn
data[r'Because (.*)'] = becauseAn
data[r'(.*) sorry (.*)'] = sorryAn
data[r'I think (.*)'] = iThink
data[r'(.*) computer(.*)'] = computer
data[r'Can you ([^\?]*)\??'] = canYou
data[r'Can I ([^\?]*)\??'] = canI
data[r'You are (.*)'] = youAre
data[r'I don\'?t (.*)'] = idont
data[r'I have (.*)'] = iHave
data[r'I would (.*)'] = iWould
data[r'I want (.*)'] = iWant
data[r'quit'] = quit

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)

def analyze(statement):
	for pattern in data.keys():
		match = re.match(pattern, statement.rstrip(".!"))
		if match:
			response = random.choice(data[pattern])
			return response.format(*[reflect(g) for g in match.groups()])

def main():
    print "============================================================"
    print "Welcome to our eliza chatbot"
    print "Press Ctrl C/ type stop/cancel/quit to get out of the conversation"
    print "Have fun"
    print "============================================================"
    print random.choice(greetings)
    last_sentence=""
    while True:
        statement = raw_input("> ")
        if not statement:
            print random.choice(no_response)
        else:	
            if last_sentence == statement:
                print (random.choice(repeating))
                last_sentence = statement
                continue
            last_sentence= statement
            if statement in quits:
                print (random.choice(quit))
                break
            print analyze(statement)

if __name__ == "__main__":
    main()
