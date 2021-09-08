from flask import Flask, render_template, jsonify
from flask_restful import Api
from flask_debugtoolbar import DebugToolbarExtension

from views.restful_blueprint_module import Example1, Example2


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret'
# Debug toolbar (/debug 右側メニュー [Route List] 閲覧用)
app.debug = True
toolbar = DebugToolbarExtension(app)


# Error処理
@app.errorhandler(404)
def error_handler(error):
    response = jsonify({'message': 'Page Not Found'})
    return response, error.code


@app.errorhandler(500)
def error_500(error):
    response = jsonify({'message': 'Internal Serer Error'})
    return response, error.code


# Debugページ
@app.route('/debug')
def debug_page():  # put application's code here
    return render_template('debug.html')


# resource追加
api.add_resource(Example1,
                 f'/api/v1/example1')
api.add_resource(Example2,
                 f'/api/v1/example2/<string:name>')


if __name__ == '__main__':
    # ここでは[debug=True]を指定していない。
    # flask_debugtoolbarを使う場合、[debug=True]を指定する必要があるので、
    # [toolbar = DebugToolbarExtension(app)]の近くで設定している。
    app.run()
