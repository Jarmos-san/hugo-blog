---
title: "Using GitHub Actions to Deploy a FastAPI Project to Heroku"
date: 2021-05-05T16:25:28+05:30
slug: "using-github-actionst-to-deploy-a-fastapi-project-to-heroku"
category: DevOps
summary:
description:
cover:
  image:
  alt:
  caption:
  relative: false
showtoc: true
draft: true
---

I often build Python projects & host the source code on GitHub repositories. And thanks to [GitHub Actions][GitHub Actions], most of my CI/CD needs are taken care off of as well. And, [Heroku][Heroku] takes care of my deployment needs.

But, Heroku doesn't provide a straightforward way to deploy the project using GitHub Actions. You'll need to download the Heroku CLI for that instead. And it means, additional bloatware on you local machine & more dependencies to take care of. Not a situation I would like to be in & I assume some of you wouldn't either.

Also, do note, similar to how you "_push_" your code to GitHub using [Git][Git], Heroku CLI uses the same technology under the hood. Thus, you would miss out on having a robust CI/CD pipeline keep a quality check on your source code.

Hence, in this article I share how I circumvent around this tricky situation. We'll be using GitHub Actions & FastAPI to deploy a hypotethetical REST API to the Internet. So, without further adieu, let's dive in & learn how to do it.

## Things to Know Before Deployment

Heroku was fundamentally designed wherein the users are expected to push their source code on Heroku version-control system. Hence, it doesn't work well with continuous integration systems like GitHub Actions.

To answer this drawback, Heroku does provide integrated builds on their platform which are triggered on every push to GitHub. And you could even set it up so the build starts only after test suite passes. But, I find it cumbersome & the extra set of work should be avoided in the first place, if possible.

Hence, we'll be using the [`heroku-deploy`][Akhileshns/heroku-deploy] Action by [AkhileshNS][AkhileshNS GitHub Profile]. It's a Node.js application which makes `git` command invocations just as you would while using the Heroku CLI.

Further, to keep things simple & to-the-point, our FastAPI app is a single file with no more than 8 lines of code!

Along with the source code & the Actions's workflow file, Heroku needs some additional files for the build process. A `requirements.txt` & a `runtime.txt` file, the former lists the project dependencies while later pins the exact Python version for the project.

In addition to the above prerequisites, do ensure you've an API key to authenticate the CI/CD pipeline. The `heroku-deploy` Action will use your API key, email address & an optional project name to authenticate & push your code upstream.

And at last, a plain text `Procfile` with these content: `web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000} --workers 4`. Heroku's build process parses this file to set up the web server on the remote machine for your project.

If some of the aforementioned stuff sounds complicated & alien to you, then fret not, the rest of the article describes everything in complete detail.

## Putting Everything Together

### Our Simple FastAPI Project

Let's start briefing the star of our article first. The simple FastAPI project detailed in a `main.py` file. It's a simple REST API that returns JSON reponses to the client. And it has two routes: a `/` (or root) & a `/healthcheck` route.

If you invoke a curl command to the root URL, it simply returns a `{"message": "Hello, World!"`} JSON response. The "_healtcheck_" URL acts as a last-line-of-defense for our project. As long as the project is working as expected, the `/healtcheck` route should return `200` status code along with a JSON response. The `heroku-deploy` Action rolls back to a previous working version if the healthcheck route doesn't return a `200` status code. The JSON response is just an additional feature of the project for human interactions.

So, putting it all together into code, this is what it's supposed to look like:

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.get('/')
def hello_world():
    '''
    The root route which returns a JSON response.

    The JSON response is delivered as:

    {
      'message': 'Hello, World!'
    }
    '''
    return {'message': 'Hello, World!'}

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    '''
    Simple route for the GitHub Actions to healthcheck on.

    More info is available at:
    https://github.com/akhileshns/heroku-deploy#health-check

    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code just enables
    the GitHub Actions to rollback to the last version the project was
    found in a "working condition". It acts as a last line of defense in
    case something goes south.

    Additionally, it also returns a JSON response in the form of:

    {
      'healtcheck': 'Everything OK!'
    }
    '''
    return {'healthcheck': 'Everything OK!'}
```

As you can see, the FastAPI app is nothing fancy & it's kept as such with an intention. So, let's check out our co-star, the GitHub Actions workflow which helps us deploy our project to Heroku.

### Configuring the GitHub Actions Workflow

If you're not aware of GitHub Actions workflows, you write down specific instructions in a [YAML][YAML] file. GitHub reads the instructions to invoke one or more Actions (_like `heroku-deploy`_) on their remote machines. This YAML file is stored under the `.github/workflows` directory & is also pushed to version control.

That said, here's what our workflow file looks like like:

```yml
# This is the .github/workflows/main.yml

name: Deploy    # Name of the workflow

# Events that trigger a workflow:
# https://docs.github.com/en/actions/reference/events-that-trigger-workflows
on: push

jobs:
  test:
  # Include your test suite here.
  lint:
  # Lint & format your code over here.
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Deploying to Heroku
        # More details available at:
        # https://github.com/akhileshns/heroku-deploy
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key:  ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: "<PROJECT-NAME>"
          heroku_email: "<EMAIL-ADDRESS>"
          healthcheck: "https://<PROJECT-NAME>.herokuapp.com/healthcheck"
          rollbackonhealthcheckfailed: true
