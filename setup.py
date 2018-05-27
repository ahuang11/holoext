from setuptools import setup

setup(name='holoext',
      version='1.0.1',
      description='Holoviews Extension',
      url='http://github.com/ahuang11/holoext',
      author='Andrew Huang',
      author_email='huang.andrew12@gmail.com',
      license='MIT',
      packages=['holoext'],
      include_package_data=True,
      install_requires=[
                        'matplotlib',
                        'numpy',
                        'pandas',
                        'holoviews',
                        'bokeh',
	  		'dask'
                        ],
      keywords=['data', 'visualization',
                'holoviews', 'bokeh',
                'mod', 'extension',
                'andrew', 'huang'],
      zip_safe=False)
