
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]


num_questions = len(test_results)


correct_answers = 0
for answer in test_results:
   if answer:
      correct_answers += 1

incorrect_answers = num_questions - correct_answers

correct_percentage = (correct_answers / num_questions) * 100


print('TEST STATISTICS')
print('===============')
print('Number of questions:', num_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers: {:.2f}%'.format(correct_percentage))
