from setuptools import setup

setup(name='holoext',
      version='0.0.1',
      description='Holoviews Extension',
      url='http://github.com/ahuang11/holoext',
      author='Andrew Huang',
      author_email='huang.andrew12@gmail.com',
      license='MIT',
      packages=['holoext'],
      install_requires=[
                        'matplotlib',
                        'numpy',
                        'pandas',
                        'holoviews',
                        'bokeh'
                        ],
      keywords=['data', 'visualization',
                'holoviews', 'bokeh',
                'mod', 'extension',
                'andrew', 'huang'],
      zip_safe=False)
