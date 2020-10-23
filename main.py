OUT00 = 0

def on_forever():
    global OUT00
    IN00 = 0
    if IN00 == 1:
        OUT00 = 1
    else:
        OUT00 = 0
forever(on_forever)
