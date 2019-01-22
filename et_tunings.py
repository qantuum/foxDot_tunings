################## Copy/Paste your method of choice in FoxDot IDE ##################

################## Find out about these scale names on https://en.xen.wiki/ ##################

################## Equal Temperament tunings (select a class) ##################

# function to return cumulative calculation (xenharmonic 'modes' - important in somes classes, keep an eye on it !!!
def cumulative(exp):
    if (isinstance(exp, list)):
        for index in range(len(exp)):
            if index != 0:
                exp[index] = exp[index-1]+exp[index]
        return exp
    else:
        return exp

class ET10:
    tuning = PRange(11)*12/10
    chromatic = PRange(11)
    minor = [0,2,3,4,6,7,8]
    
class ET11:
    tuning = PRange(12)*12/11
    chromatic = PRange(12)
    machine5 = cumulative([0,2,2,2,2])
    machine6 = cumulative([0,2,2,2,2,2])
    orgone7 = cumulative([0,1,2,1,2,1,2])
    mavilaC = cumulative([0,1,1,1,3,1,1])
    mavilaD = cumulative([0,1,1,3,1,1,3])
    mavilaE = cumulative([0,1,3,1,1,3,1])
    mavilaF = cumulative([0,3,1,1,3,1,1])
    mavilaG = cumulative([0,1,1,3,1,1,1])
    mavilaA = cumulative([0,1,3,1,1,1,3])
    mavilaB = cumulative([0,3,1,1,1,3,1])
    classicPenta = cumulative([0,1,4,1,4])
    swoon = cumulative([0,2,3,1,3])


class ET14:
    tuning = PRange(15)*12/14
    chromatic = PRange(15)
    major = [0,2,4,6,9,11,133]

class ET17:
    tuning = PRange(18)*12/17
    chromatic = PRange(18)
    otonal = [0,3,5,8,10,12,14]
    neutral = [0,2,5,7,10,12,15]
    
class ET18:
    tuning = PRange(19)*12/18
    chromatic = PRange(19)
    minor = [0,3,5,8,11,13,15]
    major = [0,3,6,8,11,14,17]
    
class ET20:
    tuning = PRange(21)*12/20
    chromatic = PRange(21)
    blackwood10Major = cumulative([0,3,1,3,1,3,1,3,1,3])
    blackwood10Minor = cumulative([0,1,3,1,3,1,3,1,3,1])
    balzano9 = cumulative([0,2,3,2,2,2,3,2,2])
    balzano11 = cumulative([0,2,2,2,2,1,2,2,2,2,2])
    balzano9Inverse = cumulative([0,2,2,2,3,2,2,2,3])
    balzano11Inverse = cumulative([0,1,2,2,2,2,2,1,2,2,2])
    octatonic = cumulative([0,2,3,2,3,2,3,2])
    diminished = cumulative([0,3,2,3,2,3,2,3])
    major = cumulative([0,4,3,1,4,3,4])
    minor = cumulative([0,4,1,3,4,1,4])
    chromatic12 = cumulative([0,2,2,1,2,1,2,2,1,2,2,2])
    zweifelMajor = cumulative([0,2,2,2,2,1,2,2,2,2,1])
    zweifelMinor = cumulative([0,2,1,2,2,2,2,2,1,2,2])
    majorQuasi = cumulative([0,3,3,3,3,3,3])
    minorQuasi = cumulative([0,3,2,3,3,3,3])
    rotenberg = cumulative([0,3,2,2,2,2,3,2,2])
    stearnsMajor = cumulative([0,3,4,1,4,3,3])
    pentatonic = cumulative([0,7,2,7,2])
    antiDiatonic = cumulative([0,5,2,2,5,2,2])
    
class ET22:
    tuning = PRange(23)*12/22
    chromatic = PRange(23)
    porcupine = [0,3,6,9,13,16,19]

    
class ET36:
    tuning = PRange(37)*12/36
    chromatic = PRange(37)


    
Scale.default.set(ET17.otonal,tuning=ET17.tuning)

################## Equal temparent other than octave tunings w/ scales ##################

Scale.default.set(Scale.major, tuning=Tuning.bohlen_pierce)
