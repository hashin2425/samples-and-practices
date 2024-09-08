""" 1分ごとにログを書き込む関数
"""


import logging
import azure.functions as func

app = func.FunctionApp()


def main(timerTriggeredAnalyzer: func.TimerRequest) -> None:
    try:
        logging.info("Python timer trigger function processed a request.")
        logging.info(timerTriggeredAnalyzer)
    except Exception as e:  # pylint: disable=broad-except
        logging.error(e)
