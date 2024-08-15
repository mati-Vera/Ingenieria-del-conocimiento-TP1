###.:MATIAS VERA:.###

#Ejercicio 1
print("Mi Primer Código En Python.")
#---------------------------------------------------

#Ejercicio 2
matriz = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

for fila in matriz:
    print(" ".join(fila))
#---------------------------------------------------

#Ejercicio 3
respuesta = input("¿Qué estás estudiando? ")
print("Estas estudiando:", respuesta)
#---------------------------------------------------

#Ejercicio 4
country = input("¿En qué país vives? ")
print(country)
#---------------------------------------------------

#Ejercicio 5
def ej5():
    nombre = "David Bowman"
    edad = 51
#---------------------------------------------------

#Ejericio 6
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
#---------------------------------------------------

#Ejercicio 7
materia = "Ingeniería del conocimiento"
print("Estás estudiando " + materia)
#---------------------------------------------------

#Ejercicio 8
num1 = "35"
print(type(num1))
#---------------------------------------------------

#Ejercicio 9
def imprimir_asociado(nombre_asociado, numero_asociado):
    print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

    imprimir_asociado("Juan Pérez", 12345)
#---------------------------------------------------

#Ejercicio 10
numerador = 874
denominador = 27

cociente = numerador // denominador

print("El cociente de 874 dividido entre 27 es:", cociente)
#---------------------------------------------------

#Ejercicio 11
respuesta = round(10.676767)
print(respuesta)
#---------------------------------------------------

#Ejercicio 12
def encontrar_producto_mas_caro(productos):
    producto_mas_caro = None
    precio_maximo = float('-inf')

    for producto in productos:
        nombre, precio, cantidad = producto
        if precio > precio_maximo:
            precio_maximo = precio
            producto_mas_caro = producto

    return producto_mas_caro

productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]
producto_mas_caro = encontrar_producto_mas_caro(productos)
print("El producto más caro es:", producto_mas_caro)
#---------------------------------------------------

#Ejercicio 13
def ej13(matricula):
    estudiantes = {
        101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matematicas": 85, "ciencias": 90}},
        102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matematicas": 78, "ciencias": 88}}
    }

    notaMatematicas = estudiantes[matricula]["calificaciones"]["matematicas"]
    notaCiencias = estudiantes[matricula]["calificaciones"]["ciencias"]

    return (notaMatematicas + notaCiencias) / 2
#---------------------------------------------------

#Ejercicio 14
def analisis_temperaturas(temperaturas):
    temperatura_media = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    return temperatura_media, temperatura_maxima, temperatura_minima

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
temperatura_media, temperatura_maxima, temperatura_minima = analisis_temperaturas(temperaturas)
print("Temperatura media:", temperatura_media)
print("Temperatura máxima:", temperatura_maxima)
print("Temperatura mínima:", temperatura_minima)
#---------------------------------------------------

#Ejercicio 15
def calcular_promedio(*args):
    if len(args) == 0:
        return "No se ingresaron notas"
    
    promedio = sum(args) / len(args)
    return promedio

resultado = calcular_promedio(85, 90, 78, 92)
print("El promedio es:", resultado)
#---------------------------------------------------

#ejercicio 16
def crear_perfil(nombre, edad, email, **kwargs):
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }
    
    perfil.update(kwargs)
    
    return perfil

usuario = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")
print(usuario)
#---------------------------------------------------

#Ejercicio 17
def empleados_con_salario_mayor(empleados, salario_minimo):
    empleados_filtrados = {}
    for id_empleado, info in empleados.items():
        if info[2] > salario_minimo:
            empleados_filtrados[id_empleado] = info
    return empleados_filtrados

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

salario_minimo = 3000
empleados_filtrados = empleados_con_salario_mayor(empleados, salario_minimo)
print(empleados_filtrados)
#---------------------------------------------------

#Ejercicio 18

def procesar_ventas(ventas_diarias):
    total_ventas = sum(ventas_diarias)
    
    promedio_ventas = total_ventas / len(ventas_diarias)
    
    return total_ventas, promedio_ventas

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

total, promedio = procesar_ventas(ventas_diarias)

print("El total de ventas es:", total)
print("El promedio de ventas por día es:", promedio)
#---------------------------------------------------

#Ejercicio 19
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcular_total_goles(resultados):
    total_goles_anotados = 0
    total_goles_recibidos = 0

    for equipo, goles in resultados.items():
        goles_anotados, goles_recibidos = goles
        total_goles_anotados += goles_anotados
        total_goles_recibidos += goles_recibidos

    return total_goles_anotados, total_goles_recibidos

total_goles_anotados, total_goles_recibidos = calcular_total_goles(resultados)
print("Total de goles anotados:", total_goles_anotados)
print("Total de goles recibidos:", total_goles_recibidos)
#---------------------------------------------------

