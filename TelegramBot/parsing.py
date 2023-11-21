from threading import Thread
from pprint import pprint
from random import randint

from requests import get, Session
from bs4 import BeautifulSoup as Bs


class ParsingFilm:
    result = []

    def __init__(self, url, all_elements, one_element) -> None:
        ParsingFilm.result = []
        self.url = url
        self.one_element = one_element
        r = get(url)
        soup = Bs(r.content, "html.parser")
        films = soup.select(all_elements)

        procs = []
        for film in films:
            t = Thread(target=ParsingFilm.get_inf, args=(self, film,))
            procs.append(t)
            t.start()

        for proc in procs:
            proc.join()

    def get_inf(self, film):
        film = film.select_one(self.one_element)
        if film:
            ParsingFilm.result.append({
                "name": film.text.replace('\n', ''),
                "href": f"{self.url}{film.get('href')}"
            })


class ParsingMusic:
    result = []

    def __init__(self, url, all_elements, one_element) -> None:
        ParsingMusic.result = []
        self.one_element = one_element
        count = randint(1, 300)
        limit = count+1
        with Session() as s:
            while True:
                new_url = f'{url}&page={count}'
                r = s.get(new_url)
                soup = Bs(r.content, "html.parser")
                if soup.select_one(
                    'div.flex.flex-col.w-full > h2'
                ) or count==limit:
                    break
                films = soup.select(all_elements)

                procs = []
                for film in films:
                    t = Thread(target=ParsingMusic.get_inf, args=(self, film,))
                    procs.append(t)
                    t.start()

                for proc in procs:
                    proc.join()

                count += 1


    def get_inf(self, film):
        film = film.select_one(self.one_element)

        if film:
            name = film.text.replace('\n', '')
            href = f"{film.get('href')}"[:-1]

            to_delete = 'https://freemusicarchive.org/music/'
            href = href[href.find(to_delete) + len(to_delete):]

            ParsingMusic.result.append({
                "name": name,
                "href": href
            })
            

if __name__ == '__main__':
    musics_args = [
        "https://freemusicarchive.org/search/?search-genre=Jazz",
        "div.w-full.flex.flex-col.gap-3.pt-3 > div",
        "a.font-bold"
    ]
    musics = ParsingMusic(
        musics_args[0], musics_args[1], musics_args[2]
    ).result
    pprint(musics)