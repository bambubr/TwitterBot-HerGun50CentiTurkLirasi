from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="Europe/Istanbul")

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10)
def scheduled_job():
    print('Exec 1000...')
    exec(open('HerGun50CentiTurkLirasi.py').read())

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=18)
def scheduled_job():
    print('Exec 1800...')
    exec(open('HerGun50CentiTurkLirasi.py').read())

sched.start()
