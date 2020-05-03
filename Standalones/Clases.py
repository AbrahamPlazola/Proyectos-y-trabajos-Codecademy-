### Clase que se encarga de crear los menúes
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return """
        El menu {menu} está disponible desde las {start_time}:00 
        hasta las {end_time}:00.
        """.format(menu = self.name, start_time = self.start_time,
        end_time = self.end_time)

    def calculate_bill(self, purchased_items):
        suma = 0
        for i in purchased_items:
            suma += self.items.get(i)
        return suma
### CLase que se encarga de crear los restaurantes relacionados con sus menúes
class Franchise:
    def __init__(self, address, menu): #, items, start_time, end_time):
        self.address = address
        self.menu = menu
        # super().__init__(menu, items, start_time, end_time)

    def __repr__(self):
        return """
        Este restaurant está localizado en {direccion}
        """.format(direccion = self.address)
    
    def available_menu(self, hora):
        disponibles = []
        for i in self.menu:
            if hora >= i.start_time and hora <= i.end_time:
                disponibles.append(i)
        return disponibles  
### Claase que se encarga de organizar los diferentes restaurantes con sus nombres
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
###Declaración y asignación de menúes
menuBrunch = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("Brunch", menuBrunch, 11, 16)

EBMenu = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early bird", EBMenu, 15, 18) 

dinnerMenu = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinnerMenu, 17, 23)

kidMenu ={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids", kidMenu, 11, 21)

###Declaración y asignación de tiendas
flagship_store = Franchise("1232 West End Road",
[brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", 
[brunch, early_bird, dinner, kids])

### Asignación de negocios
RestaurantNegocio = Business("Basta Fazoolin' with my Heart",
[flagship_store, new_installment])

###Asignación de nuevo menú y nuevo restaurante
arepasMenu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas = Menu("Arepas", arepasMenu, 10, 20)
arepasRestaurant = Franchise("189 Fitzgerald Avenue", arepasMenu)
ArepaNegocio = Business("Take a' Arepa", arepasRestaurant)

