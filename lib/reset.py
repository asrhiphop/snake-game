import pickle
import os
highScore = [0, 0, 0]
name = ["Default", "Default", "Default"]
pickle_out = open("highScore","wb")
pickle.dump(highScore, pickle_out)
pickle.dump(name, pickle_out)
pickle_out.close()


