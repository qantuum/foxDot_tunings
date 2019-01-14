################## Copy/Paste your method of choice in FoxDot IDE ##################

################## Find out about these scale names on https://en.xen.wiki/ ##################

################## Equal Temperament tunings (select a class) ##################

class ET10:
    tuning = PRange(11)*12/10
    minor = P[0,2,3,4,6,7,8]

class ET14:
    tuning = PRange(15)*12/14
    chromatic = PRange(15)
    major = P[0,2,4,6,9,11,133]

class ET17:
    tuning = PRange(18)*12/17
    chromatic = PRange(18)
    otonal = P[0,3,5,8,10,12,14]
    neutral = P[0,2,5,7,10,12,15]
    
class ET18:
    tuning = PRange(19)*12/18
    chromatic = PRange(19)
    minor = P[0,3,5,8,11,13,15]
    major = P[0,3,6,8,11,14,17]
    
class ET20:
    tuning = PRange(21)*12/20
    blackwood10 = P[0,3,4,7,8,11,12,15,16,19]
    
class ET22:
    porcupine = P[0,3,6,9,13,16,19]
    tuning = PRange(23)*12/22

    
class ET36:
    tuning = PRange(37)*12/36
    chromatic = PRange(37)


    
Scale.default.set(ET17.otonal,tuning=ET17.tuning)

################## Equal temparent other than octave tunings w/ scales ##################

Scale.default.set(Scale.major, tuning=Tuning.bohlen_pierce)

################## Just Intonation tunings w/ scales ##################

Scale.default.set(Scale.major, tuning=Tuning.just)
