import random
class pokemon:
    def __init__(self, nombre, nivel, tipo, consciente = True, atk, defc, spd, spec):
        self.nombre = nombre.lower()
        self.nivel = nivel
        self.vidaMax = ((100 + random.randint(0, 26)) * nivel)/100 + 10
        self.vidaAct = self.vidaMax
        self.tipo = tipo.lower()
        self.consciente = consciente
    
    def perderVida(self, daño):
        self.vidaAct -= daño
        if self.vidaAct > 0:
            print("Vida actual de {nombre}: {vida:.0f} / {Vmax:.0f}"
            .format(nombre = self.nombre, vida = self.vidaAct, Vmax = self.vidaMax))
        else:
            self.vidaAct = 0
            self.consciente = False
            print("¡{pokemon} fue derrotado y quedó inconsciente!".format(pokemon = self.nombre))
    
    def revivir(self):
        self.vidaAct = self.vidaMax / 2
        self.consciente = True
        print("¡{pokemon} ya no está debilitado, ahora tiene {vida:.0f} / {Vmax:.0f}!".format(pokemon = self.nombre,
        vida = self.vidaAct, Vmax = self.vidaMax))
    
    def curar(self, curacion):
        if self.vidaAct + curacion > self.vidaMax:
            curacionReal = self.vidaMax - self.vidaAct
            self.vidaAct += curacion
        else:
            curacionReal = curacion
            self.vidaAct += curacion
        print("¡{pokemon} ha recuperado {ps} puntos de vida!".format(pokemon = self.nombre, ps = curacionReal))
        print("{pokemon} ahora tiene {vida:.0f} / {vMax:.0f}"
        .format(pokemon = self.nombre, vida = self.vidaAct, vMax = self.vidaMax))

    def atacar(self, pokemonRival, tipoAtk):
        if self.consciente == True:
            multiplicador = 0
            for efectividad in tablaTipos:
                if pokemonRival.tipo in efectividad.get(tipoAtk.lower(), "a"):
                    break
                multiplicador += 1
            
            if multiplicador == 1:
                multiplicador = 0.5
            
            if self.tipo == tipoAtk.lower():
                multiplicador += 1.5

            daño = (((self.nivel * 2) / 10) + 2) * (multiplicador + random.uniform(0.85, 1.00))
            print("¡{pokemonRival} recibe {daño:.0f} puntos de daño!".format(pokemonRival = pokemonRival, daño = daño))
            pokemonRival.perderVida(daño)
        else:
            print("El pokemon está incosciente y no puede atacar!")
    
    def __repr__(self):
        return self.nombre

class Entrenador:
    def __init__(self, poke, nombre, pociones, revivires, pokActivo):
        self.pokemon = poke
        self.nombre = nombre
        self.pociones = pociones
        self.revivires = revivires
        self.pokemonActivo = pokActivo
    
    def usarPocion(self, tipoPot):
        tipoPot.lower()
        print("¡{nombre} utilizó una {tipoPot} pocion!".format(nombre = self.nombre, tipoPot = tipoPot))
        curacion = Pociones.get(tipoPot) 
        self.pokemon[self.pokemonActivo].curar(curacion)
    
    def atacarEntrenador(self, rival, tipoAtk):
        PokemonAtacante = self.pokemon[self.pokemonActivo]
        pokemonRival = rival.pokemon[rival.pokemonActivo]
        print("¡{pokAtk} ataca a {pokRival} con un ataque de tipo {tipoAtk}!"
        .format(pokAtk = PokemonAtacante, pokRival = pokemonRival, tipoAtk = tipoAtk))

        PokemonAtacante.atacar(pokemonRival, tipoAtk)

    def cambiarPokemon(self, pokemonCambiar):
        if self.pokemon[pokemonCambiar].consciente == True:
            print("{nombre} ha retirado a {pok}".format(nombre = self.nombre, pok = self.pokemon[self.pokemonActivo]))
            self.pokemonActivo = pokemonCambiar
            print("¡{nombre} ha enviado a {pok} al combate!"
            .format(nombre = self.nombre, pok = self.pokemon[self.pokemonActivo]))
        else:
            print("El pokemon al que intentas cambiar no puede estar inconsciente!")

    def revivir(self, numeroPok):
        if self.pokemon[numeroPok].consciente == False:
            print("{nombre} ha utilizado revivir en {pok}"
            .format(nombre = self.nombre, pok = self.pokemon[numeroPok]))
            self.pokemon[numeroPok].revivir()
        else:
            print("{pok} no está debilitado".format(pok = self.pokemon[numeroPok]))
    
