import os
import argparse

import json

from utils import cfg, get_json_path

def main(
        jd,
        reuse
    ):
    target_path = get_json_path(jd, cfg.TargetLang['name'])
    prev_target_path = target_path + '_prev'
    source_path = get_json_path(jd, cfg.FontName)

    with open(target_path if not reuse else prev_target_path, 'r') as f:
        target = json.load(f)
    if not os.path.isfile(prev_target_path):
        with open(prev_target_path, 'w') as f:
            json.dump(target, f)
    with open(source_path, 'r') as f:
        source = json.load(f)

    target.update(cfg.FontData)
    target['m_FontData'] = source.get('m_FontData')

    with open(target_path, 'w') as f:
        json.dump(target, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='mergefont.py')
    parser.add_argument('--jd', '--json_dir', type=str, default='./json', help='json file directory')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use previous json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))