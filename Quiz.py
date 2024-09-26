def display_question(question):
    print(question['question'])
    for option in question['options']:
        print(option)

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def run_quiz(questions):
    score = 0
    for question in questions:
        display_question(question)
        user_answer = input("Your Answer: ").strip().upper() 
        if check_answer(user_answer, question['answer']):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
        print() 

    print(f"Your total score is {score}/{len(questions)}")

if __name__ == "__main__":
    questions = [ 
        {
            "question": "What is the distance between Mandi and Gujrat?",
            "options": ["A) 80km", "B) 90km", "C) 100km", "D) 77.2km"],
            "answer": "D"
        },
        {
            "question": "What is the capital of India?",
            "options": ["A) Hyderabad", "B) Delhi", "C) Bangalore", "D) New Delhi"],
            "answer": "D"
        }, 
    {
        "question": "What is a traditional drink in Pakistan often served during hot weather?",
        "options": ["A) Lassi", "B) Coffee", "C) Lemonade", "D) Tea"],
        "answer": "A"
    },
    {
        "question": "Which VIP bus service is known for its luxury travel in Pakistan?",
        "options": ["A) Daewoo", "B) Faisal Movers", "C) Skyways", "D) Pakistan Railways"],
        "answer": "A"
    },
    {
        "question": "What is the traditional dress for women in Pakistan?",
        "options": ["A) Sari", "B) Shalwar Kameez", "C) Anarkali", "D) Lehenga"],
        "answer": "B"
    },
    {
        "question": "Arfa Karim Tower in Lahore is named after which young software prodigy?",
        "options": ["A) Malala Yousafzai", "B) Arfa Karim", "C) Aisha Khan", "D) Fatima Jinnah"],
        "answer": "B"
    },
    {
        
    "question": "Where is the Alpac Cancer Centre located?",
    "options": ["A) Faisalabad", "B) Lahore", "C) Karachi", "D) Islamabad"],
    "answer": "A"


    },
    {
        "question": "Where does the Orange Metro Train operate?",
        "options": ["A) Lahore", "B) Islamabad", "C) Karachi", "D) Faisalabad"],
        "answer": "A"
    },
    {
        "question": "What is the famous sweet dish made from milk and sugar in Pakistan?",
        "options": ["A) Gulab Jamun", "B) Barfi", "C) Kheer", "D) All of the above"],
        "answer": "D"
    },
    {
        "question": "Which city is known as the 'City of Gardens' in Pakistan?",
        "options": ["A) Lahore", "B) Karachi", "C) Islamabad", "D) Peshawar"],
        "answer": "A"
    },
]

    
    run_quiz(questions)  
