from typing import Dict
from os import listdir
from os.path import isfile
import logging


def tree(file_path: str) -> None:
	if os.path.isdir(file_path):
		for i in os.path.listdir(file_path):
			if os.path.isfile(i):
				print(i);
