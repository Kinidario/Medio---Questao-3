import random
counter = 0
state = 'reta'

def control(inputs):
    global state
    global counter
    
    
    distance_right = inputs["distance-right"]
    distance_left  = inputs["distance-left"]
    front_left = inputs["front-left"]
    front_right = inputs["front-right"]
    
    speed = 20
    left_speed = 0
    right_speed = 0
    
    if state == 'reto':

        if front_left > 0.25 or front_right > 0.25 :
            state    = 'virando'
            counter  = random.randint(5, 13)
        else:
            state    = 'reto'
            
    elif state == 'virando':
        
        if counter > 0:
            counter -= 1
        
        else:
            state = 'reto'
            
            
    if distance_right < 300 and distance_left == 300:
        right_speed = speed - 20
        left_speed = speed 
   
    if distance_left < 300 and distance_right == 300:
        right_speed = -speed
        left_speed = speed-20
        
    if distance_left < 300 and distance_right < 300:
        right_speed = -speed
        left_speed = speed
        
    if distance_left == 300 and distance_right == 300:
        left_speed = speed 
        right_speed = speed - 20  
       
        
    elif state == 'virando':
        left_speed = speed
        right_speed = speed
            
            
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Distance Left',  'value': distance_left,  'min': 0, 'max': 300 },
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 }
        ]
    }
