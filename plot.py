import numpy as np  
import matplotlib.pyplot as plt 
def read(filename,data):
	f=open(filename,"r")
	for line in f:
		data.append(float(line))
sgd_no_momentum=[]
sgd=[]
ada=[]
nag=[]
read("SGD_no_Momentum_Cifar.txt",sgd_no_momentum)
read("SGD_Cifar.txt",sgd)
read("ADA_Cifar.txt",ada)
read("NGA_Cifar.txt",nag)
iterations=range(1,200)
sgd_no_momentum_conv=[sgd_no_momentum[i]-0 for i in range(199)]
sgd_conv=[sgd[i]-0 for i in range(199)]
ada_conv=[ada[i]-0for i in range(199)]
nag_conv=[nag[i]-0 for i in range(199)]
plt.semilogy(iterations,sgd_no_momentum_conv,label="SGD_NO_Momentum")
plt.semilogy(iterations,sgd_conv,label="SGD_WITH_Momentum")
plt.semilogy(iterations,ada_conv,label="ADA")
plt.semilogy(iterations,nag_conv,label="NAG")
plt.legend(loc=1)
plt.title("Cifar")
plt.xlabel("num of iterations")
plt.ylabel("Loss Function")
plt.show()
