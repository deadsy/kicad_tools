
LIB = ggm.lib
DCM = ggm.dcm

DST = /home/jasonh/work/googoomuck/hw

all:
	./py2lib -i ggm -t lib > $(LIB)
	./py2lib -i ggm -t dcm > $(DCM)
	./py2lib -i ggm -t mod
	cp $(LIB) $(DST)
	cp $(DCM) $(DST)

clean:
	-rm $(LIB)
	-rm $(DCM)
	-rm *.kicad_mod
	-rm *.pyc

