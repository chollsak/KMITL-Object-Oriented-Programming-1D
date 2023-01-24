subject_score = {"65010001" : {"python" : 50}, "65010002" : {"python" : 50, "calculus" : 60}}

def add_score(subject_score, student, subject, score):
    if student not in subject_score.keys() :
        subject_score[student] = {subject : score}
    else :
        subject_score[student][subject] = score
    return subject_score 

def calc_average_score(subject_score):
    average_score = {student_id : "{:.2f}".format(sum([score for subject, score in all_score.items()]) / len(all_score)) for student_id, all_score in subject_score.items()}
    return average_score


print(add_score(subject_score, "65010001", "calculus", 70))
print(calc_average_score(subject_score))