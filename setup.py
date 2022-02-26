from setuptools import find_packages, setup

setup(
    name='otsumkpy',
    version='2022.2.26',
    description='Create a Python file with the specified format name.',
    author='Otsuhachi',
    author_email='agequodagis.tufuiegoeris@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='Python make file',
    entry_points={
        'console_scripts': [
            'mkpy = mkpy.mkpy:main',
        ],
    },
)
