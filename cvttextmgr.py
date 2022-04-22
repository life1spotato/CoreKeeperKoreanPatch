import os
import argparse

import json

from utils import cfg, get_json_path

def main(
        jd,
        reuse
    ):
    mgr_path = get_json_path(jd, 'TextManager')
    prev_mgr_path = mgr_path + '_prev'

    with open(mgr_path if not reuse else prev_mgr_path, 'r') as f:
        mgr = json.load(f)
    if not os.path.isfile(prev_mgr_path):
        with open(prev_mgr_path, 'w') as f:
            json.dump(mgr, f)

    mgr['thaiFontSmallDynamic'].update(cfg.TextManagerData['thaiFontSmallDynamic'])

    with open(mgr_path, 'w') as f:
        json.dump(mgr, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='cvttextmgr.py')
    parser.add_argument('--jd', '--json_dir', type=str, default='./json', help='json file dir')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use prev json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))