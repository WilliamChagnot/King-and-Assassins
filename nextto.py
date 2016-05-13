# Use to know if the target (xt, yt) is next to someone (x, y)

def nextto(x, y, xt, yt):
    di = ''
    yes = False
    if x == xt and y-1 == yt:
        yes = True
        di = 'W'
    elif x == xt and y+1 == yt:
        yes = True
        di = 'E'
    elif y == yt and x-1 == xt:
        yes = True
        di = 'N'
    elif y == yt and x+1 == xt:
        yes = True
        di = 'S'
    now = [di, yes]
    return now
