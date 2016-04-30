from distutils.core import setup
setup(name='scrapysolr',
      version='0.2.0',
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allows you to store scrapy items in a Solr server.',
      author='Dimitrios Kouzis-Loukas',
      author_email='info@scalingexcellence.co.uk',
      url='http://github.com/scalingexcellence/scrapy-solr',
      keywords="scrapy solr",
      py_modules=['scrapysolr'],
      platforms = ['Any'],
      install_requires = ['scrapy', 'pysolr'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
