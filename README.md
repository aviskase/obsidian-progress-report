# obsidian-progress-report

A simple command line app for generating progress report for contributions in the Obsidian vault

# Installation

## Using Pip

```bash
$ pip install obsidian-progress-report
```

## Manual 

```bash
$ git clone https://github.com/aviskase/obsidian-progress-report
$ cd obsidian-progress-report
$ python setup.py install
```

# Usage

Run with defaults (generate report of all created and updated files for the current month and save in vault's root):

```bash
$ obsidian-progress-report <vault>
```

where `vault` is a path to the Obsidian's vault directory.

You can also change defaults:

- `-o <name>` save to subdirectory of vault, for example: `-o Reports`
- `-s 2020-01-04` and `-e 2020-09-05` to change reporting period
- `-i created` or `-i updated` to include only specific sections

# Building

Test locally: `python setup.py install`

Create build: `python setup.py sdist bdist_wheel`

Upload build: `twine upload dist/*`
