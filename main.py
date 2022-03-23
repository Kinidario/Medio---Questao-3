#importando o comando para selecionar números aleatórios
import random
#variáveis globais
counter = 0
state = 'reta'

#Função, ela é chamada 60 vezes por segundo
def control(inputs):
#declarando as variaveis como globais para elas serem alteradas no código inteiro
    global state
    global counter
    
#Recebendo as informações do sensor
    distance_right = inputs["distance-right"]
    distance_left  = inputs["distance-left"]
    front_left = inputs["front-left"]
    front_right = inputs["front-right"]
  
#Variáveis
    speed = 20
#Velocidade de cada roda
    left_speed = 0
    right_speed = 0
    
    if state == 'reto':
#se o sensor passar de 0,25 o robô está muito próximo da borda
        if front_left > 0.25 or front_right > 0.25 :
#o robô muda o estado dele e o contador recebe um valor aleatório
            state    = 'virando'
            counter  = random.randint(5, 13)
        else:
            state    = 'reto'
            
    elif state == 'virando':
#diminuido o contador do tempo que o robô passará virando
        if counter > 0:
            counter -= 1
        
        else:
            state = 'reto'
            
#se o sensor detecta um robô ele mudará a direção dele para o robô inimigo
#vira para a direita
    if distance_right < 300 and distance_left == 300:
        right_speed = speed - 20
        left_speed = speed 

#vira para a esquerda
    if distance_left < 300 and distance_right == 300:
        right_speed = -speed
        left_speed = speed-20

#segue reto
    if distance_left < 300 and distance_right < 300:
        right_speed = -speed
        left_speed = speed

#procura o robô inimigo
    if distance_left == 300 and distance_right == 300:
        left_speed = speed 
        right_speed = speed - 20  
       
#se o estado do robô for virando, robô rodará pelo tempo do contador.
    elif state == 'virando':
        left_speed = speed
        right_speed = speed
            
#retorna a velocidade das rodas          
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Distance Left',  'value': distance_left,  'min': 0, 'max': 300 },
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 }
        ]
    }
