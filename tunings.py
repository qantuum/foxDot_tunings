################## Copy/Paste your method of choice in FoxDot IDE ##################

################## Find out about these scale names on https://en.xen.wiki/ ##################

################## Equal Temperament tunings (select a class) ##################

class ET14:
    tuning = PRange(15)*12/14,
    chromatic = PRange(15),   

class ET17:
    tuning = PRange(18)*12/17,
    chromatic = PRange(18),
    otonal = P[0,3,5,8,10,12,14],
    neutral = P[0,2,5,7,10,12,15],
    
Scale.default.set(ET17.otonal,tuning=ET17.tuning)

################## Equal temparent other than octave tunings w/ scales ##################

Scale.default.set(Scale.major, tuning=Tuning.bohlen_pierce)

################## Just Intonation tunings w/ scales ##################

Scale.default.set(Scale.major, tuning=Tuning.just)
