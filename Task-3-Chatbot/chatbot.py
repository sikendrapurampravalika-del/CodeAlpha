import datetime
import random

WELCOME_MESSAGES = [
    "Hello! I am your chatbot.",
    "Hi there! Ready to chat.",
    "Welcome! Ask me anything."
]

GOODBYE_MESSAGES = [
    "Goodbye!",
    "See you later!",
    "Thanks for chatting."
]

JOKES = [
    "Why did the computer show up at work late? It had a hard drive.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "How do you comfort a JavaScript bug? You console it."
]


def get_response(message: str) -> str:
    text = message.strip().lower()
    if not text:
        return "Please type a question or a message."

    if text in {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}:
        return random.choice(WELCOME_MESSAGES)

    if text in {"bye", "exit", "quit", "goodbye"}:
        return random.choice(GOODBYE_MESSAGES)

    if "help" in text:
        return (
            "I can answer simple questions. Try asking about the time, date, or for a joke. "
            "Type 'exit' to quit."
        )

    if "time" in text:
        now = datetime.datetime.now()
        return f"The current time is {now:%H:%M:%S}."

    if "date" in text:
        today = datetime.date.today()
        return f"Today's date is {today:%B %d, %Y}."

    if "joke" in text:
        return random.choice(JOKES)

    if "your name" in text or "who are you" in text:
        return "I am a simple chatbot built in Python."

    if "weather" in text:
        return "I cannot fetch live weather yet, but I can help with other questions."

    if "stock" in text:
        return "I am a chatbot. For stock data, run the stock tracker script."

    return "Sorry, I don't know the answer to that yet. Try asking for time, date, a joke, or type 'help'."


def main():
    print("Chatbot is ready. Type 'help' for instructions and 'exit' to quit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Bot: {response}")
        if user_input.strip().lower() in {"bye", "exit", "quit", "goodbye"}:
            break


if __name__ == "__main__":
    main()
