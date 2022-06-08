all: build

build:
	pyinstaller --onefile src/qa.py
	mv dist/qa "bin/qa-linux-$(shell printf 'r.$(shell git rev-list --count HEAD)')-$(shell date +%s)"

sums:
	$(shell sha256sum bin/qa* > bin/sha256sums)

clean: 
	rm -rf build dist src/__pycache__ *.spec docs/_build

install: build
	mkdir -p ${DESTDIR}${PREFIX}/usr/bin
	mkdir -p ${DESTDIR}${PREFIX}/usr/share/doc
	install -Dm755 qa ${DESTDIR}${PREFIX}/usr/bin/qa
	install -Dm644 README.rst "${DESTDIR}${PREFIX}/usr/share/doc/qa"

uninstall: 
	rm -f ${DESTDIR}${PREFIX}/usr/bin/qa