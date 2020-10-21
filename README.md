# Somraj's Blog

[![Website](https://img.shields.io/website?down_color=Red&down_message=Down&label=Website&style=flat-square&up_color=Green&up_message=Up&url=https%3A%2F%2Fjarmos.netlify.app%2F)](https://jarmos.netlify.app/) [![Netlify](https://img.shields.io/netlify/2b1ebff7-c584-43c9-9296-277116a5729b?color=00C7B7&label=Netlify%20Build&logo=Netlify&style=flat-square)](https://app.netlify.com/sites/goofy-galileo-0dde5b) [![LinkedIn](https://img.shields.io/static/v1?label=LinkedIn&message=Connect&color=0077B5&style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jarmos/) [![Quora profile](https://img.shields.io/static/v1?label=Quora&message=QnA&color=B92B27&style=flat-square&logo=quora)](https://www.quora.com/profile/Somraj-Saha-3) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20Me-Anything!-1abc9c.svg)](https://github.com/Jarmos-san/ama) [![Twitter Follow](https://img.shields.io/twitter/follow/Jarmosan?style=social)](https://twitter.com/Jarmosan)

This repository hosts the source code for my [personal website](https://jarmos.netlify.app). It's statically generated using [Pelican](https://www.getpelican.com) - A Static Site Generator(SSG) built on Python & is deployed using [Netlify](https://www.netlify.com/).

- [Somraj's Blog](#somrajs-blog)
  - [:checkered_flag: Getting Started](#-getting-started)
    - [:running: The Easy & Quick Way To Get It Done](#-the-easy--quick-way-to-get-it-done)
      - [:nut_and_bolt: Setup a Development Environment](#-setup-a-development-environment)
      - [:dash: Preparing Your Site For Deployment](#-preparing-your-site-for-deployment)
  - [:hammer_and_wrench: Built With](#-built-with)
  - [:building_construction: Contributing](#-contributing)
    - [:eyes: Issues](#-issues)
    - [:package: Pull Request](#-pull-request)
  - [:memo: License](#-license)
  - [:raised_hand: Get Help](#-get-help)
  - [:clap: Acknowledgements](#-acknowledgements)

## :checkered_flag: Getting Started

If you've found my blog somehow on the Internet, got interested in what I say or perhaps you just need an excuse to participate in the open-source community, then your contributions are welcome! A little bit about the website & what I'm trying to maintain;

- A simple, minimal-looking blog with no fluffy UI but mere knowledge-sharing stuff. The simpler interface the better.
- Machine Learning is still a very academy-ey field of application. Recreating experiments & thoughts are had with the fast-moving advancements made every other day. Hence, it's important to provide references to every statement I provide towards the end of each article which is why you'll find a reference section at the end.
- A non-intrusive blog without any on-the-face marketing lingoes.

### :running: The Easy & Quick Way To Get It Done

Anyway perhaps you just like the way my site is set up & would like to have one for yourself ASAP. If that's the case, this section will help you.

#### :nut_and_bolt: Setup a Development Environment

1. Fork the repository.
2. Clone your copy of the repository locally using the command `git clone git@github.com:<INSERT_YOUR_USERNAME_HERE>/blog.git`.
3. Remove the files under the directory `content`. Note, the files are written in [reStructured Text](https://docutils.sourceforge.io/rst.html) which is basically Markdown with super powers!
4. Create a virtual environment by running `python -m venv .venv`. Then install the dev requirements using the command `pip install dev-requirements.txt`. Optionally, if you prefer writing your articles in Markdown instead, the [Pelican docs suggests](https://docs.getpelican.com/en/stable/install.html#optional-packages) installing Markdown support using the `python -m pip install "pelican[markdown]"` command.
5. Remove the unnecessary settings from the `pelicanconf.py` file as per your needs & requirements.

#### :dash: Preparing Your Site For Deployment

1. Write your articles under the `content` directory & then check if its generated properly by running the `invoke serve` command. The `tasks.py` has lots of efficient CLI commands for automating your development process. Some of them are listed below, do check them out!

     - `.. clean` - Remove generated files from the `output` directory.
     - `.. build` - Build a local version of the site. The generated files are stored under the `output` directory.
     - `.. rebuild` - Build with the deleted switch.
     - `.. regenerated` - Automatically regenerate site upon file modification.
     - `.. serve` - Serve the generated site at localhost:8000 (_by default, you can change the host & port though_).
     - `.. reserve` - Build the site first under `output` & the serve it.
     - `.. preview` - Build production version of the site.
     - `.. livereload` - Automatically reload the browser tab upon file modification.
     - `.. publish` - Publish the file via `rsync` perhaps onto a S3 bucket.

**Replace `..` with `invoke`.*

2. Push your changes to GitHub.
3. Create/login into an account on [Netlify](https://www.netlify.com).
4. Link a remote repository by clicking on the "[New site from Git](https://app.netlify.com/start)" button.
5. That should help you set-up the forked repository on GitHub.
6. Once setup, clicking on "Deploy Site" button should trigger the build.
7. You can then check the site being deployed at this URL: `https://app.netlify.com/teams/<INSERT_NETLIFY_USERNAME_HERE>/sites`.
8. Once the site is deployed, Netlify assigns a domain automatically. It should look something on these lines: `https://<NETLIFY_GENERATED_ALPHANUMERIC_STRING>.netlify.app`.

## :hammer_and_wrench: Built With

The site is built using Pelican to generate static content which are then delivered using Netlify's CDN. These are the primary 2 tools you will specifically need to build the website.

For more information on how to use these tools, refer to their respective documentations:

- [Netlify Docs](https://docs.netlify.com/)
- [Pelican 4.5.0 Documentations](https://docs.getpelican.com/en/stable/)

## :building_construction: Contributing

I'm no frontend mastermind, hence the site is quite bland as you must've noticed already. Although it's intentionally kept a bit bland because I prefer the site to be minimalistic. But I do appreciate some of your suggestions to improve this project. Perhaps you're skilled at web dev & can help me fix something weird? Or maybe you would like to make some changes to the way the site looks & behaves. If you think you've the right skill then all you've got to do is fork this project, clone it locally & make a PR against this repository.

All efforts towards making this project better & more accessible are appreciated. So don't hesitate to contribute to the project. There's a reason why I've open-sourced this personal website! :wink:

There's a comprehensive guideline in the [CONTRIBUTING.md](.github/CONTRIBUTING.md) document. Refer to it for more details on contributing to the project.

### :eyes: Issues

In case of a bug report, bugfix or a suggestion, please feel free to open an issue following the respective templates

- [Ask a Question](.github/ISSUE_TEMPLATE/ask-a-question.md)
- [Bug Report](.github/ISSUE_TEMPLATE/bug-report.md)
- [Discussion](.github/ISSUE_TEMPLATE/discussion.md)

### :package: Pull Request

Pull Requests are always welcome & I'll review them as quick as possible. But for easier collaboration, please follow the specification provided in the [PR template](.github/PULL_REQUEST_TEMPLATE.md).

## :memo: License

Due to the nature of the contents of this repository, its difficult to license everything under a single License. Hence, I decided to include two licenses for each aspect of all the contents in the repository. The following points will briefly describe the licensing T&Cs for everything contained within this repository.

1. The literary content as well as the underlying source code used to markup the content are licensed under the [CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html) license. Refer to the [LICENSE](LICENSE) documentation for further information.

2. This repository also hosts the [Pelican](https:www.getpelican.com) Static-Site Generator for automatically building & delivering the markup content over a CDN. Therefore, all source code of the Pelican software is licensed under the T&Cs of the [original LICENSE](https://github.com/getpelican/pelican/blob/master/LICENSE) available at the Pelican repository.

## :raised_hand: Get Help

Facing difficulties to deploy your site after forking this repository? Well then feel free to reach out to me. I'm available on Twitter & LinkedIn for a quick chat. But if you need a very comprehensive explanation on something related to this project, open an Issue. Follow this [Discussion](.github/ISSUE_TEMPLATE/discussion.md) Issue template to create a thread.

Perhaps you've a question not related to this project in any way, then check out my [*Ask Me Anything*](https://github.com/jarmos-san/ama)

## :clap: Acknowledgements

- [Pelican](https://github.com/getpelican/pelican), a Static-Site Generator developed with Python & maintained by the amazing [Pelican Dev Team](https://github.com/orgs/getpelican/people)!
- The site uses the [blue-penguin](https://github.com/jody-frankowski/blue-penguin) theme built by [Jody Frankowski](https://github.com/jody-frankowski).
- Thanks to all the [contributors](https://github.com/Jarmos-san/blog/graphs/contributors) who helped advanced this project into what it is today.
