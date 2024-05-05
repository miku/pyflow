.PHONY: test
test:
	mut.py --target calculator --unit-test test_calculator -m

# [*] Start mutation process:
#    - targets: calculator
#    - tests: test_calculator
# [*] 1 tests passed:
#    - test_calculator [0.00023 s]
# [*] Start mutants generation and execution:
#    - [#   1] AOR calculator: 
# --------------------------------------------------------------------------------
#   1: def mul(x, y):
# - 2:     return x * y
# + 2:     return x / y
# --------------------------------------------------------------------------------
# [0.00458 s] killed by test_mul (test_calculator.CalculatorTest)
#    - [#   2] AOR calculator: 
# --------------------------------------------------------------------------------
#   1: def mul(x, y):
# - 2:     return x * y
# + 2:     return x // y
# --------------------------------------------------------------------------------
# [0.00446 s] killed by test_mul (test_calculator.CalculatorTest)
#    - [#   3] AOR calculator: 
# --------------------------------------------------------------------------------
#   1: def mul(x, y):
# - 2:     return x * y
# + 2:     return x ** y
# --------------------------------------------------------------------------------
# [0.00700 s] survived
# [*] Mutation score [0.04727 s]: 66.7%
#    - all: 3
#    - killed: 2 (66.7%)
#    - survived: 1 (33.3%)
#    - incompetent: 0 (0.0%)
#    - timeout: 0 (0.0%)
