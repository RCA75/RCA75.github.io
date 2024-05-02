import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}
###############################################

def choose_q(dificultad):
    preguntas_disponibles = p.pool_preguntas[dificultad]
    
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
        
    pregunta = preguntas_disponibles[f'pregunta_{n_elegido}']  # selecciono la pregunta
    enunciado, alternativas = shuffle_alt(pregunta)
    return pregunta['enunciado'], alternativas



if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')