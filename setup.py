import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'python-decouple',
    'gunicorn',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(name='backhp',
      version='0.0.1',
      description='KUJinaja-sub back API server',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='muskuarede',
      author_email='k.kiyama117@gmail.com',
      url='https://ku-jinja.net',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = backhp:main
      """,
      )
