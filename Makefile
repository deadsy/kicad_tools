
LIB = ggm.lib

all:
	./py2lib >> $(LIB)

clean:
	-rm $(LIB)
	-rm *.pyc

