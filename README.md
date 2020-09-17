<!-- TODO: Make the README more lively by including Emojis wherever applicable -->
# Somraj's Blog

<!-- Position of the badges for easier accessibility
Website | Netlify | LinkedIn | Quora | AMA | Twitter -->
[![Website](https://img.shields.io/website?down_color=Red&down_message=Down&label=Website&style=flat-square&up_color=Green&up_message=Online&url=https%3A%2F%2Ftest-jarmos.netlify.app%2F)](https://test-jarmos.netlify.app) [![Netlify](https://img.shields.io/netlify/40455652-e1fb-4daf-aae1-a9ecebbcb51a?color=00C7B7&label=Netlify%20Build&logo=Netlify&style=flat-square)](https://app.netlify.com/sites/test-jarmos/overview) [![LinkedIn](https://img.shields.io/static/v1?label=LinkedIn&message=Connect&color=0077B5&style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jarmos/) [![Quora profile](https://img.shields.io/static/v1?label=Quora&message=Follow&color=B92B27&style=flat-square&logo=quora)](https://www.quora.com/profile/Somraj-Saha-3) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/Jarmos-san/ama) [![Twitter Follow](https://img.shields.io/twitter/follow/Jarmosan?style=social)](https://twitter.com/Jarmosan)

This repository hosts the source code for my personal website. It's statically generated using [Pelican](https://www.getpelican.com) - A Static Site Generator(SSG) built on Python & is delivered using [Netlify](https://www.netlify.com/).

- [Somraj's Blog](#somrajs-blog)
  - [Getting Started](#getting-started)
  - [Built With](#built-with)
  - [Contributing](#contributing)
    - [Issues](#issues)
    - [Pull Request](#pull-request)
  - [License](#license)
  - [Get Help](#get-help)
  - [Acknowledgements](#acknowledgements)

## Getting Started

You found my website, liked it & now wanted to check out how I work on maintaining it. If that's the case, this section will help you get started. First thing decide if you would like to contribute to the project, then skip ahead to the [Contributing](#contributing) section.  Perhaps you just want a similar website for yourself & not sure how to do it. If it's so then the following guidelines should get you what you need.

<!--
! Take care of this shit on priority!

TODO: Steps to recreate creating & hosting the website

* Break down the steps into the following:

* 1.Setting up a local dev environment.
* 2.Pushing local content to GitHub & setting up a Netlify site using the UI.
* 3.Optionally, include steps to recreate the site using the Netlify CLI.
-->

1. Fork the repository, clone it locally using the `git@github.com:<INSERT_YOUR_USERNAME_HERE>/pelican-blog.git`.
2. CD into the newly cloned directory.
3. Create a virtualenv using the `python -m venv .venv` command.
4. Activate the virtualenv by `source .venv/bin/activate` command.
5. Install necessary dependencies using the `pip install -r blog/requirements.txt` command.

## Built With

The site is built using Pelican to generate static content which are then delivered using Netlify's CDN. These are the primary 2 tools you will specifically need to build the website.

For more information on how to use these tools, refer to their respective documentations:

- [Netlify Docs](https://docs.netlify.com/)
- [Pelican 4.5.0 Documentations](https://docs.getpelican.com/en/stable/)

## Contributing

Do you've some suggestions to improve this project? Or perhaps there's an open issue you can help me resolve? Then all you've got to do is fork this project, clone it locally & make a PR against this repository.

I appreciate all efforts towards making this project better & more accessible, so don't hesitate to contribute to the project. There's a reason why I've open-sourced my personal website! :wink:

There's a comprehensive guideline in the [CONTRIBUTING.md](./..github/CONTRIBUTING.md) document. Refer to it for more details on contributing to the project.

### Issues

In case of a bug report, bugfix or a suggestion, please feel free to open an issue following the respective templates

- [Ask a Question](./..github/ISSUE_TEMPLATE/ask-a-question.md)
- [Bug Report](./..github/ISSUE_TEMPLATE/bug-report.md)
- [Discussion](..github/ISSUE_TEMPLATE/discussion.md)

### Pull Request

Pull Requests are always welcome & I'll review them as quick as possible. But for easier collaboration, please follow the specification provided in the [PR template](./..github/PULL_REQUEST_TEMPLATE.md).

## License

Due to the nature of the contents of this repository, its difficult to license everything under a single License. Hence, I decided to include two licenses for each aspect of all the contents in the repository. The following points will briefly describe the licensing T&Cs for everything contained within this repository.

1. The literary content as well as the underlying source code used to markup the content are licensed under the [CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html) license. Refer to the [LICENSE](LICENSE) documentation for further information.

2. This repository also hosts the [Pelican](https:www.getpelican.com) Static-Site Generator for automatically building & delivering the markup content over a CDN. Therefore, all source code of the Pelican software is licensed under the T&Cs of the [original LICENSE](https://github.com/getpelican/pelican/blob/master/LICENSE) available at the Pelican repository.

## Get Help

Facing difficulties to deploy your site after forking this repository? Well then feel free to reach out to me. I'm available on Twitter & LinkedIn for a quick chat. But if you need a very comprehensive explanation on something related to this project, open an Issue. Follow this [Discussion](./..github/ISSUE_TEMPLATE/discussion.md) Issue template to create a thread.

Perhaps you've a question not related to this project in any way, then check out my [*Ask Me Anything*](https://github.com/jarmos-san/ama)

## Acknowledgements

- The site uses the [pelican-blue](https://github.com/Parbhat/pelican-blue) theme built by [Prabhat Puri](https://github.com/Parbhat)
