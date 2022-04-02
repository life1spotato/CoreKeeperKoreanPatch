import os
import argparse

import pandas as pd
import json
from glob import glob
from tqdm import tqdm

def main(opt):
    ogv, ngv, kt, json_dir, tsv_dir, reuse = opt.ogv, opt.ngv, opt.kt, opt.jd, opt.td, opt.reuse
    
    json_dir = glob(os.path.join(json_dir, 'I2Languages*.json'))[0]
    prev_jsonpath = json_dir + '_prev'
    korpath = os.path.join(tsv_dir, 'ck_kor_trans - v{}.tsv'.format(ogv))

    with open(json_dir if not reuse else prev_jsonpath, 'r') as f:
        jsondata = json.load(f)
    if not os.path.isfile(prev_jsonpath):
        with open(prev_jsonpath, 'w') as f:
            json.dump(jsondata, f)
    kordata = pd.read_csv(korpath, sep='\t').T.values[1:4,:]
    kordata = {term:[enline, krline] for term, enline, krline in zip(*kordata)}
    
    #### To activate langauge (activate: 0, deactivate: 1) ####
    # jsondata['mSource']['mLanguages'][-1] = 0
    
    for terms in tqdm(jsondata.get('mSource').get('mTerms')):
        if terms.get('Term') == 'EarlyAccess':
            terms.get('Languages')[-1] = f'앞서해보기 v{ngv} 한국어화 A{kt}'
            continue
        kd = kordata[terms.get('Term')]
        terms.get('Languages')[-1] = kd[1] if kd[1] != '' else kd[0]

    with open(json_dir, 'w') as f:
        json.dump(jsondata, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='applydata.py')
    parser.add_argument('--ogv', '--old_game_version', type=str, help='old CK version')
    parser.add_argument('--ngv', '--new_game_version', type=str, help='new CK version')
    parser.add_argument('--kt', '--korean_tag', type=str, help='Korean patch tag')
    parser.add_argument('--jd', '--json_dir', type=str, default='.', help='json file dir')
    parser.add_argument('--td', '--tsv_dir', type=str, default='.', help='tsv file dir')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use prev json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)