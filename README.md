# PyIgata

## 諸情報

### 環境設定

* 仮想環境準備 ([公式ドキュメント](https://docs.python.org/ja/3/library/venv.html))
    ```shellscript
    % python3 -m venv venv
    % source ./venv/bin/activate
    % deactivate  # 仮想環境終了
    ```
#### usage of setup script

If you want to learn more about `setup.py` files, check out [this repository](https://github.com/kennethreitz/setup.py).

* build
    ```shellscript
    % ./setup.py build
    ```
* install
    ```shellscript
    % ./setup.py install
    ```
* unit test
    ```shellscript
    % ./setup.py test
    ```
* clean
    ```shellscript
    % ./setup.py clean
    ```
* check
    ```shellscript
    % ./setup.py check
    ```
* generate package
    ```shellscript
    % ./setup.py sdist
    ```
    The package is generated in dist/

---