###Diccionarios para la efectividad de tipos
Efectivo = {
    "fuego": ["planta", "hielo", "bicho", "acero"],
    "agua": ["fuego", "tierra", "roca"],
    "electrico": ["agua", "volador"],
    "planta": ["agua", "tierra", "roca"],
    "hielo": ["planta", "tierra", "volador", "dragon"],
    "lucha": ["normal", "hielo", "roca", "siniestro", "acero"],
    "veneno": ["planta", "hada"],
    "tierra": ["fuego", "electrico", "veneno", "roca", "acero"],
    "volador": ["planta", "lucha", "bicho"],
    "psiquico": ["lucha", "veneno"],
    "bicho": ["planta", "psiquico", "siniestro"],
    "roca": ["agua", "hielo", "volador", "bicho"],
    "fantasma": ["psiquico", "fantasma"],
    "dragon": ["dragon"],
    "siniestro": ["psiquico", "fantasma"],
    "acero": ["hielo", "roca", "hada"],
    "hada": ["lucha", "dragon", "siniestro"]
}
pocoEfectivo = {
    "normal": ["roca", "acero"],
    "fuego": ["fuego", "agua", "roca", "dragon"],
    "agua": ["agua", "planta", "dragon"],
    "electrico": ["electrico", "planta", "dragon"],
    "planta": ["fuego", "planta", "veneno", "volador", "bicho", "dragon", "acero"],
    "hielo": ["fuego", "agua", "hielo", "acero"],
    "lucha": ["veneno", "volador", "psiquico", "bicho", "hada"],
    "veneno": ["veneno", "tierra", "roca", "fantasma"],
    "tierra": ["planta", "bicho"],
    "volador": ["electrico", "roca", "acero"],
    "psiquico": ["psiquico", "acero"],
    "bicho": ["fuego", "lucha", "veneno", "volador", "fantasma", "acero", "hada"],
    "roca": ["lucha", "tierra", "acero"],
    "fantasma": ["siniestro"],
    "dragon": ["acero"],
    "siniestro": ["lucha", "siniestro", "hada"],
    "acero": ["fuego", "agua", "electrico", "acero"],
    "hada": ["fuego", "veneno", "acero"]
}
Nulo = {
    "normal": ["fantasma"],
    "electrico": ["tierra"],
    "lucha": ["fantasma"],
    "veneno": ["acero"],
    "tierra": ["volador"],
    "psiquico": ["siniestro"],
    "fantasma": ["normal"],
    "dragon": ["hada"]
}
tablaTipos = [Nulo, pocoEfectivo, Efectivo]

###Diccionarios pociones
Pociones = {
    "hiper": 100,
    "super": 50,
    "normal": 20
}

charmander = pokemon("charmander", 18, "fuego")
bulbasaur = pokemon("bulbasaur", 15, "planta")
squirtle = pokemon("squirtle", 16, "agua")
pikachu = pokemon("pikachu", 20, "electrico")
eevee = pokemon("eevee", 20, "normal")

pocionesIniciales = ["normal", "super"]
Ash = Entrenador([charmander, pikachu, bulbasaur], "Ash", pocionesIniciales, 1, 1)
Gary = Entrenador([squirtle, eevee], "Gary", pocionesIniciales, 1, 1)

Ash.atacarEntrenador(Gary, "acero")
Gary.usarPocion("normal")
Ash.atacarEntrenador(Gary, "electrico")
Gary.atacarEntrenador(Ash, "normal")
Gary.cambiarPokemon(0)
Gary.cambiarPokemon(1)
Gary.revivir(1)
Gary.cambiarPokemon(1)