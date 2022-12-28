#import from scipy and matplotlib
import scipy.io.wavfile,matplotlib.pyplot
#read sample rate and wave vector from file
x,y = scipy.io.wavfile.read('mha.wav')
vdur = len(y)/x            #calculate duration
#print duration
print('Duration of wave:',vdur)
matplotlib.pyplot.plot(y)  #make plot
matplotlib.pyplot.show()   #show plot

