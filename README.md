# PyIgata

## 諸情報

### 環境設定

* 仮想環境準備 ([公式ドキュメント](https://docs.python.org/ja/3/library/venv.html))
    ```shellscript
    % python3 -m venv venv
    % source ./venv/bin/activate
    % deactivate  # 仮想環境終了
    ```

#### docker command

* build
    ```shellscript
    % docker build -t pyigata -f docker/Dockerfile .
    ```
* run
    * run python script
        ```shellscript
        % docker run [-i] [-t] --rm -v $PWD:/opt/src pyigata [ARGUMENT]
        ```
    * run shell prompt
        ```shellscript
        % docker run [-i] [-t] --entrypoint /bin/bash -rm -v $PWD:/opt/src pyigata
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


### check OSS licenses

```shellscript
% python3 -m venv venv
% source ./venv/bin/activate
% pip install -r requirements.txt
% python3 ./tool/license_check/output_packages_and_licenses.py
```

---
