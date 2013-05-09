#!/usr/bin/env python

import os
import re
import subprocess
import sys

def main():
	# Stash any changes not in the current commit
	subprocess.call(['git', 'stash', '-u', '--keep-index'], stdout=subprocess.PIPE)

	subprocess.call(['gradle', '-q', 'rebuild'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# Unstash all changes 
	subprocess.call(['git', 'reset', '--hard'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.call(['git', 'stash', 'pop', '--quite', '--index'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
	main()