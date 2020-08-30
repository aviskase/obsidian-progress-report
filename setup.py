from setuptools import setup, find_packages

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='obsidian-progress-report',
    description='A simple command line app for generating progress report for contributions in the Obsidian vault',
    version='0.1.1',
    packages=find_packages(),  # list of all packages
    python_requires='>=3.8',
    entry_points='''
        [console_scripts]
        obsidian-progress-report=obsidian_progress_report.__main__:main
    ''',
    author="Yuliya Bagriy",
    long_description=README,
    long_description_content_type="text/markdown",
    license='Unlicense',
    url='https://github.com/aviskase/obsidian-progress-report',
    download_url='https://github.com/aviskase/obsidian-progress-report/archive/0.1.1.tar.gz',
    author_email='aviskase@gmail.com',
    classifiers=[
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ]
)
