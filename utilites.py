import json

def load_candidates():
    '''
    загрузит данные из файла
    '''
    # загрузить из json
    with open('candidates.json', 'r', encoding='utf-8') as file:  # открываем файл на чтение
        data = json.load(file)  # загружаем из файла данные в словарь data
        return data


def get_all():
    """
    покажет всех кандидатов
    :return: результат load_candidates
    """
    return load_candidates()

def get_by_pk(pk):
    '''
    :param pk: для того, чтобы вывести кандидата по введенному pk - порядковому номеру
    :return: вернет кандидата по pk
    '''
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return

# def get_by_skill(skill_name):
#     '''
#     :param skill_name: навык
#     :return:которая вернет кандидатов по навыку
#     '''
#     # candidates = []
#     # for candidate in load_candidates():
#     #     if skill_name.lower() in candidate['skills'].lower().split(', '):
#     #         candidates.append(candidate)
#     #         return candidates

def get_by_skill(skill):
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(", ")
        if skill in skills:
            result.append(candidate)
    return result