#Ejercicio 20
def configurar_app(**kwargs):
    configuraciones = {}
    for key, value in kwargs.items():
        configuraciones[key] = value
    return configuraciones

configuraciones = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)
print(configuraciones)
#---------------------------------------------------

#Ejercicio 21
def ej21():
    puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
    n = len(puntuaciones)
    
    for i in range(n):
        for j in range(i + 1, n):
            if puntuaciones[i][1] < puntuaciones[j][1]:
                puntuaciones[i], puntuaciones[j] = puntuaciones[j], puntuaciones[i]
    return puntuaciones
#---------------------------------------------------

#Ejercicio 22
def calcular_precios(paquetes):
    precios_totales = {}
    for paquete in paquetes:
        destino, precio, duracion = paquete
        precio_total = precio * duracion
        precios_totales[destino] = precio_total
    return precios_totales

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

resultados = calcular_precios(paquetes)
print(resultados)
#---------------------------------------------------

#Ejercicio 23
def actualizar_inventario(inventario, ventas):
    if len(inventario) != len(ventas):
        return "Error: La longitud del inventario y las ventas debe ser la misma."

    for i in range(len(inventario)):
        inventario[i] -= ventas[i]
    
    return inventario

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

inventario_actualizado = actualizar_inventario(inventario, ventas)
print("Inventario actualizado:", inventario_actualizado)
#---------------------------------------------------

#Ejercicio 24
def organizar_eventos(*args):
    for i, evento in enumerate(args, start=1):
        print(f"{i}. {evento}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")
#---------------------------------------------------

#Ejercicio 25
def analizar_finanzas(**kwargs):
    balance_final = 0
    for ingreso_o_gasto in kwargs.values():
        balance_final += ingreso_o_gasto
    return balance_final

balance = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"El balance final es: {balance}")
#---------------------------------------------------

#Ejercicio 26
def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = {
        "Nombre": nombre,
        "Edad": edad,
        "Salario": salario
    }
    
    for key, value in kwargs.items():
        empleado[key] = value
    
    return empleado

informacion_empleado = registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
print(informacion_empleado)
#---------------------------------------------------

# Ejercicio 27
ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def calcular_estadisticas_ventas(ventas):
    total_ventas = sum(ventas)
    promedio_mensual = round(total_ventas / len(ventas))
    mes_max_ventas = max(range(len(ventas)), key=lambda i: ventas[i]) + 1

    estadisticas = {
        "Total de ventas": total_ventas,
        "Promedio mensual": promedio_mensual,
        "Mes con mayores ventas": mes_max_ventas
    }

    return estadisticas

estadisticas = calcular_estadisticas_ventas(ventas_mensuales)
print("Estadísticas de ventas:")
for key, value in estadisticas.items():
    print(key + ":", value)
#---------------------------------------------------

#Ejercicio 28
def libros_despues_2000(biblioteca):
    libros_despues_2000 = []
    for titulo, libro in biblioteca.items():
        if libro["año"] > 2000:
            libros_despues_2000.append(titulo)
    return libros_despues_2000

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

libros_publicados_despues_2000 = libros_despues_2000(biblioteca)
print(libros_publicados_despues_2000)
#---------------------------------------------------

#Ejercicio 29
notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
def ej29(notas_estudiantes):
    resultados = {}
    for nombre, calificaciones in notas_estudiantes:
        promedio = calcular_promedio(calificaciones)
        resultados[nombre] = promedio
    return resultados
#---------------------------------------------------

#Ejercicio 30
def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = kwargs
    return perfiles

usuarios = ["Ana", "Luis", "María"]
resultados = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(resultados)
#---------------------------------------------------

#Ejercicio 31
def publicar(usuario, texto, **kwargs):
    publicacion = {
        "usuario": usuario,
        "texto": texto,
        "etiquetas": kwargs.get("etiquetas", []),
        "visibilidad": kwargs.get("visibilidad", "publica"),
        "likes": kwargs.get("likes", 0),
    }
    
    return publicacion

resultado = publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)
print(resultado)
#---------------------------------------------------

#Ejercicio 32
def simular_ventas(*args):
    total_ingresos = 0
    
    for venta in args:
        producto, cantidad, precio = venta
        total_ingresos += cantidad * precio
    
    return total_ingresos

total = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
print(f"El total de ingresos es: ${total:.2f}")
#---------------------------------------------------

