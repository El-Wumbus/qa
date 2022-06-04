all: build

build:
	${HOME}pyinstaller --onefile src/qa.py
	cp dist/qa ./

clean: 
	rm -rf build dist src/__pycache__ *.spec

install: all
	mkdir -p ${DESTDIR}${PREFIX}/usr/bin
	mkdir -p ${DESTDIR}${PREFIX}/usr/share/doc
	install -Dm755 qa ${DESTDIR}${PREFIX}/usr/bin/qa
	install -Dm644 README.md "${DESTDIR}${PREFIX}/usr/share/doc/qa"

uninstall: 
	rm -f ${DESTDIR}${PREFIX}/usr/bin/qa