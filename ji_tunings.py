################## Just Intonation tunings w/ scales ##################

# Default Just Inonation provided in FoxDot
Scale.default.set(Scale.major, tuning=Tuning.just)

# see JI collection @ https://en.xen.wiki/w/Gallery_of_12-tone_just_intonation_scales
# this JI collection offers JI tunings of 12 notes that form an octave.

# let's convert ratios to cents
def toCent(exp):
    import math
    if (isinstance(exp, Pattern)):
        for index in range(len(exp)):
            exp[index] = 12*math.log(exp[index], 2)
        return exp
    else:
        return exp

class JI_highschhol1:
  tuning = toCent(P[1,21/20,9/8,6/5,5/4,4/3,7/5,3/2,8/5,5/3,7/4,15/8])

