class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    def __repr__(self):
        string = "{Author}. '{Name}'. {year}, {medium}".format(
            Author = self.artist, Name = self.title, year = self.year, medium = self.medium)
        return string

# class Marketplace:
#     def __init__(self, listings):
#         self.listings = listings

#     def addListing(self, newListing):


mandolinGirl = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)
print(mandolinGirl)