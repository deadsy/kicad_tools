
DST = /home/jasonh/work/googoomuck/hw

LIB = ggm.lib
DCM = ggm.dcm
MOD = $(DST)/ggm.pretty

all:
	./py2lib -i ggm -t lib > $(LIB)
	./py2lib -i ggm -t dcm > $(DCM)
	./py2lib -i ggm -t mod
	cp $(LIB) $(DST)
	cp $(DCM) $(DST)
	cp *.kicad_mod $(MOD)

clean:
	-rm $(LIB)
	-rm $(DCM)
	-rm *.kicad_mod
	-rm *.pyc

