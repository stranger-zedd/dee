from scipy.special import binom
import itertools
import collections

deck_size = 75

class Card:
    def __init__(self, num):
        self.num = num

    def range(self, start = 1):
        return range(start, self.num + 1)

class CardNode:
    def __init__(self, card, minimum):
        self.card = card
        self.minimum = minimum

def combin(cards, draw):
    return combin_nodes(card_nodes(cards), draw)

def combin_nodes(card_nodes, draw):
    failures = deck_size - reduce(lambda memo, node : memo + node.card.num, card_nodes, 0)
    quantities = []

    for st in list(itertools.product(*binomial_sets(card_nodes))):
        count = reduce(lambda memo, lst : memo + lst[0], st, 0)
        remainder = draw - count

        if(remainder < 0):
            continue
        elif(remainder == 0):
            extra_binomial = 1
        else:
            extra_binomial = binom(failures, remainder)

        quantities.append(reduce(lambda memo, lst : memo * lst[1], st, extra_binomial))

    return sum(quantities)

def binomial_sets(card_nodes):
    return map(lambda node : map(lambda n : [n, binom(node.card.num, n)], node.card.range(node.minimum)), card_nodes)

def card_nodes(cards):
    return map(lambda card : CardNode(card[0], card[1]) if isinstance(card, collections.Iterable) else CardNode(card, 1), cards)
