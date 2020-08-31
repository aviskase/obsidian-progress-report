from setuptools import setup, find_packages

import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
VERSION = '0.3.0'

setup(
    name='obsidian-progress-report',
    description='A simple command line app for generating progress report for contributions in the Obsidian vault',
    version=VERSION,
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
    download_url=f'https://github.com/aviskase/obsidian-progress-report/archive/{VERSION}.tar.gz',
    author_email='aviskase@gmail.com',
    install_requires=["frontmatter~=3.0"],
    classifiers=[
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ]
)