#Ejercicio 33
def hacer_reserva(reservas, fecha, nombre_huesped, habitacion, precio):
    if fecha not in reservas:
        reservas[fecha] = []
    for reserva in reservas[fecha]:
        if reserva[1] == habitacion:
            print(f"La habitación {habitacion} ya está reservada en la fecha {fecha}.")
            return
    reservas[fecha].append((nombre_huesped, habitacion, precio))
    print(f"Reserva confirmada para {nombre_huesped} en la habitación {habitacion} el {fecha}.")

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

hacer_reserva(reservas, "2024-08-15", "María", 101, 150)
hacer_reserva(reservas, "2024-08-17", "Pedro", 103, 200)
print(reservas)
#---------------------------------------------------

#Ejercicio 34
def analizar_encuestas(encuestas):
    frecuencias = {}

    for pregunta, respuestas in encuestas.items():
        conteo_respuestas = {}
        
        for respuesta in respuestas:
            if respuesta in conteo_respuestas:
                conteo_respuestas[respuesta] += 1
            else:
                conteo_respuestas[respuesta] = 1
        
        frecuencias[pregunta] = conteo_respuestas
    
    return frecuencias

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultados = analizar_encuestas(encuestas)
print(resultados)
#---------------------------------------------------

# Ejercicio 35
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]
def optimizar_rutas(rutas, distancias_max):
    rutas_optimizadas = []

    for i in range(len(rutas)):
        if rutas[i][2] <= distancias_max[i]:
            rutas_optimizadas.append(rutas[i])

    return rutas_optimizadas

rutas_optimas = optimizar_rutas(rutas, distancias_max)
print("Rutas optimizadas:")
for ruta in rutas_optimas:
    print(ruta)
#---------------------------------------------------

#Ejercicio 36
def actualizar_inventario(tienda, **kwargs):
    inventario = {
        "Tienda A": {"producto_1": 50, "producto_2": 30},
        "Tienda B": {"producto_1": 20, "producto_2": 40}
    }
    
    if tienda in inventario:
        for producto, cantidad in kwargs.items():
            if producto in inventario[tienda]:
                inventario[tienda][producto] += cantidad
            else:
                inventario[tienda][producto] = cantidad
    
    return inventario

inventario_actualizado = actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)
print(inventario_actualizado)
#---------------------------------------------------

#Ejercicio 37
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia","#moda", "#viajes", "#verano", "#moda", "#tecnologia","#moda","#moda","#moda","#moda","#moda","#verano","#verano",]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
umbral=6

def ej37(hashtags, tendencias, umbral):
    frecuencia_hashtags = {}
    
    for hashtag in hashtags:
        if hashtag in frecuencia_hashtags:
            frecuencia_hashtags[hashtag] += 1
        else:
            frecuencia_hashtags[hashtag] = 1
    
    hashtags_mencionados = set()
    for hashtag, frecuencia in tendencias:
        if frecuencia > umbral:
            hashtags_mencionados.add(hashtag)
    
    hashtags_filtrados = [hashtag for hashtag in frecuencia_hashtags 
                          if frecuencia_hashtags[hashtag] > umbral and hashtag in hashtags_mencionados]
    
    return hashtags_filtrados
#---------------------------------------------------

#Ejercicio 38
def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    if usuario in suscripciones:
        suscripciones[usuario].append(suscripcion)
    else:
        suscripciones[usuario] = [suscripcion]
    for key, value in kwargs.items():
        suscripciones[usuario].append(f"{key}: {value}")
    return suscripciones

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

suscripciones = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(suscripciones)
#---------------------------------------------------

#Ejercicio 39
def simular_mercado(precios_diarios, operaciones):
    beneficio_total = 0
    acciones = 0
    
    for operacion, dia in operaciones:
        precio = precios_diarios[dia]
        
        if operacion == "compra":
            beneficio_total -= precio
            acciones += 1
        elif operacion == "venta" and acciones > 0:
            beneficio_total += precio
            acciones -= 1
        else:
            return "Error: No se pueden vender acciones si no se ha realizado una compra previa."
    
    return beneficio_total

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = simular_mercado(precios_diarios, operaciones)
print("Beneficio o pérdida total:", resultado)
#---------------------------------------------------

#Ejercicio 40
def calcular_ranking(estudiantes):
    promedios = {}

    for id_estudiante, materias in estudiantes.items():
        total_calificaciones = 0
        total_materias = 0
        
        for calificaciones in materias.values():
            total_calificaciones += sum(calificaciones)
            total_materias += len(calificaciones)
        
        promedio_general = total_calificaciones / total_materias
        promedios[id_estudiante] = promedio_general

    ranking = sorted(promedios.items(), key=lambda item: item[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = calcular_ranking(estudiantes)

for posicion, (id_estudiante, promedio) in enumerate(ranking, start=1):
    print(f"{posicion}. Estudiante ID {id_estudiante} - Promedio General: {promedio:.2f}")
#---------------------------------------------------
