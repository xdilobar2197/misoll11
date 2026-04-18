# misoll11




class Film:
    def __init__(self, nomi, janr, davomiyligi, reyting):
        self.nomi = nomi
        self.janr = janr
        self.davomiyligi = davomiyligi
        self.reyting = reyting

    def is_good(self):
        return "Yaxshi film" if self.reyting >= 8 else "Oddiy film"

    def get_info(self):
        return f"Nomi: {self.nomi}, Janr: {self.janr}, Davomiyligi: {self.davomiyligi} min, Reyting: {self.reyting}"


