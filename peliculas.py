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
   #2. Muestra los títulos de las peliculas y el numero de actores.
    if opcion==2:
        for i in doc:
            print("La pelicula %s tiene: "%(i["title"]),end="")
            for i in i["actors"]:
                cont+=1
            print(cont,"actores/actrices")
            cont=0
 #3. Mostrar las peliculas que tengan en la sinopsis dos palabras dadas
    if opcion==3:
        pal1=input("Introduce una palabra: ")
        pal2=input("Introduce otra palabra: ")
        for i in doc:
            if (pal1 in i["storyline"]) and (pal2 in i["storyline"]):
                print(i["title"])
 #4. Mostrar las peliculas en las que haya trabajado el actor dado
    if opcion==4:
        actor=input("Introduce nombre de actor: ")
        for i in doc:
            if actor in i["actors"]:
                print (i["title"])
