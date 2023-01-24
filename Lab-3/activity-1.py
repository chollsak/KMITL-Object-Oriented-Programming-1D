def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    average_score = sum([score for subject, score in subject_score.items()]) / len(subject_score)
    return "{:.2f}".format(average_score)


print(add_score({"python" : 50}, "calculus", 60))
print(calc_average_score({"python" : 50, "calculus" : 60}))




