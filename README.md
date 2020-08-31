# obsidian-progress-report

A simple command line app for generating progress report for contributions in the Obsidian vault

## Installation

### Using Pip

```bash
$ pip install obsidian-progress-report
```

### Manual 

```bash
$ git clone https://github.com/aviskase/obsidian-progress-report
$ cd obsidian-progress-report
$ python setup.py install
```

## Usage

Run with defaults (generate report of all created and updated files for the current month and save in vault's root):

```bash
$ obsidian-progress-report <vault>
```

where `vault` is a path to the Obsidian's vault directory.

You can also change defaults:

- `-o <name>` save to subdirectory of vault, for example: `-o Reports`
- `-s 2020-01-04` and `-e 2020-09-05` to change reporting period
- `-i created` or `-i updated` to include only specific sections
- `-c createdAt` for specifying custom frontmatter field on Linux

### Linux

Since there is no robust way to get file creation date on Linux, you must use YAML frontmatter in your markdown files.

By default the script is searching for `created` field, but you can change it with `-c` option. Example:

```
---
created: 2020-08-31T00:05:23
# or created: 2020-08-31

---

# Some note

```

## Report structure

```
# 2020-08-31 – 2020-08-31

## Created

- [[Test note]]


## Updated

- [[Second note]]
- [[Third note]]

```

## Building

Test locally: `python setup.py install`

Create build: `python setup.py sdist bdist_wheel`

Upload build: `twine upload dist/*`
