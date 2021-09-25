.PHONY: default
default: wheel

.PHONY: wheel
wheel:
	rm -rf *egg*info
	python3 setup.py bdist_wheel
	mv dist/journalmap*whl .
