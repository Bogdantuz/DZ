from pprint import pprint
from time import time

from requests import get
from bs4 import BeautifulSoup as Bs
# from pandas import DataFrame
# from sqlalchemy import create_engine


start = time()

class Vals:
    index_obj_in_result = 1
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

        page += 1
        url = f'https://yermilovcentre.org/medias/?page={page}'

    return Vals.result



# def to_database(content: dict):
#     df = DataFrame.from_dict(content, orient='index')
#     engine = create_engine("sqlite:///output.db")
#     df.to_sql('main', con=engine)


if __name__ == '__main__':
    # Виведення назв та посиланнь на новин
    pprint(main())

    end = time()
    res = end - start
    print(res)

    # Створення бази данних на основі цих данних
    # to_database(main())