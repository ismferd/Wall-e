PROJECT=Wall-e
MY_CURR_DIR=$(shell pwd)
MY_PYTHON_PATH=$(shell echo ${PYTHONPATH})
PIP=pip
test: clean
	export PYTHONPATH=$(MY_PYTHON_PATH):$(MY_CURR_DIR)/src; py.test -vv --cache-clear --cov-report term --cov=$(PROJECT) tests/$(PROJECT)