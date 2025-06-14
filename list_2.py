def introduction():
	print("WELCOME TO QUIZ CHALLENGE ")
	print("LET ME KNOW YOUR IQ")
	time.sleep(1)  # it is used to stop the program for 1 second and it is in the predefined module time
	
quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Andhrapradesh", "B) Telangana", "C) Newdelhi", "D) Chattisgarh"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    }
]

def running_quiz():
	score = 0
	question_num = 1
	for x in quiz_questions:	
		print("\nQuestion", question_num, ":",x['question'])
running_quiz()