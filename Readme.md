# Flask REST Api サンプル

## プロジェクトについて

このプロジェクトはFlaskでRest Apiを実装するサンプルです。
Flask-RESTfulを追加しています。

## プロジェクトの取得方法

クローンしてください。
```
git clone https://github.com/FiroProchainezo003/FlaskRestApi
```

## 実行方法

### 共通(pip install)
まず、以下を実行してください。

```
pip install -r requirements.txt

```

### windows(CMD)

```
# Cloneしたフォルダで
> set FLASK_APP=hello
> flask run
 * Running on http://127.0.0.1:5000/
```

### Windows(Powershell)

```
# Cloneしたフォルダで
> $env:FLASK_APP = "hello"
> flask run
 * Running on http://127.0.0.1:5000/
```
### linux(Bash)

```
# Cloneしたフォルダで
$ export FLASK_APP=hello
$ flask run
 * Running on http://127.0.0.1:5000/
```

## 操作方法の概要

サンプルを起動したら http://localhost:5000/debug にアクセスしてください。<br>
http://localhost:5000/ は何も設定していないため、500エラーになります。<br>

http://localhost:5000/debug にアクセスすると、buttonと出力例が並んでいます。<br>

上から以下の通り並んでいます。
- Example1 GET
- Example1 POST (bodyなし)
- Example1 POST (想定通りのbody)
- Example1 POST (想定していないbody)
- Example1 PUT
- Example1 DELETE
- Example2 GET

ボタンを押した出力例がボタンの下に画像で貼り付けてあります。<br>
それぞれのボタンから呼び出されるソースコードは[views/restful_blueprint_module.py]に記載されています。<br>
URLの定義は[app.py]の以下の部分で行っています。<br>

```python
# resource追加
api.add_resource(Example1,
                 f'/api/v1/example1')
api.add_resource(Example2,
                 f'/api/v1/example2/<string:name>')
```

各ボタンを押すと、fetch APIでリクエストが行われます。<br>
このソースコードはブラウザのコードを参照するか、templates/debug.htmlを確認してください。

## pythonバージョン

```
$ flask --version
Python 3.9.7
Flask 2.0.1
Werkzeug 2.0.1

```

## Flaskがサポートしているバージョン

[Installation &#8212; Flask Documentation (2.0.x)](https://flask.palletsprojects.com/en/2.0.x/installation/#python-version)





