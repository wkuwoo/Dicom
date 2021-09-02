import os
import pydicom
import copy
import hashlib
import PIL
import sys
import json
import argparse
import multiprocessing
import pylibjpeg
import pandas as pd
import numpy as np

from tqdm import tqdm
from pydicom.tag import Tag

def get_all_dcm_paths(input_dir, file_exts):
    paths = []
    for r, d, f in os.walk(input_dir):
        for file in f:
            file_name, extension = os.path.splitext(file)
            if extension.lower() not in file_exts:
                continue
            if not extension:
                if file_name.find('.') >= 0:
                    continue
            paths.append(os.path.join(r, file))
    return paths

if __name__ == '__main__':
    multiprocessing.freeze_support()

    parser = argparse.ArgumentParser(description='Get All DICOM Paths')
    parser.add_argument('-i', '--input-path', type=str, required=True, help='input path of original files')
    parser.add_argument('-f', '--file-ext', nargs='*', type=str, help='file extentions of input directory')

    _args = parser.parse_args()

    if os.path.isdir(_args.input_path):
        setattr(_args, 'input_dir', os.path.normpath(_args.input_path))
        _paths = get_all_dcm_paths(_args.input_path, _args.file_ext)
        if not _paths:
            for file_ext in _args.file_ext:
                print(os.path.join(_args.input_path, '*' + file_ext))
            sys.exit()
        _paths.sort()
        print(_paths)
    elif os.path.isfile(_args.input_path):
        setattr(_args, 'input_dir', os.path.dirname(_args.input_path))
        _paths = [_args.input_path]
    else:
        sys.exit()
