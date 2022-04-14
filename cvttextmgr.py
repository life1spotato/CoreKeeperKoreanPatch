import os
import argparse

import json

from utils import yd, get_json

def main(opt):
    dir, reuse = opt.dir, opt.reuse

    mgr_path = get_json(dir, 'TextManager')
    prev_mgr_path = mgr_path + '_prev'

    with open(mgr_path if not reuse else prev_mgr_path, 'r') as f:
        mgr = json.load(f)
    if not os.path.isfile(prev_mgr_path):
        with open(prev_mgr_path, 'w') as f:
            json.dump(mgr, f)

    mgr['thaiFontSmallDynamic']['size'] = yd.TextManagerData['thaiFontSmallDynamic']['size']
    mgr['thaiFontSmallDynamic']['lineSpacing'] = yd.TextManagerData['thaiFontSmallDynamic']['lineSpacing']
    mgr['thaiFontSmallDynamic']['letterSpacing'] = yd.TextManagerData['thaiFontSmallDynamic']['letterSpacing']

    with open(mgr_path, 'w') as f:
        json.dump(mgr, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='cvttextmgr.py')
    parser.add_argument('--dir', type=str, default='.', help='json file dir')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use prev json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)