---
title: "Using GitHub Actions to Deploy a FastAPI Project to Heroku"
date: 2021-05-05T16:25:28+05:30
slug: "using-github-actions-to-deploy-a-fastapi-project-to-heroku"
category: DevOps
summary: Heroku makes deployment a piece of cake, but compromises on quality control & best practices. So, this article shows how to use GitHub Actions in tandem with Heroku while maintaining best practices.
description: Heroku makes deployment a piece of cake, but compromises on quality control & best practices. So, this article shows how to use GitHub Actions in tandem with Heroku while maintaining best practices.
cover:
  image: https://res.cloudinary.com/jarmos/image/upload/v1620895005/GitHub_Actions_Loves_Heroku_dq2ake.jpg
  alt: Heroku combined with GitHub & GitHub Actions is a match made in heaven.
  caption: GitHub Actions (and GitHub) plus Heroku is a match made in heaven
  relative: false
showtoc: true
draft: false
---

I build Python projects & host the source code on GitHub repositories quite often. And thanks to [GitHub Actions][github actions], I needn't worry about Continuous Integration needs either. While [Heroku][heroku] takes care of my Continuous Deployment needs.

But, there's a problem. Heroku doesn't provide a straightforward way to deploy the project using GitHub Actions. I need to download [Heroku CLI][heroku cli] to do it instead.

And if you've been reading my articles, you would know I'm quite a minimalist. I don't like adding more bloatware & extra dependencies to my development machine than what’s needed. Hence, I had to look out for an alternative.

My current development process is to commit changes on my local machine & then push it to remote. The remote here is usually a GitHub repo with GitHub Actions configured to trigger a suite of tests. And if everything passes, deploy the project to production. Pretty standard practice & nothing fancy over here.

But the caveat is Heroku CLI uses `git` commands to push code to Heroku's remote. So, it's pretty much like pushing code to a GitHub repository. But, with no robust CI/CD pipelines. I could configure Heroku to deploy when the tests pass On GitHub. But it's best to stick to standard practice & configure everything under one roof.

Also, invoking `git` commands on a remote machine doesn't sound like a good idea. So, I felt sharing the techniques I use to circumvent this tricky situation was the right thing to do.

So, we'll be using GitHub Actions to configure a CI/CD pipeline. And, [FastAPI][fastapi] to build our hypothetical REST API.

And, without further adieu, let's dive in & learn how to do it.

## Things to Know Before Deployment

Heroku's design reflects the need for simplicity & reducing complexity. Its users aren't expected to know in-depth CI/CD concepts & practices. But as long as the users are well-acquainted with Git commands, they're good to go.

In other words, deploying a project to Heroku is as simple as pushing your code to GitHub repos!

You would develop your project & then push your code to the Heroku remote. It triggers a build process which sets up a web server on their remote servers. In other words, deploying projects couldn't get any easier than this.

But there's a drawback to this process, Heroku doesn't provide a robust enough CI/CD pipeline. There's no way to keep a check on any breaking changes or bugs. This is where GitHub Actions come in handy.

So, we'll be using the [`heroku-deploy`][heroku deploy action] Action by [AkhileshNS](https://github.com/AkhileshNS) to deploy the project. And the said Action is a NodeJS wrapper around basic `git` command invocations. These invocations are exactly like what you would use with Heroku CLI instead.

Further, to keep things simple & to-the-point, our FastAPI app is a single file with no more than 8 lines of code!

Besides that, Heroku also requires some extra files for the build process to work. And these files are also pushed to the Heroku remote as well. They’re plain-text files with information for Heroku to parse during the build phase. You’ll find more details about them later in the article.

Additionally, the `heroku-deploy` Action also requires an API key for authentication. So, ensure you've it along with the project's name.

And with all the prerequisites taken care of, let's develop the project now.

## Putting Everything Together

### Our Simple FastAPI Project

With all the prerequisites set up & gathered, here’s an overview of our little project.

To start with, the FastAPI project is pretty simple with only 8 lines of code! It's source code is detailed in the `main.py` file. And it’s configured with routes to return a set of JSON responses when queried. The said routes are; a `/` (_or root_) route & a `/healthcheck` route. The latter of which has some significance in our CI/CD pipeline as you'll see.

The root route returns a JSON response like this; `{"message": "Hello, World!"}` when queried. And the `/healtchcheck` route acts as the last-line-of-defense for the REST API. But it also returns a JSON response for better user interpretation. So, if you invoke a `cURL` command to this route, you should get back `{“message”: “Everything, OK!”}` response back.

We'll configure our CI/CD pipeline to query the health-check route to check if it's still up & running. Failing to do so which means returning a `400` (_or similar_) response code will invoke a roll-back. Hence, our REST API in production will always be up & running regardless of any breaking changes or bugs creeping in.

That said, here's what the source code for our REST API will look like:

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

