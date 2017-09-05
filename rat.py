import requests
import datetime


id = int(input('Введите id: '))
gitlabUrl = 'https://gitlab.com/api/v4/users/{0}/events'.format(id)
r = requests.get(gitlabUrl).json()

date_list = []
for item in r:
    item = item['created_at']
    date = item.rsplit('T', 1)[0]
    date_list.append(date)


now_date = datetime.date.today()
start = now_date - datetime.timedelta(days=1)
delta = datetime.timedelta(days=7)
end = start - delta

week_list = []
while end<start:
    end = end + datetime.timedelta(days=1)
    date = end
    date = str(date)
    week_list.append(date)


for item in week_list:
    commits = date_list.count(item)
    print(item, commits)
