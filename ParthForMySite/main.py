import sys
from time import sleep

# pip install rich
from rich import print
from bs4 import BeautifulSoup


with open(
    'ParthForMySite/index.html', # index.html
    encoding='utf-8'
) as file:
    bs = BeautifulSoup(file.read(), 'html.parser')

print()
print(f'[bold]{bs.select_one("h1").text}[/bold]')
print()
print(f'[underline]{bs.select_one("p#some-text").text}[/underline]')
print()
print(f'[cyan]{bs.select("p")[1].text}[/cyan]')

for i in bs.select_one('ul'):
    if i != '\n':
        print(f'    [cyan]•[/cyan] {i.text}')

print()

colors = ['green', 'blue', 'red', 'pink', 'purple', 'cyan']
try:
    while True:
        for color in colors:
            print(f'[{color}]{bs.select("p")[-1].text}[/{color}]')
            sleep(0.15)
            
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
except KeyboardInterrupt:
    pass