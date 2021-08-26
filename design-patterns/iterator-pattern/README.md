# Iterator pattern

The iterator pattern provides a way to access elements sequentially in an aggregate object, without exposing its inner representation. That is, the user of the aggregate object does not need to know if its an array, list, dictionary etc.

This makes it a lot easier to iterate over the aggregate object, with no need to change our iteration code if the underlying representation changes in the future.

Typically the aggregate object provides an _iterator_ that is used to _iterate_ through the items in the aggregate. This abstraction enables any code to easily interact with the aggregate.

Many languages such as Java, Javascript and Python, has iterators built into the language since it is such a useful pattern. E.g. in Python the loop constructs (for, while) allows to iterate over simple aggregates such as lists, dicts etc.

The example in [iterator.py](iterator.py) shows how an iterator can be coded from scratch. However, Python has an interface built-in to enable loop constructs to iterate over a custom object; `__iter__` and `__next__`. See the Python documentation for more info.
