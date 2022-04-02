import os
import argparse

import json
from glob import glob

def main(opt):
    dir, reuse = opt.dir, opt.reuse

    thai_path = glob(os.path.join(dir, 'ThaiFont*.json'))[0]
    prev_thai_path = thai_path + '_prev'
    galmuri_path = glob(os.path.join(dir, 'Galmuri11*.json'))[0]

    with open(thai_path if not reuse else prev_thai_path, 'r') as f:
        thai = json.load(f)
    if not os.path.isfile(prev_thai_path):
        with open(prev_thai_path, 'w') as f:
            json.dump(thai, f)
    with open(galmuri_path, 'r') as f:
        galmuri = json.load(f)

    print(len(thai['m_FontData']['Array']), len(galmuri.get('m_FontData')['Array']))

    thai['m_LineSpacing'] = 19.2
    thai['m_FontData'] = galmuri.get('m_FontData')
    thai['m_Ascent'] = 17.06
    thai['m_Descent'] = -1.6
    thai['m_FontRenderingMode'] = 2

    with open(thai_path, 'w') as f:
        json.dump(thai, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='mergefont.py')
    parser.add_argument('--dir', type=str, default='.', help='json file dir')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use prev json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)