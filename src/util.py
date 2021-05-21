import re

def clean(raw_html):
  cleanr = re.compile('[^a-zA-Z., ]')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext.lstrip().rstrip()