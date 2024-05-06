SHELL = /bin/bash

requests.pyz:
	# shiv requests -o requests.pyz
	# We need to pass -p or --python to shiv; do not use the venvs python.
	shiv requests -o requests.pyz --python "/usr/bin/env python3"

clean:
	rm -f requests.pyz

run: requests.pyz
	./$<

