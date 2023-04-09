from datetime import datetime

from loguru import logger
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

from actions.send_wecom_msg import weekly_report_reminder
from actions.clock_in import clock_in_reminder, clock_out_reminder

app = FastAPI()


@app.get("/")
def self_introduction():
    return {"name": "BusyMan", "version": "20230409"}


@app.get("/jobs")
def get_weather():
    jobs = app.state.scheduler.get_jobs()
    for job in sorted(jobs, key=lambda x: x.next_run_time):
        yield {
            "name": job.name,
            "next_run_time": job.next_run_time,
        }


@app.on_event("startup")
def shutdown_event():
    app.state.scheduler = BackgroundScheduler()

    logger.info("已生成定时任务调度器")

    # 每天提醒上下班打卡
    app.state.scheduler.add_job(clock_in_reminder, "cron", hour=9, minute=55)
    app.state.scheduler.add_job(clock_out_reminder, "cron", hour=19)

    # 周五下午提醒写周报
    app.state.scheduler.add_job(
        weekly_report_reminder, "cron", day_of_week="fri", hour="14,16,18"
    )

    app.state.scheduler.start()
    logger.info("已启动定时任务调度器")


@app.on_event("shutdown")
def shutdown_event():
    app.state.scheduler.shutdown()
    logger.info("已关闭定时任务调度器")
