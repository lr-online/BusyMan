import httpx
from loguru import logger

import config
from tools import run_only_on_workdays


@run_only_on_workdays
def clock_in_reminder():
    resp = httpx.post(
        url=config.wecom_robot_url,
        json={
            "msgtype": "text",
            "text": {
                "content": "记得上班打卡",
                "mentioned_list": ["@all"],
            },
        },
    )
    assert resp.status_code == 200, resp.text
    logger.info("上班打卡消息已提送")


@run_only_on_workdays
def clock_out_reminder():
    resp = httpx.post(
        url=config.wecom_robot_url,
        json={
            "msgtype": "text",
            "text": {
                "content": "记得下班打卡",
                "mentioned_list": ["@all"],
            },
        },
    )
    assert resp.status_code == 200, resp.text
    logger.info("下班打卡消息已提送")


if __name__ == "__main__":
    clock_in_reminder()
    clock_out_reminder()
