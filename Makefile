.PHONY: test
test:
	python -m unittest discover -v
test2:
	python -m unittest tests.test_money.TestMoney.test_plus_return_sum
