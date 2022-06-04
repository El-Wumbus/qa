all: build

build:
	pyinstaller --onefile src/qa.py
	cp dist/qa ./

clean: 
	rm -rf build dist src/__pycache__ *.spec

install: all
	mkdir -p ${DESTDIR}${PREFIX}/usr/bin
	cp -f qa ${DESTDIR}${PREFIX}/usr/bin/qa
	chmod 755 ${DESTDIR}${PREFIX}/usr/bin/qa

uninstall:
	rm -f ${DESTDIR}${PREFIX}/usr/bin/qa