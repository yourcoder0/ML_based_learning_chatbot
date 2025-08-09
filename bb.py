from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

response = chatbot.get_response("Hello, how are you today?")
print(response)