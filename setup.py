from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='itoana27',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': ['templates/*/*/*']},
    install_requires=['django~=3.2'],
    extras_require={
        'ipython': ['ipython==6.21'],
    },
    scripts={
        'typeidea/manage.py'
    },
    entry_points={
        'console_scripts': [
            'typeidea_manage = namage:main',
        ]
    },
    classifiers=[
        'Development Status :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ]
)
