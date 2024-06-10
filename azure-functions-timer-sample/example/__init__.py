import logging
import time

import azure.functions as func

app = func.FunctionApp()


def main(timerTriggeredAnalyzer: func.TimerRequest) -> None:
    message = f"Python timer trigger function ran at {time.time()}. Timer fired at {timerTriggeredAnalyzer.get('firedAt')}"
    logging.info(message)
    return
