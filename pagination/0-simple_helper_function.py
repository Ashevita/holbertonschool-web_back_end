#!/usr/bin/env python3
"""Module contenant une fonction
simple pour calculer les index de pagination."""


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
