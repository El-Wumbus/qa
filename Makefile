all: build

build:
	pyinstaller --onefile src/qa.py
	cp dist/qa ./

autodoc:
	cd docs
	sphinx-apidoc -o . ../src --ext-autodoc
	cd ..

docs: autodoc
	cd docs
	make clean
	make html

clean: 
	rm -rf build dist src/__pycache__ *.spec

install: build
	mkdir -p ${DESTDIR}${PREFIX}/usr/bin
	mkdir -p ${DESTDIR}${PREFIX}/usr/share/doc
	install -Dm755 qa ${DESTDIR}${PREFIX}/usr/bin/qa
	install -Dm644 README.md "${DESTDIR}${PREFIX}/usr/share/doc/qa"

uninstall: 
	rm -f ${DESTDIR}${PREFIX}/usr/bin/qa