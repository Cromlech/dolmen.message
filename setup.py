import os
from setuptools import setup, find_packages

version = '0.4.2'

readme = open(os.path.join('src', 'dolmen', 'message', 'README.txt')).read()
changes = open("CHANGES.txt").read()

long_description = "%s\n\n%s\n" % (readme, changes)

install_requires = [
    'setuptools',
    'Beaker',
    'grokcore.component',
    'zope.component',
    ]

tests_require = [
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
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
        ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
