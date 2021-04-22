from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="america/sao_paulo")

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=20)
def scheduled_job():
    print('Postou.')

sched.start()