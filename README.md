# test2

[![Build Status](https://github.com/bbridge0200/test2/workflows/Build%20Main/badge.svg)](https://github.com/bbridge0200/test2/actions)
[![Documentation](https://github.com/bbridge0200/test2/workflows/Documentation/badge.svg)](https://bbridge0200.github.io/test2/)
[![Code Coverage](https://codecov.io/gh/bbridge0200/test2/branch/main/graph/badge.svg)](https://codecov.io/gh/bbridge0200/test2)

test2

---
## Features

-   Store values and retain the prior value in memory
-   ... some other functionality

## Installation

**Stable Release:** `pip install test2`<br>
**Development Head:** `pip install git+https://github.com/bbridge0200/test2.git`

## Documentation

For full package documentation please visit [bbridge0200.github.io/test2](https://bbridge0200.github.io/test2).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

## The Commands You Need To Know

1. `make install`

    This will setup a virtual environment local to this project and install all of the
    project's dependencies into it. The virtual env will be located in `test2/venv`.

2. `make test`, `make fmt`, `make lint`, `make type-check`, `make import-sort`

    Quality assurance

3. `pip install -e .[dev]`

    This will install your package in editable mode with all the required development
    dependencies.

4. `make docs`

    This will generate documentation using sphinx. 

5. `make publish` and `make publish-snapshot`

    Running this command will start the process of publishing to PyPI

6. `make bumpversion' - [release, major, minor, patch, dev]
    
    update verisoning with new releases 

7. `make clean`

    This will clean up various Python and build generated files so that you can ensure
    that you are working in a clean workspace.



#### Suggested Git Branch Strategy

1. `main` is for the most up-to-date development, very rarely should you directly
   commit to this branch. GitHub Actions will run on every push and on a CRON to this
   branch but still recommended to commit to your development branches and make pull
   requests to main. If you push a tagged commit with bumpversion, this will also release to PyPI.
2. Your day-to-day work should exist on branches separate from `main`. Even if it is
   just yourself working on the repository, make a PR from your working branch to `main`
   so that you can ensure your commits don't break the development head. GitHub Actions
   will run on every push to any branch or any pull request from any branch to any other
   branch.
3. It is recommended to use "Squash and Merge" commits when committing PR's. It makes
   each set of changes to `main` atomic and as a side effect naturally encourages small
   well defined PR's.

