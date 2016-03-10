.PHONY: test

all: test

test: .tox/py27
	tox -e py27 -- $(ARGS)
