import json
with open('peliculas.json','r') as fichero:
    doc=json.load(fichero)
cont=0
while True:
    print(''' 
    1. Lista de Titulo, año y duración.
    2. Muestra el Titulo de la película y el número de actores.
    3. Muestra la sinopsis de dos palabras dadas.
    4. Muestra las peliculas en las que haya trabajado el actor dado.
    5. Muestra el título y el poster de tres peliculas lanzadas entre dos fechas dadas.
    0.Salir
    ''')
    opcion=int(input("Introduce Opcion: "))
        #1. Lista el titulo, el año y la duración de la pelicula.
    if opcion==1:
        for i in doc:
            print("La pelicula %s es del año %s y dura %s"%(i["title"],i["year"],i["duration"]))
  