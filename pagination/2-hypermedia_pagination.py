import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Retourne un tuple contenant les indices de début et de fin correspondant
    à la plage d'index pour une pagination donnée.

    Arguments :
        page (int) : le numéro de la page (1-indexé).
        page_size (int) : le nombre d'éléments par page.

    Retour :
        tuple : (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne une page de données basée sur les arguments de pagination.

        Arguments :
            page (int) : le numéro de la page (1-indexé).
            page_size (int) : le nombre d'éléments par page.

        Retour :
            List[List] : Les lignes correspondantes à la page demandée.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retourne les métadonnées hypermédia pour une pagination donnée.

        Arguments :
            page (int) : le numéro de la page (1-indexé).
            page_size (int) : le nombre d'éléments par page.

        Retour :
            Dict : Les métadonnées incluant la page,
            les données, et les infos de navigation.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
