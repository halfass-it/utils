import inspect
import datetime
from dataclasses import dataclass


@dataclass
class Error:
  msg: str
  error_msg: str = None

  def __post_init__(self):
    path = inspect.getfile(inspect.currentframe().f_back)
    method = inspect.currentframe().f_back.f_code.co_name
    line = inspect.currentframe().f_back.f_lineno
    self.error_msg = f'[{path}:{method}:{line}]: {self.msg}'

  def __str__(self):
    return self.error_msg

  def __repr__(self):
    return self.error_msg


@dataclass
class CurrentDate:
  date: str = None

  def __post_init__(self):
    self.date = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')

  def __str__(self):
    return self.date

  def __repr__(self):
    return self.date
