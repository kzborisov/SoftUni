import math


class PhotoAlbum:
    _max_photos_on_page = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count/PhotoAlbum._max_photos_on_page)
        return cls(pages)

    def add_photo(self, label):
        for page_number, page in enumerate(self.photos):
            if len(page) < self._max_photos_on_page:
                self.photos[page_number].append(label)
                slot = len(page)
                return f"{label} photo added successfully on page {page_number + 1} slot {slot}"
        return "No more free slots"

    def display(self):
        line_sep = "-" * 11 + "\n"
        result = line_sep
        for row in self.photos:
            result += " ".join(["[]" for _ in range(len(row))]) + "\n"
            result += line_sep

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
