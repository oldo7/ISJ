def gen_quiz(qpool, *indexes, altcodes="ABCDEF", quiz=None):
    if quiz == None:
        quiz = []
    for index in indexes:
        answers = []
        if index >= len(qpool):
            print("Ignoring index ", index, " - list index out of range")
            continue
        for i in range(0,min(len(altcodes), len(qpool[index][1]))):
            answers.append(altcodes[i] + ": " + qpool[index][1][i])
        quiz.append((qpool[index][0], answers))
    return quiz