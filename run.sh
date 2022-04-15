read -p "json dir: " json
read -p "tsv dir: " tsv
read -p "reuse: " reuse
if [ $reuse != '--reuse' ]; then
    reuse = ''
fi
read -p 'old version: ' old
read -p 'new version: ' new
read -p 'voca version: ' voca
read -p 'patch version: ' patch
python json2tsv.py --v $new --jd $json --td $tsv
python migration.py --ov $old --nv $new --td $tsv
python mergefont.py --jd $json $reuse
python cvttextmgr.py --jd $json $reuse
python applydata.py --vv $voca --gv $new --kv $patch --jd $json --td $tsv $reuse