import random #importing the random library
greetings=["Hey! How can I help you?","Hello!Welcome to our food Ordering Service","Welcome what can I get for you?"] #list of grettings which chatbot can use for responding
menu_items={"pizza":{"name":"pizza","description":"Freshly Baked pizza with your choice of toppings.","price":220},
            "Burger":{"name":"Burger","description":"Juicy chicken burger with fries and drink.","price":490},
            "sushi":{"name":"Sushi","description":"Assorted suhsi rolls with soysauce and wasabi","price":230}} #creating dictionary for menuitems
#defining the possible questions
questions=["What would you like to have?","What would you like to order?","what can I get for you?","would you like to see our menu?"]
#Defining the possible goodbyes
goodbyes=["Thank you for choosing ou food ordering service.Enjoy your meal and have a Great Day!"]
#defining possible responses using dictionary
respones={
    "hello":greetings,
    "hi":greetings,
    "hey":greetings,
    "menu":menu_items,
    "order":questions,
    "what do you recommend":["Our pizza is a customer Favorite!", "You might like our sushi rolls for sure!"],
    "Recommend please":["Our pizza is a customer Favorite!", "You might like our sushi rolls for sure!"],
    "thank you":goodbyes,
    "bye":goodbyes,
    "see you":goodbyes,
    "I like to order pizza":"your order pizza is confirmed",
    "I like to order Burger":"your order Burger is confirmed",
    "I like to order sushi":"your order Sushi is confirmed",
    "pizza":["your order pizza is confirmed"],
    "Burger":["your order Burger is confirmed"],
    "sushi":["your order Sushi is confirmed"],
    "I want to order":questions,



}
#defining a function to generate the chatbot's response
def chatbot_response(user_message):
    #check if the user's message is in the dictionary
    if user_message.lower() in respones:
        if user_message.lower() =="menu":
            menu="Here's our menu:\n"
            for item in menu_items:
                menu+="\n"+menu_items[item]["name"]+"-"+menu_items[item]["description"]+"-"+str(menu_items[item]["price"])
                
            return menu
        else:
            return random.choice(respones[user_message.lower()])
    else:

        return "I am sorry I can't understand What you Said"
#Start the conversation
print("Chatbot: Hi, I'm a Chatbot for our food ordering service.What's your name?")
user_name=input("you: ")
#keep the Conversation going
print("Chatbot: Hi,"+user_name+"! How can I help you today?")
while True:
    user_message=input("you: ")
    if user_message.lower()=="exit":
        print("Chatbot: Thank you for chatting with me. Have a Great day,"+user_name+"!")
        break
    else:
        print("Chatbot:",chatbot_response(user_message))
    