### Configuring the GitHub Actions Workflow

With our REST API built, let's configure a CI/CD pipeline for it. The pipeline is pretty standard & is nothing fancy. On every Push and/or PR event, it'll invoke a series of tests followed by code quality checks. And if everything passes, the workflow will invoke the deployment process as well.

But before discussing more about our pipeline, let's learn a bit about GitHub Actions.

It’s easy to confuse GitHub Actions as "_yet another CI/CD tool_". But, it's not. GitHub defines it as an automation tool for all software development needs one can think of. And, there're many preconfigured Actions provided officially by GitHub and/or the community as well. One such Action we'll use for our use case is the `AkhileshNS/heroku-deploy` Action.

We’ll trigger our workflow on every push event. But you can configure it to trigger on other events as well. You can find more info on the list of [events that triggers a workflow][github actions triggers] it's official documentation.

Workflows are further configured through [YAML][yaml] files. And, they're stored under the `.github/workflows` directory which is also version controlled. GitHub will parse these YAML files for instructions on how to set up the environment.

And here's what our workflow looks like:

```yml
# This is the .github/workflows/main.yml

name: Deploy # Name of the workflow

# Events that trigger a workflow:
# https://docs.github.com/en/actions/reference/events-that-trigger-workflows
on: push

jobs:
  # Check out the following article for more inspiration on setting up a
  # standard CI/CD pipeline for most Python projects:
  # https://jarmos.netlify.app/posts/a-standard-ci-cd-pipeline-for-python-projects/
  test:
  # Include your test suite here.
  lint:
  # Lint & format your code over here.
  deploy:
    # If the test & lint jobs don't pass,
    # the deploy job willn't even execute
    needs: [test, lint]
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Deploying to Heroku
        # More details available at:
        # https://github.com/akhileshns/heroku-deploy
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: "<PROJECT-NAME>"
          heroku_email: "<EMAIL-ADDRESS>"
          healthcheck: "https://<PROJECT-NAME>.herokuapp.com/healthcheck"
          rollbackonhealthcheckfailed: true
```

GitHub Actions workflows have to adhere to a specific syntax. And explaining the syntax is a bit out of context of this article. So, you can refer to the [official docs][github actions syntax] for info to learn about the syntax.

That said, let's understand how we can customize our workflow.

At the top of our `main.yml` file is the name of the workflow signified with the `name` keyword. It's followed by the `on` keyword which instructs GitHub Actions to trigger the workflow on `push` events.

There're way more "_on event_" keywords available to trigger workflows. So, do take a look at the documentation & configure your pipeline according to your needs.

Continuing on, the `jobs` section of the workflow is pretty much the heart of the pipeline. This is where GitHub will find instructions on which Actions to trigger & when. For our needs, we defined 3 jobs & they'll run in parallel unless explicitly configured not to do so.

The jobs are configured to run on the latest version of Ubuntu. And additionally, the `deploy` job is dependent on the other previous jobs. So, while the `test` & `linter` jobs run in parallel, the `deploy` job will wait till they pass. And, if they don't, the `deploy` job willn’t even execute.

This structure of the pipeline ensures bugs are never introduced to production. And hence, ensuring quality standards of the source code. And if you want to know how to set up a code quality check for Python projects, I've an article for you. Check out [A Standard & Complete CI/CD Pipeline for Most Python Projects](../a-standard-ci-cd-pipeline-for-python-projects) to know how to set it up.

Diving deeper into the `deploy` job, let's figure out it's exact purpose.

Like its predecessors, the `deploy` job also runs on the latest version of Ubuntu. Then it instructs GitHub to parse the steps for execution. Accordingly, GitHub "_copies_" the contents of the repo in the virtual environment. Following which the `heroku-deploy` Action is executed.

The `heroku-deploy` Action also requires a couple of variables to function. And these variables are provided using the `with` keyword. The said Action accepts more variables than what we're using. So, do check out it's repo for further configuration.

That said, we're using the `heroku_api_key`, `heroku_app_name`, `heroku_email`, `healthcheck` & `rollbackonhealthcheckfailed` variables. Since, the first 3 variables accept valuable user-info, they're passed in as GitHub Secrets. The `healtcheck` variable accepts an URL to the `/healthcheck` route. And finally, the `rollbackonhealthcheckfailed` accepts a boolean value.

The last variable helps us as the last-line-of-defence. Anytime an event triggers workflow & the project deploys, a health-check will be performed. It'll look for a `200` response code & if it fails, the workflow will revert back to a previous working version!

Pretty nifty if you ask me!

But then, why do we need such complexity in the first place?

You see, in production environments it's common to have robust CI/CD pipeline(s) in place. These systems test your commit pushes & PR for any potential breakages. And not to forget coding best practices & quality standards as well.

The health-check & roll back features of the pipeline are there as a last-line-of-defence. Since, it is possible for bugs and/or breaking changes to pass the preliminary checks. And it could break our REST API in production. Imagine what it would be like for your project’s users (_and they paid for using it_)!

