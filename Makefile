all: build

build:
	pyinstaller --onefile src/qa.py
	cp dist/qa ./


docs:
	printf "cd docs\n\
	sphinx-apidoc -o . ../src --ext-autodoc\n\
	make clean\n\
	make html\n\
	cd ..\n"

clean: 
	rm -rf build dist src/__pycache__ *.spec
	cd docs
	bash -c "make clean"
	cd ..

install: build
	mkdir -p ${DESTDIR}${PREFIX}/usr/bin
	mkdir -p ${DESTDIR}${PREFIX}/usr/share/doc
	install -Dm755 qa ${DESTDIR}${PREFIX}/usr/bin/qa
	install -Dm644 README.md "${DESTDIR}${PREFIX}/usr/share/doc/qa"

uninstall: 
	rm -f ${DESTDIR}${PREFIX}/usr/bin/qa