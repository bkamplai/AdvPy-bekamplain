MAIN = main.py
PY = python3

all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All tests passed!"

localtest:
	@cat ./simpleaddition/1.in | $(PY) $(MAIN) | diff - ./simpleaddition/1.ans
	@cat ./simpleaddition/2.in | $(PY) $(MAIN) | diff - ./simpleaddition/2.ans
	@echo "All local tests passed!"

unittest:
ifeq ($(shell which pytest), )
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest -v test_unit_main.py

unittest_pytest:
	pytest -v --hypothesis-show-statistics --hypothesis-seed=100 test_unit_main.py

check_types:
	mypy --disallow-untyped-defs --strict main.py
	mypy --disallow-untyped-defs --strict test_unit_main.py

check_style:
	flake8 main.py --count --show-source --statistics

submit:
	kattis --problem simpleaddition --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc