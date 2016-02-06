# Dee

Some statistics for a game we're making called 'Cult Following'.

## Usage

At the moment, this is a library intended to be used in a REPL. Open a Python REPL, and load in `cf-stats.py`:

```python
execfile('dee.py')
```

Once you've got that in, you can use `combin(cards, draw)` to get the number of possible hand combinations
containing a given set of cards, or `probability(cards, draw)` to get the probability of drawing a given set
of cards.

Cards are, right now, just wrappers around an integer representing how many of them are in the deck. Hence, the
constructor is just `Card(num)`. I'm working on this.

If you'd like a combination including _multiple_ copies of a card, you can pass either `combin` or `probability`
an array representing that card and the minimum number, something like this:

```python
combin([Card(3), [Card(3), 2]], 5)
```
