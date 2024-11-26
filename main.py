from BobEsponja import bob
from LasChicasSuper import ChicasSuper
from ColorFavorito import PersonajeFav

def main():
    c1 = bob()
    c1.set_nombre ("Bob Esponja")
    c1.set_ano_estreno (1999)
    c1.set_concepto("Una esponja marina que vive en una piña debajo del mar")
    c1.set_genero("Comedia")
    c1.set_lugar_creacion("Estados Unidos")


    c2= ChicasSuper()
    c2.set_nombre("Las Chicas Superpoderosas")
    c2.set_ano_estreno(1998)
    c2.set_concepto("Tres chicas con superpoderes que luchan contra el crimen")
    c2.set_genero("Acción")
    c2.set_creador("Craig McCracken")


    c3= PersonajeFav()
    c3.set_nombre("AmigosImaginarios")
    c3.set_ano_estreno(2004)
    c3.set_concepto("las aventuras de un niño que visitaba a diario a su amigo imaginario en una casa muy acogedora para estas criaturas")
    c3.set_genero("Fantasía, Comedia y Aventuras")
    c3.set_personaje_mas_querido( "Mac")
    c3.set_pais_mas_visto("Mexico")
    c3.set_color_personaje_favorito("Blue")






    print("Caricatura 1")
    print(c1.descripcion())


    print("Caricatura 2")
    print(c2.descripcion())


    print("Caricatura 3")
    print(c3.descripcion())


if __name__ == "__main__":
    main()