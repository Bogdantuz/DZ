from random import randint

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = 'https://docs.google.com/spreadsheets/d/1VCs1xa5tZvnmjAx7nhtx-OsdDokZwg7w8son32ot9i4/edit#gid=0'
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds = ServiceAccountCredentials.from_json_keyfile_name('.secret/SekretKey.json', scopes=scopes)
client = gspread.authorize(credentials=creds)
data = client.open_by_url(url)


# workstem = data.add_worksheet('Home Work', 1000, 1000)
workstem = data.get_worksheet(3)

count = 2
months = ['Cічень', 'Лютий', 'Березень',
    'Квітень', 'Травень', 'Червень',
    'Липень', 'Серпень', 'Вересень',
    'Жовтень', 'Листопад', 'Грудень'
]
df = pd.DataFrame({
    'Month': months*count,
    'Math': [randint(1, 10) for a in months*count],
    'UA': [randint(0, 8) for b in months*count],
    'Biology': [randint(1, 9) for c in months*count]
})

workstem.clear()
workstem.update(
    [df.columns.values.tolist()] + df.values.tolist()
)


sns.lineplot(df)

plt.xlabel('Month')
plt.ylabel('Hours')

plt.show()