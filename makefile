# target: dependencies
#  [tab] system command

all:
	g++ -O3 utils.cpp DAE.cpp Softmax.cpp StackedAE.cpp main.cpp -I eigen 

clean:
	rm -f *.o a.out

