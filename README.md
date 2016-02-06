# Dee

Some statistics for a game we're making called 'Cult Following'.

## Usage

At the moment, this is a library intended to be used in a REPL. Open a Python REPL, and load in `cf-stats.py`:

```python
execfile('dee.py')
```

Once you've got that in, the function you probably want to use (in fact, really the _only_ useful function right
now) is `combin(cards, draw)`. This function will give you the number of possible combinations for drawing a set
of cards, including combinations with _more_ than the number of that card you need.

To use `combin`, you'll need to create some `Card`s. At the moment, a `Card` is literally a wrapper around an
integer describing how many of a given card exists in a deck (I'm working on that bit now). As such, to create
one, the interface is just `Card(num)`.

After you have `Card`s representing all the cards in your combination, you can just call `Combin` with those cards
and the amount of cards in your initial draw. This will return a (probably fairly large) number. That's the amount
of hands which could possibly contain your combo.

To get the probability, divide that by `binom(deck_size, draw)`.
