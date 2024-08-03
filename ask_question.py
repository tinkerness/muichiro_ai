# Import the chat_session from app.py
from app import chat_session

def main():
    # Step 3: Read the question from the user
    question = input("Please enter your question: ")

    # Step 4: Pass the question to the send_message function
    response = chat_session.send_message(question)

    # Step 5: Print the response
    print("Response:", response.text)

    # Step 6: Repeat the process until the user types "exit"
    while question.lower() != "exit":
        question = input("Please enter your question: ")
        response = chat_session.send_message(question)
        print("Response:", response.text)

    print("Bye!")

if __name__ == "__main__":
    main()