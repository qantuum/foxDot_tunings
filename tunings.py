# Copy/Paste in FoxDot IDE

# Equal Temperament tunings w/ scales

# auto-done part
# def tuning function
def equal(temp):    
    return PRange(temp+1)*12/temp
# def scales functions - Careful, when len(tuning) != 12, the scales pre-defined in the Scale class will not work properly
def scales13() :
   return {
     'major13':P[0,2,6,8,9,11,12]
   }
# var scales dictionary
scales = {
  13:scales13
}

# input your temperament here :
temp = 13
print(equal(temp))
print(scales[temp]())

# Set scale default - now it requires to know the scale name (see print output above)
Scale.default.set(scales[temp]()['major13'], tuning=equal(temp))

# Equal temparent other than octave tunings w/ scales

print(Tuning.bohlen_pierce)
Scale.default.set(Scale.major, tuning=Tuning.bohlen_pierce)

# Just Intonation tunings w/ scales

print(Tuning.Just)
