import requests
import datetime


def info():
    nick = str(input('Введите nick пользователя на gitlab.com: '))
    user_link = 'https://gitlab.com/api/v4/users?username={0}'.format(nick)
    id = requests.get(user_link).json()[0]['id']
    gitlab_url = 'https://gitlab.com/api/v4/users/{0}/events'.format(id)
    r = requests.get(gitlab_url).json()

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
    key = '2'  # Наш ключ в trello.com
    token = ''  # Наш токен в trello.com

    querystring = {'text': text,
                   'key': key,
                   'token': token
                   }

    response = requests.request("POST", url, params=querystring)  # Запрос на добавления комментария в карточку
    return response

send(info)
