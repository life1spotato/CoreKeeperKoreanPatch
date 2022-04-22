import os
import argparse

import json
import pandas as pd
from tqdm import tqdm

from utils import get_json_path

def main(
        v,
        jd,
        td
    ):
    filepath = get_json_path(jd, 'I2Languages')
    with open(filepath, 'r', encoding='UTF8') as f:
        data = json.load(f)
    
    src = data.get('mSource').get('mTerms')
    dst = []

    for terms in tqdm(src):
        element = {}
        element['Term'] = terms.get('Term')
        element['Languages'] = terms.get('Languages')[0].replace('\r','')
        dst.append(element)
    pd.DataFrame(dst).to_csv(os.path.join(td, f'v{v}.tsv'), index=False, sep='\t')

def parse_opt():
    parser = argparse.ArgumentParser(prog='json2tsv.py')
    parser.add_argument('--v', '--version', type=str, help='new CK version')
    parser.add_argument('--jd', '--json_dir', type=str, default='./json', help='json file dir')
    parser.add_argument('--td', '--tsv_dir', type=str, default='./tsv', help='tsv tile save dir')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))