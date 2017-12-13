import re
import random

def greetings():
    array = ["Nice to see you again!", 
             "Hello again!", 
             "Hello! How are you?",
             "Hi there... how are you today?", 
             "Hello, how are you feeling today?",
             "Hello... I'm glad you could drop by today."]
    
    max_len = len(array)
    index = randint(0, max_len-1)
    return array[index]

def repeating():
	#repeat pattern
	return ""

def no_response():
	#no more reponse from user
	return "Please input something"

def meaningless():
	#don't understand user input
	return ""

def change_topic():
	#change topic
	return ""

def basic_questions():
	#common questions
	return ""

def feelings(feeling):
    array = ["Do you often feel "+feeling+"?", 
             "When do you usually feel "+feeling+"?",
             "When you feel "+feeling+", what do you do?", 
             "Tell me more about it."]
    
    max_len = len(array)
    index = randint(0, max_len-1)
    return array[index]

def conversation():
	#the rest
	return ""

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

feelings = ["Do you often feel{}?", 
             "When do you usually feel {0}?",
             "When you feel {0}, what do you do?", 
             "Tell me more about it."]

greetings = ["Nice to see you again!", 
             "Hello again!", 
             "Hello! How are you?",
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
child =["Did you have close friends as a child?",
       "What is your favorite childhood memory?",
       "Do you remember any dreams or nightmares from childhood?",
       "Did the other children sometimes tease you?",
       "How do you think your childhood experiences relate to your feelings today?"]

data = dict()
data[r'I feel(.*)'] = feelings
data[r'Hello(.*)'] = greetings
data[r'(.*) father(.*)']=father
data[r'(.*) mother(.*)']= mother
data[r'(.*) child(.*)']= child 

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
	print("Hello.")
	while True:
		statement = raw_input("> ")
		print(analyze(statement))


if __name__ == "__main__":
    main()
    