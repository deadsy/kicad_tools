
KICAD_UTILS = /home/jasonh/work/jasonh/kicad-library-utils
CHKLIB = $(KICAD_UTILS)/schlib/checklib.py
CHKMOD = $(KICAD_UTILS)/pcb/check_kicad_mod.py

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

libtest:
	$(CHKLIB) -vv ggm.lib

modtest:
	$(CHKMOD) -vv *.kicad_mod

clean:
	-rm $(LIB)
	-rm $(DCM)
	-rm *.kicad_mod
	-rm *.pyc

