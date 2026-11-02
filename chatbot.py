def chatbot_response(user_input):
    # Convert input to lowercase to make it case-insensitive (e.g., "Hello" vs "hello")
    user_input = user_input.lower().strip()
    
    # Rule-based matching using if-elif
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    # Loop to keep the conversation going until the user exits
    while True:
        user_message = input("You: ")
        
        # Get the bot's response
        response = chatbot_response(user_message)
        print(f"Chatbot: {response}")
        
        # Break the loop if the user says goodbye
        if user_message.lower().strip() == "bye":
            break

# Run the chatbot
if __name__ == "__main__":
    start_chat()
