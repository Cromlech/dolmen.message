# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

version = '0.2.crom'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'cromlech.browser >= 0.5',
    'crom',
    'setuptools',
    'zope.interface',
    'zope.schema',
    ]

tests_require = [
    'pytest',
    ]

setup(name='dolmen.message',
      version=version,
      description="Dolmen messaging machinery",
      long_description="%s\n\n%s\n" % (readme, history),
      keywords='Dolmen Messages',
      author='The Dolmen team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org',
      license='ZPL 2.1',
      namespace_packages=['dolmen'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
