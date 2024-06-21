import inspect
import datetime
from dataclasses import dataclass


from dataclasses import dataclass, field
import inspect
import traceback
from typing import Optional

@dataclass
class Error:
    msg: str
    error_type: Optional[str] = None
    stacktrace: Optional[str] = None
    error_msg: str = field(init=False)

    def __post_init__(self):
        caller_frame = inspect.currentframe().f_back
        file_path = inspect.getfile(caller_frame)
        method_name = caller_frame.f_code.co_name
        line_number = caller_frame.f_lineno
        if self.error_type is None:
            self.error_type = "GenericError"
        if self.stacktrace is None:
            self.stacktrace = ''.join(traceback.format_stack()[:-1])
        self.error_msg = (
            f"[ERROR] {self.error_type}: {self.msg}\n"
            f"Location: {file_path}:{method_name}:{line_number}\n"
            f"Stacktrace:\n{self.stacktrace}"
        )

    def __str__(self):
        return self.error_msg

    def __repr__(self):
        return f"Error(msg='{self.msg}', error_type='{self.error_type}')"

@dataclass
class CurrentDate:
  date: str = None

  def __post_init__(self):
    self.date = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')

  def __str__(self):
    return self.date

  def __repr__(self):
    return self.date
