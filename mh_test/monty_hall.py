import random
import sys

def thingy():
	doors = [False,False,False]
	doors[random.randint(0,2)] = True
	if doors[random.randint(0,2)] == True:
		return 0
	else:
		return 1

if __name__ == "__main__":
	N = None
	try:
		N = int(sys.argv[1])
	except:
		print "Defaulting to N = 10000"
		N = 10000
	win_counter = 0
	for x in range(N):
		win_counter += thingy()
	print str(win_counter) + "/"+str(N)+"= " + str(float(win_counter)/float(N))
