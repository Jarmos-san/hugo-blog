---
title: A Standard	& Complete CI/CD Pipeline for Most Python Projects
date: "2021-01-21"
category: Programming
slug: a-standard-ci-cd-pipeline-for-python-projects
summary: The most complete (yet standard) CI/CD pipeline you'll ever find for most of your Python projects. Now spend more time on maintaining your project rather than fixing CI/CD issues.
description: The most complete (yet standard) CI/CD pipeline you'll ever find for most of your Python projects. Now spend more time on maintaining your project rather than fixing CI/CD issues.
cover:
    image: "covers/pipeline.png"
    alt: "GitHub services coupled with Poetry is a life saver"
    caption: "Use GitHub Actions + Poetry & Chill!"
    relative: true
showtoc: true
---

Have you ever spent ages tinkering with CI/CD tools rather than work on writing code for your Python project?

I sure did! There were times [Poetry](https://python-poetry.org/) couldn't install dependencies due to virtual environments. Or other times, the dependencies wouldn't just cache for some reasons. On top of that, CI/CD tools are difficult to debug dude to obscure error messages.

Hence, I'm sharing this GitHub Actions workflow which I use with most of my Python projects. It works right out-of-the-box without any tinkering & sets you on the right path to publishing your project. The workflow is very minimal yet doesn't compromise on some of the most major CI/CD principles required for maintaining optimal coding standards. Keeping it minimal also means, you're free to build upon it for further changes & improvements.

That said, here're what you get with this workflow, out-of-the-box without any changes:

- Linting & code formatting with `pylint`, `Black` & `isort` on all PRs & pushes to the remote repository.
- Running integrated test suites for catching any breaking changes before merging the PR.
- Caching dependencies for faster workflow execution times.
- Uploading coverage reports to [CodeCov](https://about.codecov.io/) for following coverage reports.

So, as you can see, the workflow doesn't do much but ensure the bare minimum CI/CD principles are taken care of. And, best of all, you can build upon it as you'll soon see.

## About the Workflow

Python's package management scene isn't praiseworthy (**sources**: [[1]](https://news.ycombinator.com/item?id=19989188) & [[2]](https://news.ycombinator.com/item?id=10000479)). And coupled with those packaging issues, due to virtualenv requirements, setting up CI/CD tools are quite complicated as well (on GitHub Actions at least). So, I scourged through the Internet to come up with the most optimal CI/CD setup for Python projects. While Poetry, out-of-the-box is a great CLI tool for local development, it doesn't work well with CI/CD platforms. With Poetry, you can manage local virtualenvs as easily as publishing your project on PyPi right from your terminal!

But that's manual labour. And as developers, we commit often & push to remote repositories on regular intervals. Repeated manual tasks are subject to mistakes thus increasing the chances of a bug or breaking changes creeping into the project. Hence, I set out with a goal to resolve this issue without spending too much time setting up CI/CD tools.

The goal was to make the setup as simple & minimal as possible, yet should qualify to meet the modern standards of CI/CD principles.

In other words, the setup should be able to perform linting and/or formatting tasks, run the test suites, generate coverage reports & upload the report to CodeCov. And those were the tasks, the setup **should have at the minimum**. Hence, the principles of minimalism were kept in mind.

I also assume most projects are hosted on GitHub repositories so the setup works **ONLY** with [GitHub Actions](https://docs.github.com/en/actions). And in case you're looking to use other CI/CD platforms like [Travis CI](https://www.travis-ci.com/)/[CircleCI](https://circleci.com/), then you might want to look elsewhere.

That said, you can copy the code snippets shared below in an aptly named `<NAME-OF-THE-WORKFLOW>.yml` under the `.github` directory of your project. For example, I usually name the file like `test_suite.yml`. GitHub can identify your workflow files from there automatically. Once you push your commits to the remote repository, the workflow should initiate then. You can access it at `https://github.com/<GITHUB-USERNAME>/<PROJECT-NAME>/actions?query=workflow%3A%22Test+Suite%22`.

That said, here's the code snippet for the CI/CD pipeline. Feel free to copy+paste it. 😉

```json
name: Test Suite

on: [pull_request, push]

jobs:
  linter:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v2.3.4
      - name: Set up python
        uses: actions/setup-python@v2
      - name: Load cache (if exists)
        uses: actions/cache@v2.1.3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip
          restore-keys: ${{ runner.os }}-pip
      - name: Install Black, Pylint & iSort
        run: python -m pip install black pylint isort
      - name: Run linters
        run: |
          pylint alokka
          black .
          isort .

  test:
    needs: linter
    strategy:
      fail-fast: true
      matrix:
        os: ["ubuntu-latest", "macos-latest", "windows-latest"]
        python-version: ["3.8", "3.9"]
    defaults:
      run:
        shell: bash
    runs-on: ${{ matrix.os }}
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2.3.4
      - name: Set up Python v${{matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version}}
      - name: Install Poetry
        uses: snok/install-poetry@v1.1.1
        with:
          virtualenvs-create: true
          virtualenvs-in-project: true
      - name: Load Cached Virtualenv
        id: cached-pip-wheels
        uses: actions/cache@v2.1.3
        with:
          path: ~/.cache
          key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}
      - name: Install dependencies
        run: poetry install --no-interaction --no-root -vvv
      - name: Install Aurochs
        run: poetry install --no-interaction
      - name: Run tests
        run: |
          source $VENV
          pytest -vvv --cov-report xml --cov=./
      - name: Upload coverage
        uses: codecov/codecov-action@v1.2.1
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          file: coverage.xml
          fail_ci_if_error: true
```

## Brief Overview of What the Workflow Does

If you're impatient like me & would like to skim through the article, here's what you should know:

- The workflow executes on PR & push events. As in when someone makes a PR, the `Test Suite` workflow will run. The same happens when you push you local commits to the remote repository.
- The workflow consists of two jobs: `linter` & `test`. The latter of which is dependent on the former. So if `linter` fails, execution of `test` will be skipped.
- `linter` runs on an Ubuntu VM & installs `pylint`, `Black` & `isort` for linting & formatting the code. They're also cached for decreasing the execution times.
- `test` runs on a MacOS, an Ubuntu & a Windows VM with Python versions - `3.8` & `3.9` respectively. Do note, these runs happen in parallel irrespective of each other's execution state.
- The `test` job will also cache & install the virtualenv stored under the `.venv` directory. And then run the test suites with PyTest which generates a `coverage.xml` report to be uploaded to CodeCov.

So, as you can see, even if the workflow is kept as minimal as possible, it still accomplishes a lot of tasks. In fact, most of these tasks are indispensable for maitaining the minimum quality standards for your projects.

Anyway, with a brief overview of what the workflow does, let's take a deeper look into what each line of code was written for. The next section describes it in as much details as possible.

## In-depth Explanation of the Workflow

Right at the top of the file is the `name: Test Suite` key-value pair. It describes the name of the workflow which GitHub shows in it's web UI. The succeeding line, `on: [pull_request, push]` pair describes the events that should trigger the workflow.

The `jobs:` section describes different jobs that should run in parallel (not neccessarily, more on it later). Being a minimalist, this workflow describes two jobs: a `linter` & a `test`. The names of the jobs are kept self-descriptive intentionally. As mentioned in the previous section, `linter` performs linting actions when some code is pushed to the repository or a PR is created. While the `test` job initiates the array of tests on the code pushed or in a PR.

That said, each job has to be assigned an operating system which is assigned with the `runs-on:` keyword. While these [jobs run in parallel](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategymax-parallel), they can be made dependent on another. Hence, they can also be stopped prior to completion if a dependent job failed earlier for some reasons.

Now for the interesting part. The `steps:` key describes what/which workflow/commands to execute. So, the `linter` job executes a [Git Checkout](https://github.com/actions/checkout) first, then sets up an appropriate version of Python in the succeeding step.

The next couple of steps involves caching dependencies for decreased workflow execution time. The [actions/cache](https://github.com/actions/cache) Action loads the dependencies if they've been cached earlier. It also identifies the correct cache with a signed key.

If the dependencies aren't loaded from the cache, then `pip` installs `Black`, `pylint` & `isort` for linting purposes.

The final step for the `linter` job is to execute the aforementioned linting & formatting tools. `Pylint`, `Black` & `isort` has sensible defaults, hence they're passed without any additional arguments. While you could replace `Pylint` with `Flake8` but I feel the latter needs some configuration to make the most out of it especially for an open-source project.

And finally coming to the `test` job. This job mirrors the previous `linter` job to an extent as you'll see soon enough.

Right off the bat, using the `needs:` key, the job is said to be dependent on the completion of the `linter` job. Thus, `test` willn't execute in parallel but will also not execute if `linter` fails. The fast fail option is enabled with the `fail-fast: true` pair.

In addition to the above strategy, this job is set to run on multiple OS platforms with multiple versions of Python. This is set with the `matrix:` key which has `os` & `python-version` has its values. The `os` & `python-version` values accept an array each, of the OS & the Python versions respectively.

The next line sets the default shell for the virtual environment the workflow should run.

And as mentioned earlier each workflow has to assigned an OS to run on with the `runs-on` keyword. The `runs-on` key for the `test` job accepts a variable which will iterate through each of the values set under `matrix.os`. Thus, allowing the workflow to run multiple instances of the ensuing steps for different OSes & Python versions!

The following next two steps is pretty similar to how `linter` started it's execution process but with a caveat. Based on the values set up under `matrix.python-version`, each OS instance will have one Python instance as well.

Now, instead of installing `pip` as was the case in `linter`, the workflow installs Poetry using the `[snok/install-poetry](https://github.com/snok/install-poetry)` Action. It configures Poetry to setup virtualenvs inside the project directory which can then easily cached in the next step.

The Cache action caches the whole virtualenv instead of the dependencies. Hence, Poetry installs the dependencies only if the cached `.venv` wasn't restored.

Following that, the `.venv` is activated & `pytest` then runs the test suite. The arguments passed to `pytest` ensures maximum verbosity for debugging & reporting the output in a `.xml` file format in the root directory. The generated report then uploads the file to [CodeCov](https://about.codecov.io/) using the [`codecov/codecov-action`](https://github.com/codecov/codecov-action).

The CodeCov Action accepts an API token that you'll have to copy & pass in as a [Secret](https://docs.github.com/en/actions/reference/encrypted-secrets) Environment Variable. The CodeCov token can be found at `https://codecov.io/gh/<GITHUB-USERNAME>/<PROJECT-NAME>` (for projects hosted on GitHub). And finally, at the end, the CodeCov Actions is set to fail if it errors out.

The workflow at it's full glory isn't as minimal as it sounds. It's complexity comes with the fact that production-grade software should be thoroughly tested & formatted by following standards, if your project is open-source. Even then, there's still a lot of room for further improvements & changes. And the next section looks into how you further build upon this workflow.

## Room for Further Improvements

As mentioned countless other times, the pipeline is kept minimalistic with an intention: _Keep room for further changes and/or improvements_.

Tthere're a ton more changes/improvements that can be made as per one's requirements. Some such improvements that I can think of over my head are:

- Enable a `release` event wherein the package is tested, formatted, linted, built & then uploaded to PyPi with Poetry.
- Considering scalability, the linters & code formatters can be run in parrallel instead of the sequential runs.
- Tag & update a `CHANGELOG.md` file upon `release`.

And many more. The possibilities are endless & only limited by the project & individual maintainer's requirements.

But all said & done, the code shared here should suffice for most open-sourced Python projects on GitHub.

And if you feel I missed something out then reach out to me on [Twitter](https://twitter.com/Jarmosan), [Email](mailto:somraj.mle@gmail.com) and/or [Ask Me Anything](https://github.com/Jarmos-san/Jarmos-san/discussions/categories/q-a).
