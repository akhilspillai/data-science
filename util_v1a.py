import re

def format_data(row):
  message = row["message"]
  punct = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\t\n'
  message = message.split()
  return message