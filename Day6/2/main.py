a = open('input.txt', 'r')
data = a.readlines()
a.close()
import copy
allSumCount = 0
currentPersonAnswers = []
currentGroupAnswers = []
allGroupAnswers = []
for line in data:
    if line == "\n": # If it's only a new line, start a new group next time 
        allGroupAnswers.append(copy.deepcopy(currentGroupAnswers))
        currentPersonAnswers = []
        currentGroupAnswers = []
        continue 
    line.replace('\n', '')
    line.replace(' ', '')
    for char in line:
        if char == " " or char == "\n":
            continue
        currentPersonAnswers.append(char)
    currentGroupAnswers.append(copy.deepcopy(currentPersonAnswers))
    currentPersonAnswers = []

if len(currentGroupAnswers) > 0:
    allGroupAnswers.append(copy.deepcopy(currentGroupAnswers))
    currentGroupAnswers = []
    currentPersonAnswers = []

for group in allGroupAnswers:
    # print("--group--")
    # print(group)
    answers = []
    answersCounted = []
    personCount = 0
    for person in group:
        personCount+=1
        for answer in person: 
            answers.append(answer)
    # print("Answers: ", answers)
    for answer in answers:
        if answer in answersCounted:
            continue 
        # print("Current answer: ", answer)
        # print("Answer Count: ", answers.count(answer))
        # print("People: ", personCount)
        answersCounted.append(answer)
        if answers.count(answer) == personCount:
            # print("All people in this group had the answer: ", answer)
            allSumCount += 1

print("Answer > ", allSumCount)


    


