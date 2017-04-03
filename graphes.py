# coding: utf8

from typing import *
from collections import *
import collections
import typing
import heapq
import functools


class makeSet(object):
    def __init__(self, x):
        self.__parent = x
        self.__rang = 0

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        pass

    @property
    def rang(self):
        return self.__rang

    @rang.setter
    def rang(self, value):
        pass

    def __le__(self, other):
        return self.rang < other.rang

    def __gt__(self, other):
        return self.rang > other.rang

    def __lt__(self, other):
        return self.rang <= other.rang

    def __eq__(self, other):
        return self.rang == other.rang

    def __ge__(self, other):
        return self.rang >= other.rang

    def __repr__(self):
        return '({}, {})'.format(
            self.parent,
            self.rang
        )

    def __str__(self):
        return repr(self)


def union(x, y):
    racine1 = find(x)
    racine2 = find(y)

    if racine1 != racine2:
        if racine1.rang < racine2.rang:
            racine1.parent = racine2
        else:
            racine2.parent = racine1
            if racine1.rang == racine2.rang:
                racine1.rang += 1

def kruskal(graphe):
    sortie = set()
    g_prim = heapq.heapify(map(makeSet, graphe.sommets))
    for (u, v) in graphe.aretes:
        if find(u) != find(v):
            sortie.add((u, v))
            union(u, v)

def find(x):
    if x[0] != None:
        return find(x[0])


def apparait_dans(x, t):
    tps += 1
    return apparait_dans_bis(x, t)

def apparait_dans_bis(x, t):
    pass

def unify(t1, t2):
    pass

@functools.lru_cache()
def h(j, d):
    return j(d)
    #dd = next(k, None)
    #if j(dd):
    #    print('oui', dd)
    #    return h(j, k)
    #elif dd is None:
    #    return True
    #else:
    #    return False


def fmap(func, ls, res=None):
    if res is None:
        res = []
    if not ls:
        return res
    res.append(func(ls[0]))
    return fmap(func, ls[1:], res)


def lmap(l, f, x=[]):
    return l and lmap(l[1:], f, x+[f(l[0])]) or x


def main():
    func, arg1, arg2 = str()
    f = "({func})({arg1}){arg2}".format(func=func, arg1=arg1, arg2=arg2)


def tdl_syntax():
    tmp = {
        "axiome : TYPE '=' attvals '.'",
        "parent : '&' TYPE",
        "parents : parent parents | parent",
        "attvals : '[' features ']'",
        "features : feature ',' features | feature",
        "feature : VAR TYPE",
        "coreference : '#' NUM"
    }


if __name__ == '__main__':
    main()
