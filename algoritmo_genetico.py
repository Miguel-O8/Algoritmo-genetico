import random

# Parámetros del algoritmo
tam_poblacion = 10
num_generaciones = 20
prob_mutacion = 0.1 #10% de probabilidad de mutacióngit init


# Función de evaluación: maximizar f(x) = x^2
def evaluar(individuo):
    return int(individuo, 2) ** 2

# Generar población inicial de números binarios aleatorios
def generar_poblacion(tam):
    return [''.join(random.choice('01') for _ in range(5)) for _ in range(tam)]

# Selección por torneo
def seleccion(poblacion):
    torneo = random.sample(poblacion, 2)
    return max(torneo, key=evaluar)

# Cruce de un punto
def cruce(padre1, padre2):
    punto = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

# Mutación
def mutar(individuo):
    individuo = list(individuo)
    for i in range(len(individuo)):
        if random.random() < prob_mutacion:
            individuo[i] = '1' if individuo[i] == '0' else '0'
    return ''.join(individuo)

# Algoritmo Genético
def algoritmo_genetico():
    poblacion = generar_poblacion(tam_poblacion)
    
    for _ in range(num_generaciones):
        nueva_poblacion = []
        for _ in range(tam_poblacion // 2):
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            hijo1, hijo2 = cruce(padre1, padre2)
            nueva_poblacion.extend([mutar(hijo1), mutar(hijo2)])
        poblacion = nueva_poblacion
    
    mejor_individuo = max(poblacion, key=evaluar)
    return mejor_individuo, evaluar(mejor_individuo)

# Ejecutar el algoritmo
mejor, valor = algoritmo_genetico()
print(f'Mejor individuo: {mejor} ({int(mejor, 2)}) con valor: {valor}')
