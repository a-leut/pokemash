class Const:
    NUM_POKE = 650

def numToStr(n):
    sn = str(n)
    if len(sn) == 1:
        return '00'+sn
    elif len(sn) == 2:
        return '0'+sn
    elif len(sn) == 3:
        return sn
