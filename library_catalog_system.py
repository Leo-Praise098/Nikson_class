from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, item_ID, title):
        if item_ID is None or str(item_ID).strip() == "":
            raise ValueError("Item ID cannot be empty.")
        if title is None or str(title).strip() == "":
            raise ValueError("Title cannot be empty.")

        self.item_ID = str(item_ID).strip()
        self.title = str(title).strip()
        self.is_borrowed = False

    @abstractmethod
    def check_out(self):
        if self.is_borrowed:
            print("This item has already been borrowed.")
        else:
            self.is_borrowed = True
            print("Item checked out successfully.")

    @abstractmethod
    def return_item(self):
        if not self.is_borrowed:
            print("This item is not currently borrowed.")
        else:
            self.is_borrowed = False
            print("Item returned successfully.")

    @abstractmethod
    def get_details(self):
        pass


class Book(LibraryItem):
    def __init__(self, item_ID: str, title: str, author: str, pages: int):
        super().__init__(item_ID, title)

        if not isinstance(author, str) or author.strip() == "":
            raise ValueError("Author cannot be empty.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer.")

        self.author = author.strip()
        self.pages = pages

    def check_out(self):
        if self.is_borrowed:
            print("This item has already been borrowed.")
        else:
            self.is_borrowed = True
            print("Item checked out successfully.")

    def return_item(self):
        if not self.is_borrowed:
            print("This item is not currently borrowed.")
        else:
            self.is_borrowed = False
            print("Item returned successfully.")

    def get_details(self):
        print(f"Item ID: {self.item_ID} \nTitle: {self.title} \nAuthor: {self.author} \nPages: {self.pages} pages.")


class DVD(LibraryItem):
    def __init__(self, item_ID: str, title: str, director: str, duration_minutes: int):
        super().__init__(item_ID, title)

        if not isinstance(director, str) or director.strip() == "":
            raise ValueError("Director cannot be empty.")
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer in minutes.")

        self.director = director.strip()
        self.duration_minutes = duration_minutes

    def check_out(self):
        if self.is_borrowed:
            print("This item has already been borrowed.")
        else:
            self.is_borrowed = True
            print("Item checked out successfully.")

    def return_item(self):
        if not self.is_borrowed:
            print("This item is not currently borrowed.")
        else:
            self.is_borrowed = False
            print("Item returned successfully.")

    def get_details(self):
        print(f"Item ID: {self.item_ID} \nTitle: {self.title} \nDirector: {self.director} \nTime duration: {self.duration_minutes} minutes.")


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item: LibraryItem):
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added to the library.")

        for existing_item in self.items:
            if existing_item.item_ID == item.item_ID:
                raise ValueError(f"An item with ID '{item.item_ID}' already exists.")

        self.items.append(item)
        print(f"Item '{item.title}' added to the library.")

    def remove_item(self, title: str):
        if title is None or str(title).strip() == "":
            raise ValueError("Title cannot be empty.")

        target = str(title).strip().lower()
        for item in self.items:
            if item.title.lower() == target:
                self.items.remove(item)
                print(f"Item '{item.title}' removed from the library.")
                return item

        print("Item not found in the library.")
        return None

    def search_item(self, title: str):
        if title is None or str(title).strip() == "":
            raise ValueError("Title cannot be empty.")

        target = str(title).strip().lower()
        for item in self.items:
            if item.title.lower() == target:
                print(f"Item found: {item.title}")
                return item

        print("Item not found in the library.")
        return None

    def display_items(self):
        if not self.items:
            print("No items in the library.")
            return

        for item in self.items:
            item.get_details()
            print()


def main():
    library = Library()

    while True:
        print("\nLibrary Catalog System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Item")
        print("4. Display All Items")
        print("5. Exit")

        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                item_type = input("Enter item type (book/dvd): ").lower().strip()
                item_ID = input("Enter item ID: ")
                title = input("Enter title: ")

                if item_type == "book":
                    author = input("Enter author: ")
                    pages = int(input("Enter number of pages: "))
                    book = Book(item_ID, title, author, pages)
                    library.add_item(book)
                elif item_type == "dvd":
                    director = input("Enter director: ")
                    duration_minutes = int(input("Enter duration in minutes: "))
                    dvd = DVD(item_ID, title, director, duration_minutes)
                    library.add_item(dvd)
                else:
                    print("Invalid item type.")

            elif choice == '2':
                title = input("Enter the title of the item to remove: ")
                library.remove_item(title)

            elif choice == '3':
                title = input("Enter the title of the item to search: ")
                library.search_item(title)

            elif choice == '4':
                library.display_items()

            elif choice == '5':
                print("Exiting the Library Catalog System.\nThankyou for using the system!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print(f"Error: {error}")
        except TypeError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()