# Generate difference JSON/YAML files

[![Actions Status](https://github.com/AlexanderPotapkov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/AlexanderPotapkov/python-project-lvl2/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2cbbc8cb7a04654b7223/maintainability)](https://codeclimate.com/github/AlexanderPotapkov/python-project-lvl2/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2cbbc8cb7a04654b7223/test_coverage)](https://codeclimate.com/github/AlexanderPotapkov/python-project-lvl2/test_coverage)

Gendiff is utility for finding differences between configuration files.

## Features

- Suppported formats: YAML, JSON
- Report generation as plain text, structured text or JSON
- Default format: stylish

### Installation

```
    pip install "git+https://github.com/AlexanderPotapkov/python-project-lvl2.git"
```

### For help

```
    gendiff -h
```

<a href="https://asciinema.org/a/522983" target="_blank"><img src="https://asciinema.org/a/522983.svg" /></a>

### To run the utility

For difference in `stylish` format:

```
    gendiff path/to/file1.json path/to/file2.json
```

or

```
    gendiff path/to/file1.yaml path/to/file2.yaml
```

For difference in `plain` format:

```
    gendiff - f plain path/to/file1.json path/to/file2.json
```

or

```
    gendiff - f plain path/to/file1.yaml path/to/file2.yaml
```

For difference in `json` format:

```
    gendiff - f json path/to/file1.json path/to/file2.json
```

or

```
    gendiff - f json path/to/file1.yaml path/to/file2.yaml
```

### Flat JSON/YAML files

<a href="https://asciinema.org/a/522986" target="_blank"><img src="https://asciinema.org/a/522986.svg" /></a>

### Nested JSON/YAML files

<a href="https://asciinema.org/a/522989" target="_blank"><img src="https://asciinema.org/a/522989.svg" /></a>

### Plain JSON/YAML

<a href="https://asciinema.org/a/522992" target="_blank"><img src="https://asciinema.org/a/522992.svg" /></a>

### JSON format

<a href="https://asciinema.org/a/522993" target="_blank"><img src="https://asciinema.org/a/522993.svg" /></a>
