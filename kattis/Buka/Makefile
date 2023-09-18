MAIN = buka.py
PY = python3

all: check_style check_types unittest localtest unittest_pytest
	@echo "All tests passed!"

localtest:
	@cat ./buka/1.in | $(PY) $(MAIN) | diff - ./buka/1.ans
	@cat ./buka/2.in | $(PY) $(MAIN) | diff - ./buka/2.ans
	@cat ./buka/3.in | $(PY) $(MAIN) | diff - ./buka/3.ans
	@cat ./buka/4.in | $(PY) $(MAIN) | diff - ./buka/4.ans
	@echo "All local tests passed!"

unittest:
ifeq ($(shell which pytest), )
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest test_unit_buka.py

unittest_pytest:
	pytest --hypothesis-show-statistics --hypothesis-seed=100 test_unit_buka.py

check_types:
	mypy --disallow-untyped-defs --strict buka.py
	mypy --disallow-untyped-defs --strict test_unit_buka.py

check_style:
	flake8 buka.py --count --show-source --statistics