from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='bst.pygasus.demo',
      version=version,
      description="Demo package",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Steve Aschwanden',
      author_email='steve.aschwanden@biel-bienne.ch',
      url='',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bb', 'bst.pygasus'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pyaxl',
          'bst.pygasus.core',
          'pyaml',
          'Whoosh',
          'Unidecode'
      ],
      entry_points={
          'fanstatic.libraries': ['demo = bst.pygasus.demo.extjs:library'],
      }
)
