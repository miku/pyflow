.PHONY: run
run:
	monkeytype run main.py
	monkeytype stub ops.ops > ops/ops.pyi

.PHONY: list
list:
	monkeytype list-modules


.PHONY: clean
clean:
	rm -f monkeytype.sqlite3
	rm -f ops/ops.pyi
