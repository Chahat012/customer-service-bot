import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... Please ask your question.")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Please speak again.")
    except sr.RequestError:
        speak("Internet issue detected. Please try again later.")
    return ""

def show_commands():
    commands = [
        "Hello / Hi / Greetings: General greeting",
        "Order Status / Track my order: For order tracking",
        "Product info / Tell me about product: For product details",
        "Customer care / Talk to support: To contact support",
        "Return policy / Refund: For return and refund information",
        "Thank you: To say thanks",
        "Help: To know what I can do",
        "Bye / Exit: To stop the bot"
    ]
    speak("Here are some things you can ask me:")
    for c in commands:
        speak(c)

def process_command(command):
    command = command.lower()
    # Greetings
    if any(greet in command for greet in ["hello", "hi", "greetings"]):
        speak("Hello! How can I assist you today?")
    # Order status
    elif any(word in command for word in ["order status", "track my order", "order track", "where is my order"]):
        speak("Please provide your order ID. I will check the status for you.")
    # Product Info
    elif any(word in command for word in ["product info", "tell me about product", "product details"]):
        speak("Which product would you like information about?")
    # Customer Support
    elif any(word in command for word in ["customer care", "support", "contact support", "customer service"]):
        speak("Connecting you to our customer support. Please wait.")
    # Return Policy
    elif any(word in command for word in ["return policy", "refund", "how to return", "exchange"]):
        speak("Our return policy allows returns within 7 days of delivery. For a refund or exchange, please share your order details.")
    # Thanks
    elif any(word in command for word in ["thank you", "thanks"]):
        speak("You're welcome! Let me know if you need anything else.")
    # Help
    elif "help" in command:
        show_commands()
    # Exit
    elif any(word in command for word in ["bye", "exit", "quit", "close"]):
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak("Sorry, I don't have information on that topic. Say 'help' to know what I can do.")
    return True

# Main loop
while True:
    user_command = listen()
    if user_command:
        if process_command(user_command) == False:
            break
