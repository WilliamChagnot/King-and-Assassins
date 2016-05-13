# Try to figure out the best way from a point (x, y) to a point (xt, yt)
# The player 0 move horizontaly first (better for assassins)

def bestway(nb, x, y, xt, yt):
    px = 0
    py = 0
    di = ''
    if nb == 0:
        if x == xt:
            if y < yt:
                py = 1
                di = 'E'
            elif y > yt:
                py = -1
                di = 'W'
        elif x < xt:
            px = 1
            di = 'S'
        elif x > xt:
            px = -1
            di = 'N'

    if nb == 1:
        if y == yt:
            if x < xt:
                px = 1
                di = 'S'
            elif x > xt:
                px = -1
                di = 'N'
        elif y < yt:
            py = 1
            di = 'E'
        elif y > yt:
            py = -1
            di = 'W'
    return(px, py, di)
