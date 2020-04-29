class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        string = "{Author}. '{PaintName}'. {year}, {medium}. {Owner}, {Location}".format(
            Author = self.artist, PaintName = self.title, year = self.year, medium = self.medium,
            Owner = self.owner.name, Location = self.owner.locations)
        return string

class Marketplace:
    def __init__(self, listings = None):
        if listings == None:
            self.listings = []
        else:
            self.listings = listings

    def addListing(self, newListing):
        self.listings.append(newListing)

    def removeListing(self, toRemove):
        self.listings.pop(toRemove)

    def showListings(self):
        for i in self.listings:
            print(i)

class Client:
    def __init__(self, name, locations = "Private Collection", isMuseum = False):
        self.name = name
        self.locations = locations
        self.isMuseum = isMuseum
    

veneer = Marketplace()
edytta = Client("Edytta Halpirt")
moma = Client("The MOMA", "New York", True)
mandolinGirl = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print(mandolinGirl)