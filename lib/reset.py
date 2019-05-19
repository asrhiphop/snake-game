import pickle
import os
highScore = 0
pickle_out = open("highScore","wb")
pickle.dump(highScore, pickle_out)
pickle_out.close()


