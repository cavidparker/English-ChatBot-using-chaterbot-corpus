# #import ChatBot

# from chatterbot import ChatBot
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# import os

# bot = ChatBot('Candice')


# # Train your bot :
# from chatterbot.trainers import ListTrainer
# bot.set_trainer(ListTrainer)

# ### Training

# bot.train(['What is your name ?', 'My name is Candice'])
# bot.train(['Who are ?','I am a bot,created by cavid'])
# bot.train(['Do you know me ?', 'Yes, you created me ','No babe', 'parker'])

# #  So, we will use ChatterBotCorpusTrainer to train our bot on the large dataset:

# from chatterbot.trainers import ChatterBotCorpusTrainer
# ## Create a new trainer for chatbot
# trainer = ChatterBotCorpusTrainer(bot)

# ## Train the chatbot based on the english corpus 
# trainer.train("chatterbot.corpus.english")

# ## get  a response to an input statement
# chatbot.get_response("Hello, How are you today?")

# for file in os.listdir('./english/'):
# 	data = open('./english/'+files,'r').readlines()
# 	bot.train(data)


# # chat feature :
# while True:
# 	message=input('\t\t\tYou:')
# 	if message.strip()!='Bye':
# 		replay=bot.get_response(message)
# 		print('Candice:',replay)
# 	if message.strip()=='Bye':
# 		print('Candice: Bye')
# 		break

#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#Create a chatbot
bot=ChatBot('Candice')

## 
# bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)




#training on english dataset
for files in os.listdir('./english/'):
    data=open('./english/'+files,'r').readlines()
    trainer.train(data)#chat feature
while True:
    message=input('\t\t\tYou:')
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Candice:',reply)
    if message.strip()=='Bye':
        print('Candice: Bye')
        break