import numpy as np

X1 = np.array([1, -2, 0, -1], dtype=np.float)
X2 = np.array([0, 1.5, -0.5, -1], dtype=np.float)
X3 = np.array([-1, 1, 0.5, -1], dtype=np.float)

X = np.array([X1, X2, X3], dtype=np.float)
W = np.array([1, -1, 0, 0.5], dtype=np.float)

d = np.array([-1, -1, 1], dtype=np.float)

c = 0.1
epochs = 1

for i in range(epochs):
    print("Iteration ", i+1)
    for j in range(len(X)):
        net = np.dot(X[j], W)
        
        if (net <= 0):
            op = -1
        elif net > 0:
            op = 1
        
        error = d[j] - op
       
        dW = c*error*X[j]
        W += dW
        
    print("W after ", i+1, " epochs ", W)    
print("Final W after ", epochs, "epochs:")
print(W)