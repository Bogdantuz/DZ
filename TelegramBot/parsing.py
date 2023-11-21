from threading import Thread

from requests import get
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
        self.url = url
        self.one_element = one_element
        r = get(url)
        soup = Bs(r.content, "html.parser")
        films = soup.select(all_elements)

        procs = []
        for film in films:
            t = Thread(target=ParsingMusic.get_inf, args=(self, film,))
            procs.append(t)
            t.start()

        for proc in procs:
            proc.join()

    def get_inf(self, film):
        film = film.select_one(self.one_element)
        if film:
            ParsingMusic.result.append({
                "name": film.text.replace('\n', ''),
                "href": f"{film.get('href')}"
            })