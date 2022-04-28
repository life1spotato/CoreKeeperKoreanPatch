import os
import argparse

import pandas as pd

from utils import cfg

def main(
        ov,
        nv,
        td
    ):
    ff = os.path.join(td, cfg.EngTsvString)
    older = pd.read_csv(ff.format(ov), sep='\t', index_col=0).T.to_dict('records')[0]
    newer = pd.read_csv(ff.format(nv), sep='\t', index_col=0).T.to_dict('records')[0]

    updated = {'Term': [], 'Languages': []}
    new = {'Term': [], 'Languages': []}
    for nk in newer.keys():
        if older.get(nk):
            if older[nk] != newer[nk]:
                updated['Term'].append(nk)
                updated['Languages'].append(newer[nk])
        else:
            new['Term'].append(nk)
            new['Languages'].append(newer[nk])
    
    pd.DataFrame.from_dict(updated).to_csv(ff.format(nv + '_updated'), sep='\t')
    pd.DataFrame.from_dict(new).to_csv(ff.format(nv + '_new'), sep='\t')

def parse_opt():
    parser = argparse.ArgumentParser(prog='migration.py')
    parser.add_argument('--ov', '--old_version', type=str, help='old CK version')
    parser.add_argument('--nv', '--new_version', type=str, help='new CK version')
    parser.add_argument('--td', '--tsv_dir', type=str, default='./tsv', help='tsv file directory')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))