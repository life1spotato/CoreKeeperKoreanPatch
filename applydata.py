import os
import argparse

import pandas as pd
import json
from tqdm import tqdm

from utils import cfg, get_json_path

def main(
        vv,
        gv,
        kv,
        jd,
        td,
        reuse
    ):
    
    json_path = get_json_path(jd, 'I2Languages')
    prev_json_path = json_path + '_prev'
    korpath = os.path.join(td, cfg.KorTsvString.format(vv))

    with open(json_path if not reuse else prev_json_path, 'r') as f:
        jsondata = json.load(f)
    if not os.path.isfile(prev_json_path):
        with open(prev_json_path, 'w') as f:
            json.dump(jsondata, f)
    kordata = pd.read_csv(korpath, sep='\t').T.values[1:4,:]
    kordata = {term:[enline, krline] for term, enline, krline in zip(*kordata)}
    
    ti = cfg.TargetLang['index']
    #### To activate langauge (activate: 0, deactivate: 1) ####
    # jsondata['mSource']['mLanguages'][ti] = 0
    
    for terms in tqdm(jsondata.get('mSource').get('mTerms')):
        if terms.get('Term') == 'EarlyAccess':
            terms.get('Languages')[ti] = cfg.EarlyAccessString.format(gv, kv)
            continue
        kd = kordata[terms.get('Term')]
        terms.get('Languages')[ti] = kd[1] if kd[1] != '' else kd[0]

    with open(json_path, 'w') as f:
        json.dump(jsondata, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='applydata.py')
    parser.add_argument('--vv', '--voca_version', type=str, help='localization sheet version')
    parser.add_argument('--gv', '--game_version', type=str, help='new CK version')
    parser.add_argument('--kv', '--patch_version', type=str, help='korean patch version')
    parser.add_argument('--jd', '--json_dir', type=str, default='./json', help='json file dir')
    parser.add_argument('--td', '--tsv_dir', type=str, default='./tsv', help='tsv file dir')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use prev json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))