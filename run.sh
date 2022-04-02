read -p "json dir: " json_dir
read -p "tsv dir: " tsv_dir
read -p "reuse: " reuse
if [ $reuse != '--reuse' ]; then
    reuse = ''
fi
read -p 'old version: ' old
read -p 'new version: ' new
read -p 'patch tag: ' tag
python json2tsv.py --version $new --dir $json_dir --save_dir $tsv_dir
python migration.py --ov $old --nv $new --dir $tsv_dir
python mergefont.py --dir $json_dir
python cvttextmgr.py --dir $json_dir $reuse
python applydata.py --ogv $old --ngv $new --kt $tag --jd $json_dir --td $tsv_dir $reuse