if __name__ == '__main__':
    colores = {'azul': 'blue', 'negro': 'black', 'rosado': 'pink'}

    propiedades = {1: 'Nombre', 2: 'Apellido', 3: 'Profesión', 4: 'Región'}

    print(propiedades)
    colores

    ### También podemos modificar los valores de sus elementos y realizar operaciones con ellos
    colores['negro'] = 'noir'

    print(colores)

    edades = {'Albert': 24,
              'Johel': 24,
              'Roque': 26,
              'Victor': 27
              }
    edades['Roque']

    #Puedes acceder a la clave
    for c in edades:
        print(c)

    #Podemos acceder al contenido de la clave
    #Es decir del lado derecho
    for c in edades:
        print(edades[c])

    ### El método _items()_ nos devuelve Clave y Valor automáticamente
    for cla, e in edades.items():
        print(cla, e)

    ### El método _del()_ nos permite eliminar los valores de un diccionario.
    del (colores['azul']);

    print(colores)

    ### Debemos combinar provechosamente las listas y los diccionarios. Por ejemplo para crear un equipo de personajes
    equipo = []

    personajes = {'Nombre': 'Raskolnikov',
                  'Clase': 'Picaro',
                  'Nación': 'Rusia'
                  }
    equipo.append(personajes);
    print(equipo)

    personajes = {'Nombre': 'Emma',
                  'Clase': 'Curandera',
                  'Nación': 'Francia'
                  }
    equipo.append(personajes);

    personajes = {'Nombre': 'Rebeca',
                  'Clase': 'Banquera',
                  'Nación': 'Inglaterra'
                  }
    equipo.append(personajes);
    equipo

    for e in equipo:
        print(e["Nombre"], ",", e["Clase"], "oriundo de ", e["Nación"]);