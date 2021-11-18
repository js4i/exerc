#! /usr/bin/env python
import re
from itertools import tee


def _pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def valida_cdvpy(cdvpy: str):
    """ """
    match = re.search(r'^[1-9][0-9]{5}$', cdvpy)

    if bool(match):

        list_of_input = list(map(int, cdvpy))
        list_of_pairwise = list(
            _pairwise(list_of_input)
        )

        repeted_pairwise_size = len(list_of_pairwise)
        pairwise_size = len(
            set(x for x in list_of_pairwise)
        )

        return repeted_pairwise_size == pairwise_size

    return False


if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))
