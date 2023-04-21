import httpx
from loguru import logger

import config
from tools import run_only_on_workdays


@run_only_on_workdays
def weekly_report_reminder():
    resp = httpx.post(
        url=config.wecom_robot_url,
        json={
            "msgtype": "markdown",
            "markdown": {
                "content": """
吉时已到，启动周任务复盘与下周计划


1⃣️请各位老师开始更新及新建 [TAPD任务](https://www.tapd.cn/my_worktable/index/todo) 
2⃣️请各位老师向组长汇报工作内容

>【本周任务进展】
>   1、
>   2、
>   3、


>【下周任务】
>   1、
>   2、
>   3、

>【问题】
>   1、
>   2、
>   3、
    
>【需要配合】
>   1、任务1需要 xx 配合联调、测试
>   2、
>   3、
    
    
>【TapD】甘特图截图
>  图片1.jpg
>  图片2.jpg
"""
            },
        },
    )
    assert resp.status_code == 200, resp.text
    logger.info("周任务更新提醒已发出")


if __name__ == "__main__":
    weekly_report_reminder()
