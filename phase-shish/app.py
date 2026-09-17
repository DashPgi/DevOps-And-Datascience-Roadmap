# Custom error classes
class TooManyPagesReadError(ValueError):
    pass

class Book :
    def __init__(self, name : str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return f"Book({self.name}, {self.page_count}, {self.page_read})"

    def read(self, pages : int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.page_read + pages} pages, but you only have {self.page_count} pages."
            )
        self.page_read += pages
        print(self.page_read)

python101 = Book("Python", 50)

try :
    python101.read(66)
    python101.read(60)
except TooManyPagesReadError as e:
    print(e)