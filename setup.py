import os
from setuptools import setup, find_packages

version = '0.1'

readme = open('README.txt').read()
changes = open(os.path.join('docs', "HISTORY.txt")).read()

long_description = "%s\n\n%s\n" % (readme, changes)

install_requires = [
    'cromlech.io',
    'grokcore.component',
    'setuptools',
    'zope.component',
    'zope.interface',
    'zope.schema',
    ]

tests_require = [
    'cromlech.browser [test]',
    'zope.testing',
    ]

setup(name='dolmen.message',
      version=version,
      description="Dolmen messaging machinery",
      long_description=long_description,
      keywords='Dolmen Messages',
      author='Dolmen Team',
      author_email='',
      url='http://dolmen-project.org',
      license='ZPL 2.1',
      namespace_packages=['dolmen'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = dict(test=tests_require),
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
        ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