But fortunate for us, you needn't worry about such a scenario ever becoming a reality. With the health-check & roll-back features, issues will turn back north as quickly as it turned south. So, in other words, you get a good night's sleep without any worry.

### About the `Procfile`, `requirements.txt` & `runtime.txt` Files

As mentioned earlier, Heroku requires certain plain-text files during the build process. It parses these files to set up the web-server & the dependencies for the project. So, for our REST API project which is a Python application, following are the files Heroku needs to parse.

- The `Procfile` (_without a file extension_) which Heroku parses to set up a web-server on the remote machine. So, while using uvicorn, the contents of the file would be: `uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000} --workers 4`.
- The `requirements.txt` lists project dependencies. And, Heroku will parse it to install the project's dependencies.
- The `runtime.txt` file states the specific Python version to use for our REST API. So, if it depends on Python v3.8.10, the contents of the file would be `python-3.8.10`. **Do note the format** & it has to be exactly similar else it won't work.

With these files, your build environment on Heroku should be up & running in no time. But let's double check the directory structure before committing things to version-control. Here's what your directory structure should look like:

```shell
example_project/          # Root directory for our project
├─ .github/
│  ├─ workflows/
│  │  ├─ main.yml         # Our Workflow file
├─ main.py                # Our FastAPI project
├─ Procfile               # Instructions for Heroku to setup Uvicorn
├─ requirements.txt       # Lists the dependencies of our project
├─ runtime.txt            # List the Python version our project depends on
```

Now, each time you push your changes to a GitHub repository, the push event will trigger the workflow. And if the tests & code quality checks pass, the workflow will try to deploy the project to Heroku. On top of it, if the health-check URL returns a `200` response code back to our workflow, the REST API goes live!

You can then navigate to the `https://<PROJECT-NAME>.herokuapp.com` URL to check out our REST API. If it’s working you should see a JSON response on the screen.

With this setup, now you’ve the best of both worlds. Simple deployment with Heroku & robust code quality checks with GitHub Actions! And the best part of it all, there was no need to use the Heroku CLI on your local machine. :grinning_squinting_face:

## Some Potential Roadblocks

While the techniques & code detailed out in this article works, it's not robust enough. There're a couple of fragile areas in the `heroku-deploy` Action which need to be taken care of. If you peruse through the source code, you’ll find it's [invoking actual `git` commands][heroku deploy action: source code #l19] using NodeJS.

But, NodeJS wasn't meant to invoke shell commands. So, no wonder things can & will break while using it. In other words, the Action used here is more of a workaround than anything else!

A better solution to this problem would be to wrap an API provided by Heroku to create an Action. And fortunate for us, appears to be some light at the other end of this tunnel. Heroku provides an official API to interact with their build process & other services. They named it [Heroku Platform API][heroku platform api]. They even shared an article to [programmatically release code to Heroku][using platform api to release code to heroku] using their Platform API.

So, a shout-out to JavaScript developers. If you're reading this & you're experienced developing GitHub Actions, the community needs you. But till then, this article should be a good guideline for anyone wanting to deploy their FastAPI app to Heroku.

There are other alternatives though. Google Serverless Infrastructure is one & other provided by Microsoft Azure and/or Amazon Web Service. So, if you want to try them out, check this article I authored Google's Serverless offering. You can read it at: [Google Serverless Infrastructure: A Primer on GCP & Serverless Computing](../posts/google-serverless-infrastructure-what-are-the-differences).

Until then cheers & happy developing! :clinking_beer_mugs:

<!-- ! Reference Links -->

[uvicorn]: https://www.uvicorn.org/
[github actions]: https://github.com/features/actions
[using platform api to release code to heroku]: https://blog.heroku.com/programmatically_release_code_to_heroku_using_the_platform_api
[heroku platform api]: https://devcenter.heroku.com/articles/platform-api-reference
[heroku deploy action: source code #l19]: https://github.com/AkhileshNS/heroku-deploy/blob/79ef2ae4ff9b897010907016b268fd0f88561820/index.js#L19
[actions/checkout]: https://github.com/actions/checkout
[github actions triggers]: https://docs.github.com/en/actions/reference/events-that-trigger-workflows
[github actions docs]: https://docs.github.com/en/actions
[yaml]: https://yaml.org/
[akhileshns/heroku-deploy]: https://github.com/akhileshns/heroku-deploy
[akhileshns github profile]: https://github.com/AkhileshNS
[git]: https://git-scm.com/
[heroku]: https://www.heroku.com
[heroku cli]: https://devcenter.heroku.com/articles/heroku-cli
[fastapi]: http://fastapi.tiangolo.com/
[heroku deploy action]: https://github.com/AkhileshNS/heroku-deploy
[github actions syntax]: https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions
