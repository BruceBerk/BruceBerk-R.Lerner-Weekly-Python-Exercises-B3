import pytest
import json
from solution import Serializable, JSONMixin, XMLMixin, CSVMixin


def test_no_mixin(tmp_path):
    class Book(Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book('title', 'author', 100)
    p = tmp_path / "hello.txt"

    b.dump(p)

    b = Book('Catch-22', 'Joseph Heller', 30)

    b.load(p)

    assert b.title == 'title'
    assert b.author == 'author'
    assert b.price == 100

