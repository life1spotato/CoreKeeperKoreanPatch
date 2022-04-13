import os
import argparse

import pandas as pd

ff = 'v{}.tsv'

def main(opt):
    global ff
    ov, nv, dir = opt.ov, opt.nv, opt.dir
    ff = os.path.join(dir, ff)
    older = pd.read_csv(ff.format(ov), sep='\t', index_col=0).T.to_dict('records')[0]
    newer = pd.read_csv(ff.format(nv), sep='\t', index_col=0).T.to_dict('records')[0]

    updated = {'key': [], 'element': []}
    new = {'key': [], 'element': []}
    for nk in newer.keys():
        if older.get(nk):
            if older[nk] != newer[nk]:
                updated['key'].append(nk)
                updated['element'].append(newer[nk])
        else:
            new['key'].append(nk)
            new['element'].append(newer[nk])
    
    pd.DataFrame.from_dict(updated).to_csv(ff.format(nv + '_updated'), sep='\t')
    pd.DataFrame.from_dict(new).to_csv(ff.format(nv + '_new'), sep='\t')

def parse_opt():
    parser = argparse.ArgumentParser(prog='migration.py')
    parser.add_argument('--ov', '--old_version', type=str, help='old CK version')
    parser.add_argument('--nv', '--new_version', type=str, help='new CK version')
    parser.add_argument('--dir', type=str, default='.', help='tsv file dir')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)