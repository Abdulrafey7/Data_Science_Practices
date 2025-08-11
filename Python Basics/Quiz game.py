
Questions = ("1. What is the capital of Australia?",
             "2. Which planet is known as the \"Evening Star\"?" ,
             "3. What is the chemical symbol for gold?" ,
             "4. What is the largest ocean on Earth?" )

Options = [("(a) Sydney ", "(b) Melbourne" , "(c) Canberra" , "(d) Perth"),
           ("(a) Mars" , "(b) Saturn" , "(c) Venus" , "(d) Jupiter"),
           ("(a) Ag" , "(b) Fe" , "(c) Au" , "(d) Cu"),
           ("(a) Pacific Ocean","(b) Atlantic Ocean" , "(c) Indian Ocean" , "(d) Arctic Ocean")]

Correct = ("C","C","C","C")

Answers = []

no = 0

Score = 0

for question in Questions:
    print("-----------------------------------------------------")
    print(question)
    for option in Options[no]:
        print(option)

    answer = input("Enter your answer: (A,B,C,D)").upper()
    Answers.append(answer)
    if answer == Correct[no]:
        Score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    no+=1

print("-----------------------------------------------------")
print("                      Result")
print("-----------------------------------------------------")

print("Correct Answers: ",end=" ")
for answer in Answers:
    print(answer,end=" ")

print()
print("Your Answers: ",end=" ")
for answer in Answers:
    print(answer,end=" ")

Score = Score/len(Answers) * 100
print()
print(f"Your Score: {Score}%")





