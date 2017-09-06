import requests
import datetime


def info():
    id = int(input('Введите id пользователя на gitlab.com: '))  # ID Пользователя на gitlab.com
    gitlabUrl = 'https://gitlab.com/api/v4/users/{0}/events'.format(id)  # URL на события
    r = requests.get(gitlabUrl).json()

    date_list = []
    for current_date in r:
        current_date = current_date['created_at']
        date = current_date.rsplit('T', 1)[0]
        date_list.append(date)


    now_date = datetime.date.today()
    start = now_date - datetime.timedelta(days=1)
    delta = datetime.timedelta(days=7)
    end = start - delta

    week_list = []
    while end < start:
        end = end + datetime.timedelta(days=1)
        date = end
        date = str(date)
        week_list.append(date)

    daily_commits = []
    for current_date in week_list:
        commit = date_list.count(current_date)
        if commit:
            info = ['за', current_date, 'коммитов было-', commit]
            daily_commits.append(info)
        else:
            info = ['за', current_date, 'коммитов не было']
            daily_commits.append(info)
    return daily_commits
info = info()
print(info)


def send(info):
    idCard = input('Введите id карточки на trello.com: ')  # ID Нашей карточки в trello.com. Пример 59ae5dfc529cc2277f6a75bd или la8gztsN
    url = ("https://api.trello.com/1/cards/{0}/actions/comments").format(idCard)  # URL на добавления комментария в карточку

    text = info
    key = '93f7cc27bf5ab965fc4eea3abe8f2912'  # Наш ключ в trello.com
    token = 'b6800f56453309ac1ddd91dafe05fc3c8a69192d0fae45fb57342ae782d53aa0'  # Наш токен в trello.com

    querystring = {'text': text,
                   'key': key,
                   'token': token
                   }

    response = requests.request("POST", url, params=querystring)  # Запрос на добавления комментария в карточку
    return response

send(info)