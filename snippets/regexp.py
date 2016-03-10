import re

html_source = '''...'''

links = re.findall(
    pattern=r'''<a href=("|')(?P<URL>.*?)\1>(?P<Text>.*?)</a>''',
    string=html_source)

for _, url, text in links:
    print(url, text, sep=': ')
