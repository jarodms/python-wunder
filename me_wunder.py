from myconfig import *
import time, datetime
import wunderpy2

api = wunderpy2.WunderApi()
client = api.get_client(access_token, client_id) 


task_desc = input('Enter the task: ')
task_time = input('Days from now (optional YYYY-MM-DD): ')

if len(task_time) == 0:
	task = client.create_task(list_id, task_desc)
else:
	if len(task_time) <= 2:
		now = datetime.datetime.now()
		now_plus_days = now + datetime.timedelta(days = int(task_time))
		task_time = now_plus_days.strftime('%Y-%m-%d')

	task = client.create_task(list_id, task_desc, due_date=task_time)

