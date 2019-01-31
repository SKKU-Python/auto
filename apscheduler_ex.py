
from apscheduler.schedulers.background import BackgroundScheduler 
from apscheduler.jobstores.base import JobLookupError

import time


def job(): 
	print("I'm working...", "| [time] " 
	, str(time.localtime().tm_hour) + ":" 
	+ str(time.localtime().tm_min) + ":" 
	+ str(time.localtime().tm_sec))

def job_2(): 
	print("Job2 실행: ", "| [time] " 
	, str(time.localtime().tm_hour) + ":" 
	+ str(time.localtime().tm_min) + ":" 
	+ str(time.localtime().tm_sec))
	
	
sched = BackgroundScheduler() 
sched.start()


# cron 사용 - 매 5초마다 job 실행 
# : id 는 고유 수행번호로 겹치면 수행되지 않습니다. 
# 만약 겹치면 다음의 에러 발생 => 'Job identifier (test_1) conflicts with an existing job' 
sched.add_job(job, 'cron', second='*/5', id="test_1")


# cron 으로 하는 경우는 다음과 같이 파라미터를 상황에 따라 여러개 넣어도 됩니다. 
# 매시간 20분 3초에 실행한다는 의미. 
sched.add_job(job_2, 'cron', minute="20", second='3', id="test_2")


	
count = 0 
while count < 4: 
	print("Running main process...............") 
	time.sleep(5) 
	count += 1 
	if count == 3: 
		sched.remove_job("test_1")
		sched.remove_job("test_2")
		print("Kill cron Scheduler")
