################## Scales and tuning names can be researched on https://en.xen.wiki/ ##################

################## Equal Temperament tunings (select a class) ##################
################## "ET" or "Equal Temperament" can also be defined as "EDO" or "Equal Division of Octive"

# global method to return cumulative sum
def cumulative(exp):
        if (isinstance(exp, Pattern)):
            for index in range(len(exp)):
                if index != 0:
                    exp[index] = exp[index-1]+exp[index]
            return exp
        else:
            return exp

# abstract class for distributing names method
class Tunings:
    def library(self):
        lib = []
        for items in (self.__class__.__dict__.items(), self.__dict__.items()):
            lib.extend([(key, value) for key, value in items if isinstance(value, (Pattern))])
        return dict(lib)
    def names(self):
        return sorted(self.library().keys())

class ET10(Tunings):
    tuning = PRange(11)*12/10
    chromatic = PRange(11)
    minor = [0,2,3,4,6,7,8]
    def library(self):
        lib = []
        for items in (self.__class__.__dict__.items(), self.__dict__.items()):
            lib.extend([(key, value) for key, value in items if isinstance(value, (Pattern))])
        return dict(lib)
    def names(self):
        return sorted(self.library().keys())
    
class ET11(Tunings):
    tuning = PRange(12)*12/11
    chromatic = PRange(12)
    machine5 = cumulative(P[0,2,2,2,2])
    machine6 = cumulative(P[0,2,2,2,2,2])
    orgone7 = cumulative(P[0,1,2,1,2,1,2])
    mavilaC = cumulative(P[0,1,1,1,3,1,1])
    mavilaD = cumulative(P[0,1,1,3,1,1,3])
    mavilaE = cumulative(P[0,1,3,1,1,3,1])
    mavilaF = cumulative(P[0,3,1,1,3,1,1])
    mavilaG = cumulative(P[0,1,1,3,1,1,1])
    mavilaA = cumulative(P[0,1,3,1,1,1,3])
    mavilaB = cumulative(P[0,3,1,1,1,3,1])
    classicPenta = cumulative(P[0,1,4,1,4])
    swoon = cumulative(P[0,2,3,1,3])


class ET14(Tunings):
    tuning = PRange(15)*12/14
    chromatic = PRange(15)
    major = P[0,2,4,6,9,11,133]

class ET17(Tunings):
    tuning = PRange(18)*12/17
    chromatic = PRange(18)
    otonal = P[0,3,5,8,10,12,14]
    neutral = P[0,2,5,7,10,12,15]
    
class ET18(Tunings):
    tuning = PRange(19)*12/18
    chromatic = PRange(19)
    minor = P[0,3,5,8,11,13,15]
    major = P[0,3,6,8,11,14,17]
    
class ET20(Tunings):
    tuning = PRange(21)*12/20
    chromatic = PRange(21)
    blackwood10Major = cumulative(P[0,3,1,3,1,3,1,3,1,3])
    blackwood10Minor = cumulative(P[0,1,3,1,3,1,3,1,3,1])
    balzano9 = cumulative(P[0,2,3,2,2,2,3,2,2])
    balzano11 = cumulative(P[0,2,2,2,2,1,2,2,2,2,2])
    balzano9Inverse = cumulative(P[0,2,2,2,3,2,2,2,3])
    balzano11Inverse = cumulative(P[0,1,2,2,2,2,2,1,2,2,2])
    octatonic = cumulative(P[0,2,3,2,3,2,3,2])
    diminished = cumulative(P[0,3,2,3,2,3,2,3])
    major = cumulative(P[0,4,3,1,4,3,4])
    minor = cumulative(P[0,4,1,3,4,1,4])
    chromatic12 = cumulative(P[0,2,2,1,2,1,2,2,1,2,2,2])
    zweifelMajor = cumulative(P[0,2,2,2,2,1,2,2,2,2,1])
    zweifelMinor = cumulative(P[0,2,1,2,2,2,2,2,1,2,2])
    majorQuasi = cumulative(P[0,3,3,3,3,3,3])
    minorQuasi = cumulative(P[0,3,2,3,3,3,3])
    rotenberg = cumulative(P[0,3,2,2,2,2,3,2,2])
    stearnsMajor = cumulative(P[0,3,4,1,4,3,3])
    pentatonic = cumulative(P[0,7,2,7,2])
    antiDiatonic = cumulative(P[0,5,2,2,5,2,2])
    
class ET22(Tunings):
    tuning = PRange(23)*12/22
    chromatic = PRange(23)
    porcupine = P[0,3,6,9,13,16,19]
    
class ET23(Tunings):
    tuning = PRange(24)*12/22
    chromatic = PRange(24)
    keter = cumulative(P[0,2,2,2,3,2,2,3,2,2])
    chesed = cumulative(P[0,2,2,3,2,2,3,2,2,3])
    netzach = cumulative(P[0,2,3,2,2,3,2,2,3,2])
    malkuth = cumulative(P[0,3,2,2,3,2,2,3,2,2])
    binah = cumulative(P[0,2,2,3,2,2,3,2,2,2])
    tiferet = cumulative(P[0,2,3,2,2,3,2,2,2,3])
    yesod = cumulative(P[0,3,2,2,3,2,2,2,3,2])
    chokmah = cumulative(P[0,2,2,3,2,2,2,3,2,2])
    gevurah = cumulative(P[0,2,3,2,2,2,3,2,2,3])
    hod = cumulative(P[0,3,2,2,2,3,2,2,3,2])

    
class ET36(Tunings):
    tuning = PRange(37)*12/36
    chromatic = PRange(37)

# application example

print(ET17().names())

Scale.default.set(ET17.otonal,tuning=ET17.tuning)

################## Equal temparent other than octave tunings w/ scales, these are not EDOs since our reference space is not an octive ##################

Scale.default.set(Scale.major, tuning=Tuning.bohlen_pierce)
