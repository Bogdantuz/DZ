from threading import Thread
from pprint import pprint
from time import time

from requests import get
from bs4 import BeautifulSoup as Bs

start = time()


class Vals:
    index_obj_in_result = 1
    to_do = []
    result = {}

def main():
    page = 1
    url = f'https://yermilovcentre.org/medias/?page={page}'
    while True:
        r = get(url)
        soup = Bs(r.text, 'html.parser')

        button_to_next_page = soup.select(
            'div.row.justify-content-center.align-items-center > a'
        )[1].get('class')[0]

        if button_to_next_page == 'g-arrow-active-right':
            Vals.to_do.append(soup)
        else:
            Vals.to_do.append('End')
            break

        page += 1
        url = f'https://yermilovcentre.org/medias/?page={page}'


Thread(target=main).start()

while True:
    if Vals.to_do:
        soup = Vals.to_do[0]

        if not soup == 'End':
            all_videos = soup.select(
                'div.row.no-gutters.justify-content-left.father-for-small-media > div'
            )

            for one in all_videos:
                video = one.select_one('a.row.title-text.mx-0.pt-3.pb-2')

                text = video.text.replace(
                    '\n                        ',
                    ''
                ).replace(
                    '\n                    ',
                    ''
                )
                href = f"https://yermilovcentre.org{video.get('href')}"

                Vals.result[Vals.index_obj_in_result] = {
                    'name': f'{text}',
                    'href': f'{href}'
                }
                Vals.index_obj_in_result += 1

        else:
            break

        Vals.to_do.pop(0)


if __name__ == '__main__':
    pprint(Vals.result)
    end = time()
    res = end - start
    print(res)