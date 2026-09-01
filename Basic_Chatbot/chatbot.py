# Basic Rule-Based Chatbot

print("Welcome to Basic Chatbot!")
print("You can type: hello, how are you, thanks, bye")

while True:
    user_input = input("\nYou: ").lower()
    if user_input == "hello":
        print("Bot: Hi!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input == "thanks":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
