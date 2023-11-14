import os
from pandas import DataFrame, read_excel


if os.path.exists('ExcelFile/Diary.xlsx'):
    df = read_excel('ExcelFile/Diary.xlsx')
    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

elif os.path.exists('Diary.xlsx'):
    df = read_excel('Diary.xlsx')
    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

else:
    base = {
        'Math': [12, 11, 12, 10],
        'Python': [100, 100, 100, 100],
        'English': [8, 9, 7, 8]
    }
    df = DataFrame(base)

print(df.to_string())


def pdf():
    print(df)

def add(math = None, python = None, english=None):
    colums = ['Math', 'Python', 'English']
    ind = len(df)
    if math or python or english:
        for i in colums:
            df.loc[ind, i] = locals()[i.lower()]
    else:
        for i in colums:
            inf = input(f'{i}: ')

            if inf != '':
                df.loc[ind, i] = inf

            else:
                df.loc[ind, i] = None


def drop(ind):
    df.drop(int(ind), inplace=True)

def change(ind = None, colm = None, val = None):
    vals = {}
    if not(ind or colm or val):
        sysname = ['ind', 'colm', 'val']
        realname = ['Index', 'Column', 'Value']
        for i in realname:
            inp = f"{input(f'{i}: ')}"
            vals[sysname[realname.index(i)]] = f"{inp}"
    else:
        vals = {'ind': ind, 'colm': colm, 'val': val}
        
    try:
        vals['colm'] = list(df.columns).index(vals['colm'])
    except ValueError:
        pass
    df.iloc[int(vals['ind']), int(vals['colm'])] = vals['val']


print()
while True:
    try:
        text = input('>>> ')
    except KeyboardInterrupt:
        print('exit')
        break

    if text == 'exit':
        break

    comands = ['pdf', 'add', 'drop', 'change']
    if text in comands:
        text = f"{comands[comands.index(text)]}()"
    elif ' ' in text:
        if len(text.rsplit(' ')) >= 3:
            name = text.rsplit(' ')[0]
            arg = text.rsplit(' ')[1:]
        else:
            name, arg = text.rsplit(' ')
        if name in comands:
            if isinstance(arg, list):
                text = f'{name}('
                for ar in arg:
                    text = f'{text}"{ar}",'
                text = f'{text})'
            else:
                text = f'{name}("{arg}")'
    
    exec(text)


df.to_excel("ExcelFile/Diary.xlsx")