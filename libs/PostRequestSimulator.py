'''
In this module we simulate form submission from website
'''

class PostRequestSimulator():
    def __init__(self):
        pass

    # simulate post request on server at submit for in website
    def submit_post_request(self):

        while True:
            # generate request dict
            form = {'csrfmiddlewaretoken': 'token', 'sex': [], 'age': [], 'interests': []}

            # initialize feature options
            feature_dict = {'sex': {1: 'Мужской', 2: 'Женский'},
                            'age': {1: '12-17', 2: '18-24', 3: '25-34', 4: '35-44',
                                    5: '45-54', 6: '55-64', 7: '65+'},
                            'interests': {1: 'Кулинария', 2: 'Наука', 3: 'Спорт', 4: 'Активный отдых',
                                    5: 'Музыка и песни', 6: 'Творчество', 7: 'Психология и саморазвитие',
                                    8: 'Природа и садоводство', 9: 'Настольные и видеоигры', 10: 'Мода и шоппинг',
                                    11: 'Красота и здоровье', 12: 'Алкоголь', 13: 'Бизнес и инвестиции',
                                    14: 'Техника и ремонт', 15: 'Фильмы и сериалы', 16: 'Книги и комиксы',
                                    17: 'Фото и видео', 18: 'Коллекционирование', 19: 'Ведение блога',
                                    20: 'Не знаю'}}

            # sex radio box
            sex_inp = input("Выбери пол:\n1 - Мужской\n2 - Женский\n")
            try:
                sex_inp = int(sex_inp)
                form['sex'].append(feature_dict['sex'][sex_inp])
            except:
                print("Вводи числа из списка!")

            # age radio box
            age_inp = input(
                "Выбери возраст:\n1 - 12-17\n2 - 18-24\n3 - 25-34\n4 - 35-44\n5 - 45-54\n6 - 55-64\n7 - 65+\n")
            try:
                age_inp = int(age_inp)
                form['age'].append(feature_dict['age'][age_inp])
            except:
                print("Вводи числа из списка!")

            # interests checkbox
            interests_inp = input(
                "Выбери интересы (для ввода нескольких вариантов используй запятую)\n Пример ввода: 1,3,12,13:\n1 - Кулинария\n2 - Наука\n3 - Спорт\n4 - Активный отдых\n5 - Музыка и песни\n6 - Творчество\n7 - Психология и саморазвитие\n8 - Природа и садоводство\n9 - Настольные и видеоигры\n10 - Мода и шоппинг\n11 - Красота и здоровье\n12 - Алкоголь\n13 - Бизнес и инвестиции\n14 - Техника и ремонт\n15 - Фильмы и сериалы\n16 - Книги и комиксы\n17 - Фото и видео\n18 - Коллекционирование\n19 - Ведение блога\n20 - Не знаю\n")
            interests_inp = interests_inp.split(',')
            for i in interests_inp:
                try:
                    i = int(i)
                    form['interests'].append(feature_dict['interests'][i])
                except TypeError:
                    print("Вводи числа из списка!")

            print('Форма отправлена')
            return form

    # convert dict from request to list with feature
    def request_to_feature_list(self, form):

        body_post = list()
        body_post.append(form['sex'])
        body_post.append(form['age'])

        for i in form['interests']:
            body_post.append(i)

        if 'Не знаю' in body_post:
            body_post.remove('Не знаю')

        return body_post