
LIB = ggm.lib
DCM = ggm.dcm

DST = /home/jasonh/work/googoomuck/hw

all:
	./py2lib -i ggm -t lib > $(LIB)
	./py2lib -i ggm -t dcm > $(DCM)
	cp $(LIB) $(DST)
	cp $(DCM) $(DST)

clean:
	-rm $(LIB)
	-rm $(DCM)
	-rm *.pyc

