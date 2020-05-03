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
        self.listings.remove(toRemove)

    def showListings(self):
        for i in self.listings:
            print(i)

class Client:
    def __init__(self, name, locations = "Private Collection", isMuseum = False):
        self.name = name
        self.locations = locations
        self.isMuseum = isMuseum

    def sellArtwork(self, artwork, price):
        if artwork.owner.name != self.name:
            print("Error")
            return

        newListing = Listing(artwork, price, self.name)
        veneer.addListing(newListing)
    
    def buyArtwork(self, artwork):
        if artwork.owner.name == self.name:
            print("You already own that artwork")
            return
        
        artListing = None
        for i in veneer.listings:
            if i.art == artwork:
                artListing = i
                break
        if artListing != None:
            artListing.art.owner = self
            veneer.removeListing(artListing)
        else:
            print("The artwork is not on any listing")
    
class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller
    
    def __repr__(self):
        string = "{ArtName}, ${Price}".format(ArtName = self.art.title, Price = self.price)
        return string

veneer = Marketplace()
edytta = Client("Edytta Halpirt")
moma = Client("The MOMA", "New York", True)
mandolinGirl = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

edytta.sellArtwork(mandolinGirl, "6M (USD)")

moma.buyArtwork(mandolinGirl)
print(mandolinGirl)

# Amazing! We built out a whole marketplace with buyers, sellers, art, and listings!

# Here are some more things you could try:

# Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
# Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
# Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.