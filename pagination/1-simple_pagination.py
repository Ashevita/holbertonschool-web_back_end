#!/usr/bin/env python3
"""Module contenant une fonction
simple pour calculer les index de pagination."""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"


def index_range(page: int, page_size: int) -> tuple:
    """
    Calcule les index de début et de fin pour la pagination.

    Args:
        page (int): Le numéro de page (1-indexé).
        page_size (int): Le nombre d'éléments par page.

    Returns:
        tuple: Un tuple contenant l'index de début et l'index de fin.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


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
    pass


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    Retourne une page de données paginées.

    Args:
        page (int): Numéro de page, doit être > 0.
        page_size (int): Taille de la page, doit être > 0.

    Returns:
        List[List]: Une liste contenant les
        lignes correspondantes à la page demandée.
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    start_index, end_index = index_range(page, page_size)
    dataset = self.dataset()

    # Si les index dépassent la taille du dataset, retourne une liste vide
    if start_index >= len(dataset):
        return []

    return dataset[start_index:end_index]
