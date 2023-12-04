class LibraryItem:
    def __init__(self, name, author, item_id):
        self.name = name
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.name}, Author: {self.author}, Checked Out: {self.checked_out}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.name} has been checked out."
        else:
            return f"{self.name} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.name} has been returned.")
        else:
            print(f"{self.name} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Director: {self.director}, Duration: {self.duration} minutes")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Director: {self.director}, Duration: {self.duration} minutes")


class Magazine(LibraryItem):
    def __init__(self, title, issue, item_id):
        super().__init__(title, "N/A", item_id)
        self.issue = issue

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Issue: {self.issue}")


def main():
    book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", item_id="B001", genre="Classic")
    dvd = DVD(title="Inception", director="Christopher Nolan", item_id="D001", duration=148)
    magazine = Magazine(title="Vogue", issue="October 2023", item_id="M001")
    book.display_info()
    print(book.check_out())
    book.return_item()