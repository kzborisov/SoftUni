from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)