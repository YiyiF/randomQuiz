#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data.
capitals = {'Alabama': 'Montgomery', 'New Jersey': 'Trenton', 'Texas': 'Austin', 'Montana': 'Helena', 'New York': 'Albany', 'Washington': 'Olympia'}

# TODO: One more step. Get states and capitals from file.

# Generate 5 quiz files.
for quizNum in range(5):
    # Create the quiz and answer key files.
    quizFile = open('capitalquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' ' * 20 + 'State Capitals Quiz (Form %s)\n' % (quizNum + 1))

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through 6 states, making a question for each.
    for questionNum in range(6):

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the questions and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()