---
Title: A Standard	&#38; Complete CI/CD Pipeline for Most Python Projects
Date: 2021-01-21 15:47
Modified: 2021-01-21 15:47
Category: Programming
Tags: Software Development, Python, GitHub
Authors: Somraj Saha
Slug: a-standard-ci-cd-pipeline-for-python-projects
Summary: The most complete (yet standard) CI/CD pipeline you'll ever find for most of your Python projects. Now spend more time on maintaining your project rather than fixing CI/CD issues.
---

![Python CI/CD Pipeline](./static/images/pipeline.png)

A standard CI/CD pipeline for Python projects. The pipeline serves a minimalistic purpose while maintaining room for further changes as per requirements. Hence, feel free to build upon it. But for most projects, it should suffice as it is right now.

## Further Details

Some background on this setup:

Keeping in mind the principles of minimalism & assuming most projects are hosted on GitHub repositories, this setup works **ONLY** on [GitHub Actions](https://docs.github.com/en/actions). Hence, copy the code snippets shared below in an aptly named `<NAME-OF-THE-WORKFLOW>.yml` under the `.github` directory.

Once you push these contents to the remote repository, the workflow should initiate automatically. You can access it at `https://github.com/<GITHUB-USERNAME>/<PROJECT-NAME>/actions?query=workflow%3A%22Test+Suite%22`.

That said, here's the code snippet for the CI/CD pipeline.

<script src="https://gist.github.com/Jarmos-san/a1f219934fd23ad6b915a37dd85a2864.js"></script>

## What Does the Pipeline Do

From the top, the `name: Test Suite` key-value pair describes the name of the workflow. Followed by which the next `on: [pull_request, push]` pair describes the events that should trigger the workflow.

The `jobs:` section describes different jobs that should run in parallel (not neccessarily, more on it later). Being a minimalist, this workflow describes two jobs: a `linter` & a `test`. The names of the jobs are kept self-descriptive intentionally. Suffice to say, `linter` performs linting actions when some code is pushed to the repository or a PR is created. While the `test` job initiates the array of tests on the code pushed or in a PR.

That said, each job has to be assigned an operating system which is assigned with the `runs-on:` keyword. While these [jobs run in parallel](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategymax-parallel), they can be made dependent on another. Hence, they can also be stopped prior to completion if a dependent job failed earlier for reasons.

Now for the interesting part. The `steps:` key describes what/which workflow/commands to execute. So, the `linter` job executes a [Git Checkout](https://github.com/actions/checkout) first, then sets an appropriate version of Python in the succeeding step.

The next couple of steps involves caching dependencies for lower workflow execution time. The [actions/cache](https://github.com/actions/cache) Action loads the dependencies if they've been cached earlier. It identifies the correct cache with a signed key.

If the dependencies aren't loaded from the cache, then `pip` installs `Black`, `Flake8` & `isort` for linting purposes.

The final step for the `linter` job is to execute the aforementioned linting & formatting tools. `Black` & `isort` has sensible defaults, hence they're passed without any additional arguments. But `flake8` has to be executed with a couple of arguments which will otherwise make it very inefficient.

So, `flake8` is told not to check the `.venv` directory for linting errors & allow a max line length of 85. These configurations are enabled with the `--exclude` & `--max-line-length` flags respectively. Excluding the virtual environment directory is needed because otherwise `flake8` would check the Python `site-packages` for linting errors as well (**which takes a lot of time to finish!**). And max line length is set to 85 because most people use wide monitors (instead of CRTs) these days.

And finally coming to the `test` job. This job mirrors the previous `linter` job to an extent as you'll see soon enough.

Right off, using the `needs:` key, the job is said to be dependent on the completion of the `linter` job. Thus, `test` willn't execute in parallel but will also not execute if `linter` fails. The fast fail option is enabled with the `fail-fast: true` pair.

In addition to the above strategy, this job is set to run on multiple OS platforms with multiple versions of Python. This is set with the `matrix:` key which has `os` & `python-version` has its values. The `os` & `python-version` values accept an array each, of the OS & the Python versions respectively.

The next line sets the default shell for the virtual environment the workflow should run.

And as mentioned earlier each workflow has to assigned an OS to run on with the `runs-on` keyword. The `runs-on` key for the `test` job accepts a variable which will iterate through each of the values set under `matrix.os`. Thus, allowing the workflow to run multiple instances of the ensuing steps for different OSes & Python versions!

The next two steps is pretty similar to how `linter` started it's execution process but with a caveat. Based on the values set up under `matrix.python-version`, each OS instance will have one Python instance as well.

Now, instead of installing `pip` as was the case in `linter`, the workflow installs [Poetry](https://python-poetry.org/) using the `[snok/install-poetry](https://github.com/snok/install-poetry)` Action. It configures Poetry to setup virtualenvs inside the project directory which can then easily cached in the next step.

The Cache action caches the whole virtualenv instead of the dependencies as was the case in `linter`. Hence, Poetry installs the dependencies only if the cached `.venv` wasn't restored.

Following that, the `.venv` is activated & `pytest` then runs the test suite. The arguments passed to `pytest` ensures maximum verbosity for debugging & reporting the output in a `.xml` file format in the root directory. The generated report then uploads the file to [CodeCov](https://about.codecov.io/) using the [`codecov/codecov-action`](https://github.com/codecov/codecov-action).

The CodeCov Action accepts an API token that you'll have to copy & pass in as a [Secret](https://docs.github.com/en/actions/reference/encrypted-secrets) Environment Variable. The token can be found in this URL: `https://codecov.io/gh/<GITHUB-USERNAME>/<PROJECT-NAME>` (for projects hosted on GitHub). And finally, at the end, the CodeCov Actions is set to fail if it errors out.

## Room for Further Improvements

As mentioned earlier, the pipeline is kept minimalistic with an intention: _Keep room for further changes and/or improvements_.

Hence, there're a ton more changes/improvements that can be made as per one's requirements. Some such improvements that can be thought of right away are:

- Enable a `release` event wherein the package is uploaded to PyPi with Poetry.
- Considering scalability, the linters & code formatters can be run in parrallel instead of sequential runs.
- Tag & update a `CHANGELOG.md` file upon `release`.

And many more. The possibilities are endless & only limited by the project & individual requirements. But all said & done, the code shared here should more than suffice for most open-sourced Python projects on GitHub.

Feedback & error reports are welcome. Reach out to me on [Twitter](https://twitter.com/Jarmosan), [Email](mailto:somraj.mle@gmail.com) and/or [Ask Me Anything](https://github.com/Jarmos-san/Jarmos-san/discussions/categories/q-a).
