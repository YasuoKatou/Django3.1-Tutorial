# 概要

このサンプルプログラムは、[Django ドキュメント](https://docs.djangoproject.com/ja/3.1/)の

* [はじめての Django アプリ作成、その 1](https://docs.djangoproject.com/ja/3.1/intro/tutorial01/)
* [はじめての Django アプリ作成、その 2](https://docs.djangoproject.com/ja/3.1/intro/tutorial02/)
* [はじめての Django アプリ作成、その 3](https://docs.djangoproject.com/ja/3.1/intro/tutorial03/)
* [はじめての Django アプリ作成、その 4](https://docs.djangoproject.com/ja/3.1/intro/tutorial04/)
* [はじめての Django アプリ作成、その 5](https://docs.djangoproject.com/ja/3.1/intro/tutorial05/)

までの内容を保存したものです。

## 実行環境

* windows 10 home
* Python 3.8.6 (```python --version```)
* Django 3.1.4 (```python -m django --version```)

## Django コマンドのまとめ

* サイトの作成

  ```django-admin startproject mysite```

* サーバの起動

  ```python manage.py runserver```

* アプリケーションの作成

  ```python manage.py startapp polls```

* データベースの作成

  ```python manage.py migrate```

* Django が提供する APIを使う

  ```python manage.py shell```

* 管理ユーザーを作成

  ```python manage.py createsuperuser```

* テストの実行

  ```python manage.py test polls```

