from pyramid.config import Configurator

from backhp.resources import MyRequest


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # Config の設定を付与してくれるクラス
    config = Configurator(settings=settings)
    # 静的ファイルのマッピング
    config.add_static_view('static', 'static', cache_max_age=3600)
    # URLの付与
    config.add_route('home', '/')
    config.set_request_factory(MyRequest)
    # jinja2 テンプレートローダー
    config.include('pyramid_jinja2')
    # 設定のスキャン(反映)
    config.scan()
    # wsgiに
    return config.make_wsgi_app()
