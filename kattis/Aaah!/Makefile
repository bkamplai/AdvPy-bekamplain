MAIN = main.py
PY = python3

all: check_style check_types unittest localtest unittest_pytest submit clean
	@echo "All tests passed!"

localtest:
	@cat ./aaah/aaah.1.in | $(PY) $(MAIN) | diff - ./aaah/aaah.1.ans
	@cat ./aaah/aaah.2.in | $(PY) $(MAIN) | diff - ./aaah/aaah.2.ans
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
	kattis --problem aaah --language 'python 3' --force $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf *.pyc