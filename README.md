# PyIgata

## 諸情報

### 環境設定

* 仮想環境準備
    ```
    % virtualenv venv
    % source ./venv/bin/activate
    % deactivate  # 仮想環境終了
    ```
If you want to learn more about `setup.py` files, check out [this repository](https://github.com/kennethreitz/setup.py).

* build
    ```
    % ./run.sh --setup build
    ```
* install
    ```
    % ./run.sh --setup install
    ```
* unit test
    ```
    % ./run.sh --setup test
    ```
* clean
    ```
    % ./run.sh --setup clean
    ```
* check
    ```
    % ./run.sh --setup check
    ```
* generate package
    ```
    % ./run.sh --setup sdist
    ```
    The package is generated in dist/

---
