################## Scales and tuning names can be researched on https://en.xen.wiki/ ##################

################## Equal Temperament tunings (select a class) ##################
################## "ET" or "Equal Temperament" can also be defined as "EDO" or "Equal Division of Octive"

# abstract class for distributing names method
class Tunings:
    @classmethod
    def library(cls):
        lib = []
        for items in (cls.__class__.__dict__.items(), cls.__dict__.items()):
            lib.extend([(key, value) for key, value in items if isinstance(value, (Pattern))])
        return dict(lib)
    @classmethod
    def names(cls):
        return sorted(cls.library().keys())
    # global method to return cumulative sum
    @classmethod
    def cumulative(cls, exp):
        if (isinstance(exp, Pattern)):
            for index in range(len(exp)):
                if index != 0:
                    exp[index] = exp[index-1]+exp[index]
            return exp
        else:
            return exp

class ET10(Tunings):
    tuning = PRange(11)*12/10
    chromatic = PRange(11)
    minor = P[0,2,3,4,6,7,8]
    
class ET11(Tunings):
    tuning = PRange(12)*12/11
    chromatic = PRange(12)
    machine5 = Tunings.cumulative(P[0,2,2,2,2])
    machine6 = Tunings.cumulative(P[0,2,2,2,2,2])
    orgone7 = Tunings.cumulative(P[0,1,2,1,2,1,2])
    mavilaC = Tunings.cumulative(P[0,1,1,1,3,1,1])
    mavilaD = Tunings.cumulative(P[0,1,1,3,1,1,3])
    mavilaE = Tunings.cumulative(P[0,1,3,1,1,3,1])
    mavilaF = Tunings.cumulative(P[0,3,1,1,3,1,1])
    mavilaG = Tunings.cumulative(P[0,1,1,3,1,1,1])
    mavilaA = Tunings.cumulative(P[0,1,3,1,1,1,3])
    mavilaB = Tunings.cumulative(P[0,3,1,1,1,3,1])
    classicPenta = Tunings.cumulative(P[0,1,4,1,4])
    swoon = Tunings.cumulative(P[0,2,3,1,3])


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
    blackwood10Major = Tunings.cumulative(P[0,3,1,3,1,3,1,3,1,3])
    blackwood10Minor = Tunings.cumulative(P[0,1,3,1,3,1,3,1,3,1])
    balzano9 = Tunings.cumulative(P[0,2,3,2,2,2,3,2,2])
    balzano11 = Tunings.cumulative(P[0,2,2,2,2,1,2,2,2,2,2])
    balzano9Inverse = Tunings.cumulative(P[0,2,2,2,3,2,2,2,3])
    balzano11Inverse = Tunings.cumulative(P[0,1,2,2,2,2,2,1,2,2,2])
    octatonic = Tunings.cumulative(P[0,2,3,2,3,2,3,2])
    diminished = Tunings.cumulative(P[0,3,2,3,2,3,2,3])
    major = Tunings.cumulative(P[0,4,3,1,4,3,4])
    minor = Tunings.cumulative(P[0,4,1,3,4,1,4])
    chromatic12 = Tunings.cumulative(P[0,2,2,1,2,1,2,2,1,2,2,2])
    zweifelMajor = Tunings.cumulative(P[0,2,2,2,2,1,2,2,2,2,1])
    zweifelMinor = Tunings.cumulative(P[0,2,1,2,2,2,2,2,1,2,2])
    majorQuasi = Tunings.cumulative(P[0,3,3,3,3,3,3])
    minorQuasi = Tunings.cumulative(P[0,3,2,3,3,3,3])
    rotenberg = Tunings.cumulative(P[0,3,2,2,2,2,3,2,2])
    stearnsMajor = Tunings.cumulative(P[0,3,4,1,4,3,3])
    pentatonic = Tunings.cumulative(P[0,7,2,7,2])
    antiDiatonic = Tunings.cumulative(P[0,5,2,2,5,2,2])
    
class ET22(Tunings):
    tuning = PRange(23)*12/22
    chromatic = PRange(23)
    porcupine = P[0,3,6,9,13,16,19]
    
class ET23(Tunings):
    tuning = PRange(24)*12/22
    chromatic = PRange(24)
    keter = Tunings.cumulative(P[0,2,2,2,3,2,2,3,2,2])
    chesed = Tunings.cumulative(P[0,2,2,3,2,2,3,2,2,3])
    netzach = Tunings.cumulative(P[0,2,3,2,2,3,2,2,3,2])
    malkuth = Tunings.cumulative(P[0,3,2,2,3,2,2,3,2,2])
    binah = Tunings.cumulative(P[0,2,2,3,2,2,3,2,2,2])
    tiferet = Tunings.cumulative(P[0,2,3,2,2,3,2,2,2,3])
    yesod = Tunings.cumulative(P[0,3,2,2,3,2,2,2,3,2])
    chokmah = Tunings.cumulative(P[0,2,2,3,2,2,2,3,2,2])
    gevurah = Tunings.cumulative(P[0,2,3,2,2,2,3,2,2,3])
    hod = Tunings.cumulative(P[0,3,2,2,2,3,2,2,3,2])

class ET24(Tunings):
    tuning = PRange(25)*12/24
    chromatic = PRange(25)
    makam_segah = Tunings.cumulative(P[0,3,4,4,3,3,4])
    makam_huzzam = Tunings.cumulative(P[0,3,4,2,6,2,4])
    makam_hicazkar = Tunings.cumulative(P[0,2,5,3,4,2,5])
    makam_mahur = Tunings.cumulative(P[0,4,3,3,4,4,4])
    makam_rast = Tunings.cumulative(P[0,4,3,3,4,4,3])
    makam_ussak = Tunings.cumulative(P[0,3,3,4,4,2,4])
    
class ET36(Tunings):
    tuning = PRange(37)*12/36
    chromatic = PRange(37)
    
# non-octive based tunings must include a redifinition of our interval range. For example, re-creating the Boehlen-Pierce scale goes like:

class BoehlenPierceII:
    tuningfreq = 3**(PRange(14)/13)
    tuning=[]
    for i in tuningfreq:
        tuning.append(math.log(i,2)*12)
    chromatic = PRange(14)
        
# as you see, we need to redigine our intervals first, then convert them to cents.

# Now let us go with a nice tunings discovered by James Mulvale, the Sweetie

class Sweetie(Tunings):
    tuningfreq = (23/16)**(PRange(9)/8)
    tuning=[]
    for i in tuningfreq:
        tuning.append(math.log(i,2)*12)
    chromatic = Prange(9)
        
#the Sweetie generates nice, warm-sounding notes. It is the division in 8 disting pitches, of the ratio 23/16, as opposed to the octave, which is 2/1; or the tritave, which is 3/1.

# application example

print(ET17.names())

Scale.default.set(ET17.otonal,tuning=ET17.tuning)

################## Equal temparent other than octave tunings w/ scales, these are not EDOs since our reference space is not an octive ##################

Scale.default.set(Scale.major, tuning=Tuning.bohlen_pierce)
