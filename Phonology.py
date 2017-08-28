# coding: utf-8
from Feature import Feature
from itertools import product, chain


class Phoneme(object):
    __memory = dict()

    def __init__(self, symbole, **traits):
        self.__symbole = symbole
        self.__traits = set(map(lambda x: Feature(x[0], x[1]), traits.items()))
        recup = self.__memory.get(symbole)
        if recup == traits:
            print('Cette combinaison traits-symbole existe déjà.')
        else:
            self.__memory[symbole] = traits

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return self.__symbole if self.__symbole else str(self.__traits)

    @property
    def symbole(self):
        return self.__symbole

    @symbole.setter
    def symbole(self, value):
        pass

    @property
    def traits(self):
        return self.__traits

    @traits.setter
    def traits(self, value):
        pass


def main():
    from bs4 import BeautifulSoup
    from codecs import open

    tmp = open('api.html', 'r', 'utf-8')
    markup = BeautifulSoup(tmp, 'lxml')

    dico = dict()

    gg = [
        [('Aperture↓', 'Fermées'), [('non arr.', 'i'), ('arr.', 'y')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɨ'), ('', ''), ('arr.', 'ʉ')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɯ'), ('arr.', 'u')]],
        [('Aperture↓', 'Pré-fermées'), [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɪ'), ('arr.', 'ʏ')], [('non arr.', ''), ('', ''), ('arr.', '')], [('non arr.', '*'), ('arr.', 'ʊ')], [('non arr.', ''), ('arr.', '')]],
        [('Aperture↓', 'Mi-fermées'), [('non arr.', 'e'), ('arr.', 'ø')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɘ'), ('', ''), ('arr.', 'ɵ')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɤ'), ('arr.', 'o')]],
        [('Aperture↓', 'Moyennes'), [('non arr.', ''), ('arr.', '')], [('non arr.', ''), ('arr.', '')], [('non arr.', ''), ('', 'ə'), ('arr.', '')], [('non arr.', ''), ('arr.', '')], [('non arr.', ''), ('arr.', '')]],
        [('Aperture↓', 'Mi-ouvertes'), [('non arr.', 'ɛ'), ('arr.', 'œ')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɜ'), ('', ''), ('arr.', 'ɞ')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ʌ'), ('arr.', 'ɔ')]],
        [('Aperture↓', 'Pré-ouvertes'), [('non arr.', 'æ'), ('arr.', '')], [('non arr.', ''), ('arr.', '')], [('non arr.', ''), ('', 'ɐ'), ('arr.', '')], [('non arr.', ''), ('arr.', '')], [('non arr.', ''), ('arr.', '')]],
        [('Aperture↓', 'Ouvertes'), [('non arr.', 'a'), ('arr.', 'ɶ')], [('non arr.', ''), ('arr.', '')], [('non arr.', ''), ('', 'ä'), ('arr.', '')], [('non arr.', ''), ('arr.', '')], [('non arr.', 'ɑ'), ('arr.', 'ɒ')]]
    ]

    rr = list(chain(*list(zip(*list(map(lambda x: list(chain(*x[1:])), gg))))))
    for x, y, z in product(['antérieur', '~antérieur', 'central', '~postérieur', 'postérieur'], ['non rarrondi', '-', 'arrondi'], ['fermé', 'pré fermé', 'mi fermé', 'moyen', 'mi ouverte', 'pré ouvert', 'ouvert']):
        if (x != 'central') and (y == '-'):
            dico[(x, y, z)] = '-'
        else:
            pp = rr.pop(0)
            dico[(x, y, z)] = pp[1] if pp[1] else '-'
    print(*dico.items(), sep='\n')

if __name__ == '__main__':
    main()
