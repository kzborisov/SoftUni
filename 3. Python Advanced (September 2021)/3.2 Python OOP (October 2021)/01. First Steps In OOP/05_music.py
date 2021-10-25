class Music:
    def __init__(self, title, artis, lyrics):
        self.title = title
        self.artis = artis
        self.lyrics = lyrics

    def print_info(self):
        return f'this is "{self.title}" from "{self.artis}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
