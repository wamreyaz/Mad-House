import numpy as np
import matplotlib.pyplot as plt
import random

N = 100
TEST = 1000
RUNS = 1000

def gen_samples(num):
    """
        Generates a num * 2 array of unifromly distributed numbers
        on (-1,1)
    """
    samples = np.random.uniform(-1, 1, (num, 2))
    return samples

def gen_target_fxn():
	"""
	    Generates the (x,y) intercept of the classyfying plane
	"""
	f = np.random.uniform(-1, 1, (2, 2))
	return f

def line_to_incpt(f):
	"""
		From the set of 4 points generate X, Y intercepts.
		Makes it easier
	"""
	x1 = f[0, 0]
	x2 = f[1, 0]
	y1 = f[0, 1]
	y2 = f[1, 1]

	m = (y2 -y1 / x2 - x1)

	Y_incpt = c = y2 - m*x1

	X_incpt = -c/m

	return (X_incpt, Y_incpt)


def find_label(fxn, data):
    """
        Uses a simple geometric formula to classify points in 2d
        plane.
        If eq of line is aX + bY = C, then point (X_0, Y_0) lies
        above or below the plane if aX_0 + bY_0 - C > 0 and
        aX_0 + bY_0 - C < 0, respectively. We use intercept form of line.
        fxn[0] is x intercept, fnx[1] is y intercept. data is N * 2 array
        of points
    """
    label = np.random.uniform(0, 1, data.shape[0])
    
    for ii in range(data.shape[0]):
        label[ii] = np.sign(data[ii ,0] * fxn[1] + data[ii, 1] *fxn[0] -fxn[0] * fxn[1])
                                              
    return label

def classify(weight, data):
    """
        Implements sgn(W^tX)
    """
    data_ = np.concatenate([np.array([1]), np.array(data)])
    prod = weight.dot(data_)
    return np.sign(prod)

def draw_plot(fxn, h, data,labels):
    line_x = np.linspace(-1, 1)
    line_y = fxn[1] - (fxn[1] / fxn[0] * line_x) 

    colors = {1:'r', -1:'g'}

    plt.plot(line_x, line_y, color = 'b')
    plt.plot(h[0], h[1], color = 'y')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.grid()

    color_list = [colors[labels[ii]] for ii in range(0, N)]

    plt.scatter(data[:, 0], data[:, 1], color = color_list)
    plt.show()

    
def get_line_from_weight(w):
    """
        Generates a line from the final 3-tuple of weights
        according to the equation  
            w_0*1 + w_1*x_1 + w_2*x_2 = 0
    """
    
    line_x = np.linspace(-1, 1)
    line_y = -w[0]/w[2] - (w[1] / w[2] * line_x) 
    return (line_x, line_y)


################################################################
################################################################

def PLA():
	"""
		It wraps all the above functions and also implements
		the PLA algorithm
	"""
	#All the random business
	samples = gen_samples(N)
	f = gen_target_fxn()
	fxn = line_to_incpt(f)

	# Classify points based on the target function
	labels = find_label(fxn, samples)

	weights = np.array([0, 0, 0])

	h = [0] * N
	num_iter = 0

	## Run actual PLA

	while True:
	    misclassified = []
	    for ii in range(0, N):
	        h[ii] = classify(weights, samples[ii])
	        if h[ii] != labels[ii]:
	            misclassified.append(ii)
	    
	    if len(misclassified) is not 0:
			
			num_iter += 1
			x = random.choice(misclassified)
			weights = weights + labels[x] * np.concatenate([np.array([1]), samples[x]])
	    else:
	        break

	return weights, fxn

##################################################################
##################################################################

## Run the PLA as many times as ypu like
error = 0.0
for i in xrange(0, RUNS):
	weights, fxn = PLA()
	test_samples = np.random.uniform(-1, 1, (TEST, 2))
	true_labels = find_label(fxn, test_samples)
	predicted_labels = np.random.uniform(0, 1, TEST)
	for ii in xrange(0, TEST):
		predicted_labels[ii] = classify(weights, test_samples[ii])
		if true_labels[ii] != predicted_labels[ii]:
			error += 1

print "P[f not g] = ", error/RUNS/TEST
