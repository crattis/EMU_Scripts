import random

for num in range(0,1):
    count= 0
    questions = []
    with open('2019_midterm.txt', mode='r') as f:
        lines = f.readlines()
        while count < 25:
            exam_question = random.choice(lines)
            if exam_question not in questions:
                questions.append(exam_question)
                count += 1
    with open('exam_' + str(num)+'.txt', mode='w') as output:
        for x in (questions):
            output.write(x + '\n')
