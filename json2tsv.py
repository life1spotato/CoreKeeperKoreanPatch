import os
import argparse

import json
from glob import glob
import pandas as pd
from tqdm import tqdm

def main(opt):
    version, dir = opt.version, opt.dir
    
    filepath = glob(os.path.join(dir, 'I2Languages*.json'))[0]
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    src = data.get('mSource').get('mTerms')
    dst = []

    for terms in tqdm(src):
        element = {}
        element['Term'] = terms.get('Term')
        element['Languages'] = terms.get('Languages')[0].replace('\r','')
        dst.append(element)
    pd.DataFrame(dst).to_csv(os.path.join(dir, f'v{version}.tsv'), index=False, sep='\t')

def parse_opt():
    parser = argparse.ArgumentParser(prog='json2tsv.py')
    parser.add_argument('--version', type=str, help='CK version')
    parser.add_argument('--dir', type=str, default='.', help='json file dir')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)