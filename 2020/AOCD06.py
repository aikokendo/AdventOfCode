from classes.helper import Helper
from classes.seat import Seat

def parseFiletoQuestionnairesSol1(file_data):
    questionnaires = file_data.split('\n\n')
    qSets = []
    qCount = []
    for questionnaire in questionnaires:
        qSet = set()
        [qSet.add(q) for q in questionnaire if q != '\n']
        qSets.append(qSet)
        qCount.append(len(qSet))
    return qSets,qCount


def parseFiletoQuestionnairesSol2(file_data):
    questionnaires = file_data.split('\n\n')
    qSets = []
    qCount = []
    for questionnaire in questionnaires:
        persons = questionnaire.split('\n')
        for index, person in enumerate(persons):
            if index == 0:
                qPerson = set()
                [qPerson.add(q) for q in person]
            else:
                qPerson2 = set()
                [qPerson2.add(q) for q in person]
                qPerson = qPerson.intersection(qPerson2)
        qSets.append(qPerson)
        qCount.append(len(qPerson))
    return qSets, qCount


#inputs
file_name = 'input\inputd06.txt'

file = Helper.read_file(file_name)
questionnaires = parseFiletoQuestionnairesSol1(file)
print('Part 1 solution:', sum(questionnaires[1]))

questionnaires = parseFiletoQuestionnairesSol2(file)
print('Part 2 solution:', sum(questionnaires[1]))
