import os
import argparse

import json

from utils import cfg, get_json

def main(opt):
    dir, reuse = opt.dir, opt.reuse

    target_path = get_json(dir, cfg.TargetLang['name'])
    prev_target_path = target_path + '_prev'
    source_path = get_json(dir, cfg.FontData['name'])

    with open(target_path if not reuse else prev_target_path, 'r') as f:
        target = json.load(f)
    if not os.path.isfile(prev_target_path):
        with open(prev_target_path, 'w') as f:
            json.dump(target, f)
    with open(source_path, 'r') as f:
        source = json.load(f)

    target['m_LineSpacing'] = cfg.FontData['m_LineSpacing']
    target['m_FontData'] = source.get('m_FontData')
    target['m_Ascent'] = cfg.FontData['m_Ascent']
    target['m_Descent'] = cfg.FontData['m_Descent']
    target['m_FontRenderingMode'] = cfg.FontData['m_FontRenderingMode']

    with open(target_path, 'w') as f:
        json.dump(target, f)

def parse_opt():
    parser = argparse.ArgumentParser(prog='mergefont.py')
    parser.add_argument('--dir', type=str, default='.', help='json file dir')
    parser.add_argument('--reuse', '--use_prev', action='store_true', help='use prev json file')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)