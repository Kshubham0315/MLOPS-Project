import sys
import logging
from types import ModuleType


def error_message_detail(error: Exception, error_detail: ModuleType) -> str:
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in python script: "
        f"[{file_name}] at line number [{line_number}] "
        f"error message: {error}"
    )


class MyException(Exception):

    def __init__(self, error_message: str, error_detail: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message_detail(self, error_detail)

    def __str__(self):
        return self.error_message