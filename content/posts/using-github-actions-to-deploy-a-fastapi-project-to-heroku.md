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

I often build Python projects & host the source code on GitHub repositories. And thanks to [GitHub Actions](https://github.com/features/actions), most of my CI/CD needs are taken care off of as well. And, [Heroku](https://www.heroku.com) takes care of my deployment needs.

But, Heroku doesn't provide a straightforward way to deploy the project using GitHub Actions. You'll need to download the Heroku CLI for that instead. And it means, additional bloatware on you local machine & more dependencies to take care of. Not a situation I would like to be in & I assume some of you wouldn't either.

Also, do note, similar to how you "_push_" your code to GitHub using [Git](https://git-scm.com/), Heroku CLI uses the same technology under the hood. Thus, you would miss out on having a robust CI/CD pipeline keep a quality check on your source code.

Hence, in this article I share how I circumvent around this tricky situation. We'll be using GitHub Actions & FastAPI to deploy a hypotethetical REST API to the Internet. So, without further adieu, let's dive in & learn how to do it.

## Things to Know Before Deployment

Before we proceed ahead with the rest of the article, let's check out what resources do we need first:

- A GitHub Action named [heroku-deploy](https://github.com/akhileshns/heroku-deploy) by [AkhileshNS](https://github.com/AkhileshNS).
- A repository containing your FastAPI project's source code among other files needed for deployment.
- A Heroku account (_which we'll need for the API key among other things_).

These are the bare minimum number of prerequisites you'll definitely need to deploy your project to Heroku.

GitHub Actions are triggered based on certain events which in turn perform certain tasks based on a set of of instructions. These instructions are laid out in a YAML file which is placed under `.github/workflows/<WORKFLOW-FILENAME.yml>` of the source code repository. In a later section of the article, we'll look into what to include in this article.

Moving on, the repository also holds the source code of your FastAPI project. And for a simple description's sake, we'll keep the source code of the said project small enough. We'll name it `main.py` & we'll share the contents of the article soon enough.

We'll also require a Heroku account, obviously! And to authenticate to the account on a remote machine, we'll also require an API key, the email address you used to login to the Heroku & the name of the project (_optional as you'll see soon_).

Besides the aforementioned prerequisites, Heroku also needs some more files to build & deploy your project on their infrastructure. They are as follows:

- A plain-text `Procfile` without a file extension. Heroku reads this file to setup the webserver for your project on their infrastructure.
- A `requirements.txt` detailing all the dependencies for your project.
- A `runtime.txt` file stating the Python version to use for your project. State the version of Python your project depends on in the `Python-3.minor.patch` format. You can check what version of Python does your project depend on by typing `python --version` in your terminal.

**Share the GitHub Actions workflow**:

And now, time for the main course of the article; the GitHub Actions workflow file which allows you to deploy your FastAPI project to Heroku.

```yml
# Name of the workflow
name: Deploy

# Events that trigger a workflow:
# https://docs.github.com/en/actions/reference/events-that-trigger-workflows
on: push

jobs:
  # Include additional builds for testing/linting your code
  # It ensures quality control before deploying the project to Heroku
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

And the Python file for our FastAPI project:

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

So, as you can see, our simple FastAPI project is nothing fancy. It's just a plain old "_Hello, World!_" program but with an additional feature. We included a "_healthcheck_" route as the last-line-of-defence in case something goes south & our project breaks.

While you should always have an automated & robust CI/CD pipeline in place for your projects, things can & often break, there's no manoeuvring around it. Hence, the healtcheck route acts as the gatekeeper for your project. The workflow we mentioned above will send a GET request to the healthcheck route on every workflow invocation. And, if for some reason, it doesn't return a `200` response code, the workflow will just rollback to the previous working state of the project.

**Say final words**:

So, I hope now you know how to deploy your FastAPI project to Heroku with GitHub Actions. You no longer have to download Heroku's CLI tool on your local machine. And you also don't have to worry about server management stuff! All you got to do is work on maintaining & developing your project with FastAPI.

Hence, I'll be looking forward to what you build. And if you think your project is interesting enough & this article helped you make the project to what it is today, then feel free to reach out to me!
