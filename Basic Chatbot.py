def simple_chatbot():
   print("Chatbot: Hi there! How can I help you today? (Type 'bye' to exit)")
   with open("chat_log.txt", "a") as file:
        file.write("Chatbot: Hi there! How can I help you today? (Type 'bye' to exit)\n")
        while True:
            user_input = input("You: ").lower()
            file.write(f"You: {user_input}\n")

            if user_input == "hello":
                response = "Hi!"
            elif user_input == "how are you":
                response = "I'm fine, thanks for asking!"
            elif user_input == "what is your purpose":
                response = "My purpose is to demonstrate a basic chatbot for the CodeAlpha internship."
            elif user_input == "bye":
                response = "Goodbye! Have a great day!"
                print(f"Chatbot: {response}")
                file.write(f"Chatbot: {response}\n")
                break
            else:
                response = "I'm sorry, I don't understand that. Can you rephrase?"

            print(f"Chatbot: {response}")
            file.write(f"Chatbot: {response}\n")
if __name__ == "__main__":
    simple_chatbot()
