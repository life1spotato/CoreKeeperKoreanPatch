import os
import argparse

import json
import pandas as pd
from tqdm import tqdm

from utils import get_json

def main(opt):
    version, dir, save_dir = opt.version, opt.dir, opt.save_dir
    
    filepath = get_json(dir, 'I2Languages')
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    src = data.get('mSource').get('mTerms')
    dst = []

    for terms in tqdm(src):
        element = {}
        element['Term'] = terms.get('Term')
        element['Languages'] = terms.get('Languages')[0].replace('\r','')
        dst.append(element)
    pd.DataFrame(dst).to_csv(os.path.join(save_dir, f'v{version}.tsv'), index=False, sep='\t')

def parse_opt():
    parser = argparse.ArgumentParser(prog='json2tsv.py')
    parser.add_argument('--version', type=str, help='CK version')
    parser.add_argument('--dir', type=str, default='.', help='json file dir')
    parser.add_argument('--save_dir', type=str, default='.', help='tsv tile save dir')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)