import os
import sys
from src.logger import logging


def error_detailed(error, error_detail: sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python Script name [{0}] Line No. [{1}] Error Message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_detailed(error_message, error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divided by 0")
        raise CustomException(e, sys)