```

Customize your workflow file based on your needs & requirements. For more information on how to do it, take a look at the official docs at: [docs.github.com/en/actions][GitHub Actions Docs].

That said, let's peruse through the workflow file & see how it works.

At the top of our `main.yml` file is the `name: Deploy` key-value pair which signifies the name of the workflow. Followed by it the `on: push` key-value pair defines how & when the workflow is triggered. You can find a list of events that triggers Actions workflow at: [Events That Trigger Workflows][GitHub Actions Triggers].

The `jobs` section defines what set of Actions will be run signified with the `steps` keyword. And the `runs-on` keyword defines the Operating System to run the set of `jobs` on.

Our simple workflow file has only two Actions for our purpose. The [`checkout`][actions/checkout] Action loads the contents of your repository on GitHub's remote machines. And finally, the `heroku-deploy` is what deploys our project to Heroku.

More specifically, the `heroku-deploy` Action accepts certain required & optional values. The `heroku_api_key`, `heroku_app_name` & the `heroku_email` are compulsory. But, the `healthcheck` & the `rollbackonhealthcheckfailed` value are optional but can benefit our project greatly.

The `healthcheck` value accepts an URL to receive a `200` Status Code. Failing which will make the workflow to exit without completion. On top of it, the `rollbackonhealthcheck` value rolls back to a previous working state in case the previous health check fails.

So, why do we need such complexity in the first place?

You see, in production environments its common to have robust CI/CD pipeline(s) in place. These systems tests your `git` pushes & PR for any potential breakages code quality as well. The healtcheck & roll back features of the deployment process is just there as a last-line-of-defence for the project.

So, in case a bug passes the CI/CD pipeline potentially breaking the app, the healthchecks will just roll back to a previous working state.

### About the `Procfile`, `requirements.txt` & `runtime.txt` Files

Heroku requires any Python projects to have certain files for it's build process. They're plain text files & Heroku's build process parses those files to deploy the project. The text files required by Heroku & the specific purpose they serve are detailed below:

- `Procfile` (_without a file extension_). Heroku reads this file to setup the webserver on the remote machine. So, if you're using [uvicorn][Uvicorn], you should've this web: `uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000} --workers 4` in the file.
- The `requirements.txt` lists out the Python dependencies for your project and Heroku parses this file to install the project's dependencies.
- The `runtime.txt` file states the specific Python version to use for your project. Do note the format for the contents of the file. It looks something like: `Python-3.minor.patch`. So, if you're using `Python 3.8.10`, you should include it as `Python-3.8.10` in the file.

So, if you've followed everything word-to-word till now. You should've a similar directory structure:

```shell
example_project/
├─ .github/
│  ├─ workflows/
│  │  ├─ main.yml
├─ main.py
├─ Procfile
├─ requirements.txt
├─ runtime.txt
```

Now when you push your code to a GitHub repository, it should immediately trigger a workflow. And if everything works as expected & you see a similar build process as the screenshot below? Then you're good to go.

{{ **SHARE SCREENSHOT HERE** }}

You can then check out your FastAPI project deployed on the `<PROJECT-NAME>.herokuapp.com` URL. Perform a `curl` request to it & you should receive a `{"message: "Hello, World!}` JSON response back!

And you did all that without installing Heroku CLI on your local machine. On top of it, now you can even have one or more robust test suites & code quality checks before deploying the project to production. And all of it will be taken care of by GitHub Actions! :grinning_squinting_face:

## Some Potential Road Blocks

While the techniques & code detailed out in this article work, it's not robust enough. There're a couple of fragile areas in the "_heroku-deploy_" Action source code & prone to breaking. This is so because the author of the said Action is [invoking actual `git` commands using NodeJS][Heroku Deploy Action: Source Code #L19].

But, NodeJS wasn't meant to invoke shell commands. No wonder things can & will break while using it. So, in other words, the Action used with here is more of a workaround than anything else!

A better solution to this problem would be to wrap an API provided by Heroku to create a GitHub Action. And fortunate for us, there's some light at the other end of this tunnel. Heroku does provide an official API to interact with their services & infrastructure. And, they named it [Heroku Platform API][Heroku Platform API].

Heroku even went all out & shared an article to [programmatically release code to Heroku][Using Platform API to Release Code to Heroku] using Platform API. So, JavaScript developers, if your reading this & you've experience developing GitHub Actions, the community needs your help.

And, until someone provides a more robust solution to this problem, this article should be a good guideline for anyone wanting to deploy their FastAPI app to Heroku. Or you could try other similar altenatives like Google Serverless Infrastructure. You can find out more on the same in this article: [Google Serverless Infrastructure: A Primer on GCP & Serverless Computing](../details-of-google-serverless-computing/)

<!-- ! Reference Links -->
[Uvicorn]: https://www.uvicorn.org/
[GitHub Actions]: https://github.com/features/actions
[Using Platform API to Release Code to Heroku]: https://blog.heroku.com/programmatically_release_code_to_heroku_using_the_platform_api
[Heroku Platform API]: https://devcenter.heroku.com/articles/platform-api-reference
[Heroku Deploy Action: Source Code #L19]: https://github.com/AkhileshNS/heroku-deploy/blob/79ef2ae4ff9b897010907016b268fd0f88561820/index.js#L19
[actions/checkout]: https://github.com/actions/checkout
[GitHub Actions Triggers]: https://docs.github.com/en/actions/reference/events-that-trigger-workflows
[GitHub Actions Docs]: https://docs.github.com/en/actions
[YAML]: https://yaml.org/
[Akhileshns/heroku-deploy]: https://github.com/akhileshns/heroku-deploy
[AkhileshNS GitHub Profile]: https://github.com/AkhileshNS
[Git]: https://git-scm.com/
[Heroku]: https://www.heroku.com
