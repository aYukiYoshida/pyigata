# PyIgata

## Requirements

- poetry

## 諸情報

### 環境設定

- 旧仮想環境準備 ([公式ドキュメント](https://docs.python.org/ja/3/library/venv.html))

    ```bash
    % python3 -m venv venv
    % source ./venv/bin/activate
    % deactivate  # 仮想環境終了
    ```

- with poetry

    ```bash
    % poetry install
    ```

#### docker command

- build

    ```bash
    % docker build -t pyigata -f docker/Dockerfile.pyigata .
    ```

- run

  - run python script

    ```bash
    % docker run [-i] [-t] --rm -v $PWD:/opt/src pyigata [ARGUMENT]
    ```

  - run shell prompt

    ```bash
    % docker run [-i] [-t] --entrypoint /bin/bash --rm -v $PWD:/opt/src pyigata
    ```

#### usage of setup script

If you want to learn more about `setup.py` files, check out [this repository](https://github.com/kennethreitz/setup.py).

- build

    ```bash
    % ./setup.py build
    ```

- install

    ```bash
    % ./setup.py install
    ```

- unit test

    ```bash
    % ./setup.py test
    ```

- clean

    ```bash
    % ./setup.py clean
    ```

- check

    ```bash
    % ./setup.py check
    ```

- generate package

    ```bash
    % ./setup.py sdist
    ```

    Then the package is generated in `dist/`.

#### pre-commit

```bash
% pre-commit --version # verify that the installation was successful
% pre-commit install
```

### check OSS licenses

```bash
% python3 -m venv venv
% source ./venv/bin/activate
% pip install -r requirements.txt
% deactivate
% python3 main.py license \
    --target=./venv/lib/python3.8/site-packages \
    --output=./out/license_list.csv
```

### Run jupyter lab on docker

- build

    ```bash
    % docker-compose build
    ```

- run

    ```bash
    % docker-compose up -d
    ```

- run shell

    ```bash
    % docker-compose exec -u root jupyternbenv bash -p
    ```

- shutdown

    ```bash
    % docker-compose down
    ```

---
