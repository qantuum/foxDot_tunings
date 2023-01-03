################## Just Intonation tunings w/ scales ##################

# Default Just Inonation provided in FoxDot
Scale.default.set(Scale.major, tuning=Tuning.just)

# see JI collection @ https://en.xen.wiki/w/Gallery_of_12-tone_just_intonation_scales

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
    # let's convert ratios to cents
    @classmethod
    def toCent(cls, exp):
        import math
        if (isinstance(exp, Pattern)):
            for index in range(len(exp)):
                exp[index] = 12*math.log(exp[index], 2)
            return exp
        else:
            return exp
    
class Highschool1(Tunings):
    tuning = Tunings.toCent(P[1,21/20,9/8,6/5,5/4,4/3,7/5,3/2,8/5,5/3,7/4,15/8])

class CarlosHarm(Tunings):
    tuning = Tunings.toCent(P[1,17/16,9/8,19/16,5/4,21/16,11/8,3/2,13/8,27/16,7/4,15/8])

class Sevish(Tunings):
    tuning = Tunings.toCent(P[1,33/32,9/8,7/6,5/4,21/16,11/8,3/2,77/48,5/3,27/16,7/4])
    
class Hexany(Tunings):
    hexany_1379 = Tunings.toCent(P[1,7/6,4/3,3/2,14/9,7/4])
    hexany_1359 = Tunings.toCent(P[1,9/8,5/4,3/2,45/32,27/16,15/8])
