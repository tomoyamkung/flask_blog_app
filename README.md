# flask_blog_app

## 仮想環境

仮想環境は Pipenv を使って作成。Python のバージョンは 3.8.2 とする。

## ソースコードフォーマット

フォーマットは [psf/black](https://github.com/psf/black "psf/black: The uncompromising Python code formatter") に従う。

実行方法は以下の通り：

```sh
$ pipenv run black
All done! ✨ 🍰 ✨
1 file left unchanged.
```

black の設定は pyproject.toml に記述する。


モジュールインポートの順序は [timothycrosley/isort](https://github.com/timothycrosley/isort "timothycrosley/isort: A Python utility / library to sort imports.") に従う。

実行方法は以下の通り：

```sh
$ pipenv run isort
Skipped 1 files
```

isort の設定も pyproject.toml に登録する。

## 文法チェック

文法チェックは [Flake8](http://flake8.pycqa.org/en/latest/index.html "Flake8: Your Tool For Style Guide Enforcement — flake8 3..9 documentation") に従う。

flake8 の実行方法は以下の通り：

```sh
$ pipenv run flake8
./sample.py:22:1: W391 blank line at end of file
```

flake8 の設定は setup.cfg に記述する。

## typehint

typehint のチェックツールとして mypy を採用する。  
mypy の実行方法は以下の通り：

```sh
$ pipenv run mypy
Success: no issues found in 1 source file
```

flake8 の設定も setup.cfg に登録する。

## データベース

データベースには Amazon DynamoDB を使用する。開発時は開発用途で配布されている Docker イメージの DynamoDB ローカルを使用する。

ここでは DynamoDB ローカルの操作について記す。

### DynamoDB ローカルコンテナの起動と停止

Docker イメージを入手する。コマンドは以下の通り。

```sh
$ docker pull amazon/dynamodb-local
```

name を "dynamodb" としてコンテナを起動するコマンドは以下の通り。

```sh
$ docker run -d --rm --name dynamodb -p 8000:8000 amazon/dynamodb-local
```

name を "dynamodb" として起動したコンテナを停止するコンテナは以下の通り。

```sh
$ docker stop dynamodb
```

DynamoDB ローカルへの操作は AWS CLI から行う。
AWS CLI はローカルにインストールする。インストール手順は [macOS での AWS CLI バージョン 2 のインストール - AWS Command Line Interface](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-mac.html "macOS での AWS CLI バージョン 2 のインストール - AWS Command Line Interface") を参照のこと。

念のため、このプロジェクト用の AWS CLI プロファイルを作成した。プロファイル名は "local" とした。コマンドは以下の通り。

```sh
$ aws configure --profile local
AWS Access Key ID [None]: access_key
AWS Secret Access Key [None]: secret_access_key
Default region name [None]: localhost:8000
Default output format [None]:
```

起動した DynamoDB ローカルコンテナに対しての操作は `aws` から行うが、例えば `list-tables` を実行する場合のコマンドは以下の通り。

```sh
$ aws dynamodb list-tables --endpoint-url http://localhost:8000 --profile local
{
    "TableNames": []
}
```

### テーブルの初期化

テーブルを初期化するコマンドは以下の通り。

```sh
$ pipenv run init_db
```

## アプリケーション起動手順

アプリケーションの起動手順は以下の通り。

1. DynamoDB ローカルのコンテナを起動する：`$ aws dynamodb list-tables --endpoint-url http://localhost:8000 --profile local`
2. アプリケーションを起動する：`$ pipenv run run_server`
