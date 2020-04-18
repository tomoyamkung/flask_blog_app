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
