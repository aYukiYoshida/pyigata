#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 説明
# ==========
#
# output_packages_and_licenses.pyで作成したライブラリ情報一覧ファイルをパースし、
# 指定されたconfigファイルで許可されていないライセンスのライブラリがないかをチェックします。
#
# パラメータ
# ==========
#
# 1. パース対象のライセンス一覧ファイルパス
#    e.g.) pip_licenses.txt
# 
# 2. configファイルパス
#    使用を許可するライセンスや、確認済みのライブラリの設定が書かれたconfig fileのパス
#    e.g.) ../license_check_config.yml
#
# 返却値
# ==========
#
# exit 0: warningなしの場合
# exit 1: warningありの場合
#
################################################################################

import sys
import yaml
import pprint

if len(sys.argv) < 3:
    print('Insufficient number of arguments.')
    sys.exit(1)
target_path = sys.argv[1]
config_path = sys.argv[2]

with open(config_path, 'r') as f:
    config = yaml.load(f)

libraries = {}
warnings = {}

with open(target_path, 'r') as f:
    for line in f:
        if len(line.rstrip().split("\t")) == 4:
            name = line.rstrip().split("\t")[0]
            license = line.rstrip().split("\t")[2]
            libraries[name] = license

for library in libraries:
    if libraries[library] in config['allowed']:
        continue
    if library in config['reviewed']['pip']:
        continue
    if library in config['ignored']['pip']:
        continue
    warnings[library] = libraries[library]

# output result
print('warnings:')
pprint.pprint(warnings)
result = 'RESULT: ' + str(len(libraries)) + ' dependencies checked, ' + str(len(warnings)) + ' warnings found.'
print(result)

# judge
if len(warnings) > 0:
    print('license check failed.')
    sys.exit(1)
