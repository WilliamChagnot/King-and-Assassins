# Use to check if there is a 'cible' (knight, king, assassin, villager) in a certain radius (distance) of a position (x, y)

def lookout(x, y, distance, cible, state):
    for i in range(distance):
        for j in range(distance):
            x1 = x + i
            y1 = y + j
            if state['people'][x1][y1] == cible:
                return(x1, y1)
            x2 = x - i
            y2 = y + j
            if state['people'][x2][y2] == cible:
                return(x2, y2)
            x3 = x + i
            y3 = y - j
            if state['people'][x3][y3] == cible:
                return(x3, y3)
            x4 = x - i
            y4 = y - j
            if state['people'][x4][y4] == cible:
                return x4, y4
