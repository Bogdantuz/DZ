from pprint import pprint

from requests import get
from bs4 import BeautifulSoup as Bs
from pandas import DataFrame
from sqlalchemy import create_engine


def main():
    url = 'https://yermilovcentre.org/medias/?page=1'
    r = get(url)
    soup = Bs(r.text, 'html.parser')

    def count_of_page():
        span_of_page = soup.select_one(
            'span.f100x20px.mx-5.d-none.d-sm-block'
        ).text
        slesh = span_of_page.find('/')
        result = int(
            span_of_page[slesh:].replace('/', '')
        )
        return result

    index_obj_in_result = 1
    result = {}
    for page in range(count_of_page()):
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

            result[index_obj_in_result] = {
                'name': f'{text}',
                'href': f'{href}'
            }
            index_obj_in_result += 1

        url = f'https://yermilovcentre.org/medias/?page={str(page + 2)}'

    return result


def to_database(content: dict):
    df = DataFrame.from_dict(content, orient='index')
    engine = create_engine("sqlite:///output.db")
    df.to_sql('main', con=engine)


if __name__ == '__main__':
    # Виведення назв та посиланнь на новин
    pprint(main())

    # Створення бази данних на основі цих данних
    to_database(main())