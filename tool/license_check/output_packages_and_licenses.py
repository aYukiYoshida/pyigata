#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 説明
# ==========
#
# 現在の環境にinstallされているpythonライブラリ情報を、一括出力します
# 出典: http://futago-life.com/wife-support/tech/python-lib-license.html
# format: タブ区切りで下記のライブラリ情報のリストが出力されます
#   name, version, license, repository_url
#
# パラメータ
# ==========
#
# なし
#
################################################################################

import pkg_resources

def get_pkg_license(pkg):
    '''
    pkgで指定するpackageのライセンスを復帰します。
    '''
    try:
        lines = pkg.get_metadata_lines('METADATA')
    except:
        lines = pkg.get_metadata_lines('PKG-INFO')
 
    license = 'UNKNOWN'
    labels = ['License: ', 'Classifier: License :: OSI Approved :: ']
    for label in labels:
        for line in lines:
            if line.startswith(label):
                license = line[len(label):]
                break 
    return license

def get_pkg_home_page(pkg):
    '''
    pkgで指定するpackageのHome Page URLを取得する。
    '''
    try:
        lines = pkg.get_metadata_lines('METADATA')
    except:
        lines = pkg.get_metadata_lines('PKG-INFO')
    label = 'Home-page: '
    for line in lines:
        if line.startswith(label):
            url = line[len(label):]
            break
    return url

def create_packages_and_licenses_text():
    '''
    pythonにインストールされているライブラリの
    「Package名、版数、ライセンス名、Home Page URL」をタブ区切りで出力します。
    '''
    text = ''
    for pkg in sorted(pkg_resources.working_set, key=lambda x: str(x).lower()):
        text += '\t'.join([pkg.key,pkg.version,get_pkg_license(pkg),get_pkg_home_page(pkg)]) + '\n'
    return text
 
if __name__ == "__main__":
    text = create_packages_and_licenses_text()
    print(text)
