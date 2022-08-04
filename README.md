# :man_technologist: Somraj Saha's Blog.

[![Website][website]][personal website]
[![Netlify Deploy][netlify deploy badge]][netlify deploy]
[![LinkedIn][my linkedin badge]][my linkedin]
[![Quora profile][my quora badge]][my quora]
[![Ask Me Anything !][my ama badge]][my ama]
[![Twitter Follow][my twitter badge]][my twitter]

**DISCLAIMER**: **I'M NO LONGER MAINTAINING THE PROJECT!**

The repository & the project is abandoned! I'm no longer actively maintaining & working on this project since
I recreated it using Next.js instead. If you're interested in checking it out, please head over to my [personal website's repository](https://github.com/Jarmos-san/personal-website). The project uses the latest features of React.js
and is faster than a traditional Hugo project. So, feel free to check it out & contribute to it!

This repository hosts the tools, assets & themes for my [personal
website][personal website]. The site is statically generated with
[Hugo][hugo landing page] & the [PaperMod][hugo-papermod] theme. Hugo which is a
Static Site Generator(SSG) built with [Golang][go landing page] generates the
static contents for the site to be deployed to [Netlify][netlify landing page].

- [:man_technologist: Somraj Saha's Blog](#man_technologist-somraj-sahas-blog)
  - [:checkered_flag: Getting Started](#checkered_flag-getting-started)
    - [:running: The Easy & Quick Way To Get It Done](#running-the-easy--quick-way-to-get-it-done)
      - [:nut_and_bolt: Setup a Development Environment](#nut_and_bolt-setup-a-development-environment)
      - [:chart_with_upwards_trend: Setting Up Traffic Tracking & Analytics](#chart_with_upwards_trend-setting-up-traffic-tracking--analytics)
        - [Cloudflare](#cloudflare)
        - [Google Analytics](#google-analytics)
      - [:control_knobs: Setup a CMS](#control_knobs-setup-a-cms)
      - [:dash: Preparing Your Site For Deployment](#dash-preparing-your-site-for-deployment)
      - [:gear: Setup GitHub Actions to Deploy](#gear-setup-github-actions-to-deploy)
  - [:hammer_and_wrench: Built With](#hammer_and_wrench-built-with)
  - [:building_construction: Contributing](#building_construction-contributing)
    - [:eyes: Issues](#eyes-issues)
    - [:package: Pull Request](#package-pull-request)
  - [:memo: License](#memo-license)
  - [:raised_hand: Get Help](#raised_hand-get-help)
  - [:clap: Acknowledgements](#clap-acknowledgements)

## :checkered_flag: Getting Started

Did you find my website somehow either on GitHub or elsewhere on the Internet?
Do you want a site similar to mine for yourself too? Or perhaps, you just ❤️
open-source software & would like to make a contribution to my site, then read
this [README](/README.md) should be your first step.

A bird's eye overview of what the blog is capable of:

- It's FREE, as in no server costs are involved (_for now_).
- In context to the point above, there's no server in the first place to serve
  the website on the Internet. All the generated static content are delivered
  over [Netlify's CDN][netlify cdn guide].
- Transparency is a major aspect in everything I do in life. The same applies to
  my personal website as well. That said, I try to keep stuff related to it as
  open-source as possible on this repository. In other words, my website will
  forever be open-sourced.
- My site uses [Cloudflare Analytics][cloudflare analytics] along with Google
  Analytics (GA) for the following reasons:
  - Cloudflare is more privacy driven & hence is suitable for some of my more
    privacy-concerned audiences.
  - I would love to use [Matomo][matomo] over GA but it requires me to rent out
    a VPS. I just don't have the financial overhead to increase my expenses at
    the moment. So, as much as I want to protect my user's privacy, it's just
    not a possibility right now. Although, I appreciate every bit of a
    [donation][buy me a coffee] that will help me setup & maintain a Matomo
    Analytics server to protect your privacy.
  - Cloudflare Analytics is still in beta & doesn't offer as many metrics as GA
    provides. Much of the metrics I need, is important for me to keep improving
    the services I provide on my site & to my sponsors.
- Knowledge-sharing over aesthetics. Visit my site & you'll find it's pretty
  simple & minimalist. That's intentional as I want my audiences to read my
  content & take home some valuable lessons. Intrusive popups & marketing
  gimmicks aren't my thing, so I try to keep that away from my personal site.
- Make it a Wordpress alternative. Hence, it even supports an admin panel
  powered by Forestry.io!

So, if the aforementioned points matters to you, then fo ahead & check out how
to get your own blog which looks similar to mine.

### :running: The Easy & Quick Way To Get It Done

In a hurry to get your personal website running ASAP, then check out the
following section.

#### :nut_and_bolt: Setup a Development Environment

1. Fork the repository.
2. Clone your copy of the repository locally using the command
   `git clone git@github.com:<INSERT_YOUR_USERNAME_HERE>/blog.git`.
3. Remove the files under the directory `content`. Note, the files are written
   in [Markdown][markdown guide]. So, if you've been active on GitHub for a
   while, writing your `.md` content will be a breeze.
4. Ensure you've Hugo installed & is available on PATH. If not, then follow the
   instructions available in [the official documentation][install hugo] to set
   it up on your local machine.
5. Clone the [PaperMod theme][hugo-papermod] under the `./theme/` directory with
   the `git submodule add https://github.com/adityatelange/hugo-PaperMod.git`
   command.
6. `cd` back into the root directory & run the `hugo server` command on your
   preferred terminal & see if everything works as expected.

#### :chart_with_upwards_trend: Setting Up Traffic Tracking & Analytics

The blog uses Cloudflare's tracker along with Google Analytics (GA). Thus,
privacy-concerned users can either use [uBlock Origin][ublock origin] to block
tracking JS code or block trackers & cookies from the browser. Using both of
them in tandem also helps keep a check on certain inconsistencies
([_source_][cloudflare vs google analytics]).

That said, following are the instructions to setup Cloudflare (and/or GA):

##### Cloudflare

- Create a [Cloudflare][cloudflare landing page] account (_if you don't have one
  already_).
- Create the tracking JS snippet on the [Analytics
  dashboard][cloudflare analytics dashboard].
- Copy & replace the existing snippet in
  [`layouts/partials/extend_head.html`](./layouts/partials/extend_head.html)
  with the snippet you just created on the Cloudflare Analytics dashboard.

##### Google Analytics

- Create a [Google Analytics][google analytics] if you don't own one already!
- Create the [Google Analytics 4 property][tracking code setup instructions] for
  the website.
- Add the tracking code (which looks something like `G-XXXXXXXXX`) in the
  `config.yml` to the `GoogleAnalyticsID` key.
- Add the `gtag.js` snippet to `extend_head.html` partial under
  `layouts/partials`.

  ```javascript
  <!-- Global site tag (gtag.js)-->
  <script async src="https://www.googletagmanager.com/gtag/js?id={{ .Site.Params.GoogleAnalyticsID}}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());

    gtag('config', '{{ .Site.Params.GoogleAnalyticsID}}');
  </script>
  <!-- End of Global site tag (gtag.js)-->
  ```

- Check your GA dashboard with tracking cookies & JS enabled on your browser.

And you're good to go!

But in case, you've privacy concerns on using GA, refer to the [Privacy
Policy][privacy policy] document for a detailed description of how we use the
data gathered through the trackers.

**NOTE**: As of Hugo 0.80, the new Google Analytics 4 [doesn't
work][ga 4 doesn't work] out-of-the-box with Hugo's internal templates.

#### :control_knobs: Setup a CMS

**Note**: I'm in favour of using [Forestry.io][forestry]'s service right now
over [Netlify CMS][netlify cms landing page]. It's much more easier & intuitive
(_and less buggier too_) to setup. The decision was made after coming across a
blocker as documented in [#40][issue #40]. Since, the devs of Netlify haven't
shown any interest to fix the issue, Forestry is a better choice.

For a detailed installation process, refer to the official Forestry.io
[documentations][forestry docs]. The devs did an amazing job articultating the
exact procedure to set it up.

That said, following are the advantages of get setting up a CMS admin panel on
the site:

- You no longer need a Markdown Editor (or even the development environment)
  installed locally. Just access it at: `https://<YOUR-SITE>/admin` & start
  writing.
- You can give editorial access to 2 more writers all for free. More than that
  you would've to purchase a subsciption.
- Forestry leverages the Git-backend to update any config files it needs for the
  CMS, on your behalf. All you got to do is tweak the settings on it's web-based
  GUI.
- And finally, the main reason for switching from Netlify CMS to Forestry,
  availability of remote media storage. As of the now the site is configured to
  load up the image assets off of [Cloudinary][cloudinary] but other options
  include [S3][aws s3] & [Netlify Large Media][netlify large media]. These
  options should help me in case I need to scale up my image storage
  capabilities.

There's more information available on the official docs, so do check it out.
They did a convincing job to make me switch.

#### :dash: Preparing Your Site For Deployment

1. Write your articles inside the `./content` directory & save them as `.md`
   files. Check if the articles are generated as expected by running the
   `hugo server` command.
2. Push your changes to GitHub with the `git push` command from the root
   directory.
3. Create/login into an account on [Netlify][netlify landing page].
4. Refer to the [Netlify Documentations][netlify docs] to setup an initial
   deployment. You'll have to do it only once if you want to deploy your changes
   with GitHub Actions instead just like me.
5. Once the site is deployed, Netlify assigns a domain automatically. It should
   look something on these lines:
   `https://<NETLIFY_GENERATED_ALPHANUMERIC_STRING>.netlify.app`.

#### :gear: Setup GitHub Actions to Deploy

While you could push your changes to GitHub & Netlify will still trigger a build
on their platform, but it's pretty inefficient & non-scalable. Reasons being:

- Netlify has a limited 300 minutes compared to GitHub's insane 2000 minutes of
  build times. While it should suffice if you've just one site but you can chew
  through your quoate pretty quick once you start deploying more sites.
- Hugo is fast (_or rather the fastest SSG out there_). It'll generate your
  static files in under 1ms. Couple it with a fast Action, you can deploy the
  generated files to Netlify's CDN in less than half a min! This comes handy
  when you're committing changes constantly & would like to preview a live
  version of the changes. Doing the same takes at least a min on Netlify's
  servers.
- It's a more configurable way to deploy the contents.

And the list goes on. There really is no reason why shouldn't use GitHub Actions
to deploy your site to Netlify (_if you can, that is_).

So without further ado, let's setup GitHub Actions to build & deploy the site to
Netlify (_finally!_ 😤)

- The [nwtgck/actions-netlify][netlify actions] is used to manage the build &
  deployment process. If you had followed the steps till now, you might notice
  on the GitHub Action's tab that it failed (_which is expected_). To fix it
  you'll need an Netlify Auth Token & the Site ID.
- You can find the Netlify Auth Token under the [User
  Settings>Applications][netlify user settings] tab. While the Site ID can be
  found under the individual site's settings at:
  `https://app.netlify.com/sites/<YOUR-SITE-NAME>/settings/general`. The
  alphanumeric name under `API ID` is what you should be looking out for.
- Copy those details & save them as [Encrypted
  Secrets][github encrypted secrets]. Make sure to name them as
  `NETLIFY_AUTH_TOKEN` & `NETLIFY_SITE_ID` respectively for the Auth token & the
  Site ID.

And you're good to go! Write an article under the `./content` directory & push
them to the remote respository. Then watch your workflow build & deploy the site
all under half a minute! 🤯

## :hammer_and_wrench: Built With

The site is built using Hugo to generate static content. These contents are then
deployed to Netlify to be delivered over Netlify's CDN. These are the primary 2
tools you will specifically need to build the website.

For more information on how to use these tools, refer to their respective
documentations:

- [Netlify][netlify docs]
- [Hugo][hugo docs]
- [hugo-PaperMod][hugo-papermod] theme

## :building_construction: Contributing

I'm no frontend mastermind, hence I often need a helping to fix something on the
website. So, if you find something broken & a feature needing some improvement,
don't hesitate to make a PR. All suggestions & PRs to improve this project are
appreciated.

or, perhaps you're just looking to get your feet wet in the open-source
community. Then this site will be a perfect opportunity for you. Besides,
there's a reason why I've open-sourced this personal website! :wink:

There's a comprehensive guideline in the
[CONTRIBUTING.md](.github/CONTRIBUTING.md) document. Refer to it for more
details on contributing to the project.

### :eyes: Issues

In case of a bug report, bugfix or a suggestion, please feel free to open an
issue following the respective templates

- [Ask a Question](.github/ISSUE_TEMPLATE/ask-a-question.md)
- [Bug Report](.github/ISSUE_TEMPLATE/bug-report.md)
- [Discussion](.github/ISSUE_TEMPLATE/discussion.md)

### :package: Pull Request

Pull Requests are always welcome & I'll review them as quick as possible. But
for easier collaboration, please follow the specification provided in the
[PR template](.github/PULL_REQUEST_TEMPLATE.md).

## :memo: License

All software used & the content I share are licensed under the T&Cs as stated
below:

1. All the literary content available under [`./content/posts`](./content/posts)
   are licensed under the [CC0-1.0](./LICENSE) license.

2. The repository also uses and/or contains software used to generate the static
   contents for the personal website. Following are the software as well as
   other related tools used & their licensings T&Cs.

   | Software            | Licence T&Cs                                      |
   | ------------------- | ------------------------------------------------- |
   | Hugo                | [Apache-2.0][hugo license]                        |
   | Netlify Actions     | [MIT][netlify actions license]                    |
   | Hugo-PaperMod theme | [MIT][hugo-papermod license]                      |
   | Netlify             | [Netlify Terms of Service Agreement][netlify tos] |
   | Git Checkout Action | [MIT][git checkout action license]                |
   | Actions-Hugo        | [MIT][hugo action license]                        |
   | Automerge-Action    | [MIT][automerge action license]                   |

## :raised_hand: Get Help

Facing difficulties to deploy your site after forking this repository? Well then
feel free to reach out to me. I'm available on [Twitter][my twitter] &
[LinkedIn][my linkedin] for a quick chat. But if you need a very comprehensive
explanation on something related to this project check out the [Discussion
threads][project discussion threads].

Or maybe your question isn't related to this project, then check out my [_Ask Me
Anything_][my ama].

## :clap: Acknowledgements

- [Hugo Devs][hugo devs], thanks to whom, my website wouldn't come into
  fruition!
- The site uses the [PaperMod][hugo-papermod] theme built by [Aditya
  Telange][hugo-papermod dev].
- And at last, thanks to [all those who contributed][project contributors] to
  fixing & correcting my site.

<!-- * Reference links -->
<!-- ? Personal Related Links -->

[personal website]: https://jarmos.netlify.app
[my twitter]: https://twitter.com/Jarmosan
[my linkedin]: https://www.linkedin.com/in/jarmos/
[my ama]: https://github.com/Jarmos-san/Jarmos-san/discussions/categories/q-a
[my quora]: https://www.quora.com/profile/Somraj-Saha-3
[buy me a coffee]: https://www.buymeacoffee.com/jarmos

<!-- ? Hugo Related Links -->

[hugo-papermod]: https://adityatelange.github.io/hugo-PaperMod/
[install hugo]: https://gohugo.io/getting-started/installing/
[hugo google analytics]: https://gohugo.io/templates/internal/#google-analytics
[hugo license]: https://github.com/gohugoio/hugo/blob/master/LICENSE
[hugo devs]: https://github.com/orgs/gohugoio/people
[hugo-papermod dev]: https://github.com/adityatelange
[hugo-papermod license]:
  https://github.com/adityatelange/hugo-PaperMod/blob/master/LICENSE

<!-- ? Netlify Related Links -->

[netlify actions license]:
  https://github.com/nwtgck/actions-netlify/blob/develop/LICENSE
[netlify tos]: https://www.netlify.com/tos/
[netlify landing page]: https://www.netlify.com/
[netlify cdn guide]:
  https://community.netlify.com/t/support-guide-making-the-most-of-netlifys-cdn-cache/127
[netlify cms license]:
  https://github.com/netlify/netlify-cms/blob/master/LICENSE
[netlify actions]: https://github.com/marketplace/actions/netlify-actions
[netlify user settings]: https://app.netlify.com/user/applications

<!-- ? Cloudflare Related Links -->

[cloudflare vs google analytics]:
  https://community.cloudflare.com/t/gap-between-cloudflare-analytics-and-google-analytics-reporting/33326
[cloudflare analytics dashboard]:
  https://dash.cloudflare.com/?to=/:account/:zone/analytics/traffic

<!-- ? Project Related Links -->

[project discussion threads]: https://github.com/Jarmos-san/blog/discussions
[project contributors]: https://github.com/Jarmos-san/blog/graphs/contributors
[issue #40]: https://github.com/Jarmos-san/blog/issues/40

<!-- ? Miscellaneous Related Links -->

[netlify deploy]:
  https://github.com/Jarmos-san/blog/actions?query=workflow%3A%22Netlify+Deploy%22
[git checkout action license]:
  https://github.com/actions/checkout/blob/main/LICENSE
[hugo action license]:
  https://github.com/peaceiris/actions-hugo/blob/main/LICENSE
[automerge action license]:
  https://github.com/pascalgn/automerge-action/blob/master/LICENSE
[ga 4 doesn't work]: https://github.com/gohugoio/hugo/issues/7954

<!-- ? Shield Badges -->

[website]:
  https://img.shields.io/website?down_color=Red&down_message=Down&label=Website&style=flat-square&up_color=Green&up_message=Up&url=https%3A%2F%2Fjarmos.netlify.app%2F
[netlify deploy badge]:
  https://github.com/Jarmos-san/blog/workflows/Netlify%20Deploy/badge.svg?branch=dev
[my linkedin badge]:
  https://img.shields.io/static/v1?label=LinkedIn&message=Connect&color=0077B5&style=flat-square&logo=linkedin
[my quora badge]:
  https://img.shields.io/static/v1?label=Quora&message=QnA&color=B92B27&style=flat-square&logo=quora
[my ama badge]: https://img.shields.io/badge/Ask%20Me-Anything!-1abc9c.svg
[my twitter badge]: https://img.shields.io/twitter/follow/Jarmosan?style=social

<!-- ? Documentations -->

[forestry docs]: https://forestry.io/docs/welcome/
[github encrypted secrets]:
  https://docs.github.com/en/actions/reference/encrypted-secrets
[netlify docs]: https://docs.netlify.com/
[hugo docs]: https://gohugo.io/documentation/

<!-- ? Landing Pages -->

[go landing page]: https://golang.org
[netlify cms landing page]: https://www.netlifycms.org/
[hugo landing page]: https://gohugo.io
[cloudflare landing page]: https://www.cloudflare.com/
[cloudflare analytics]: https://www.cloudflare.com/analytics/
[cloudinary]: https://cloudinary.com/
[aws s3]: https://aws.amazon.com/s3/
[netlify large media]: https://www.netlify.com/products/large-media/
[forestry]: https://forestry.io/
[markdown guide]: https://www.markdownguide.org/
[matomo]: https://matomo.org/
[ublock origin]: https://github.com/gorhill/uBlock
[google analytics]: https://analytics.google.com/
[tracking code setup instructions]:
  https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319
[privacy policy]:
  https://www.privacypolicygenerator.info/live.php?token=fsG90WvN3xCCNeV6wrBEI9ZowuN2KUEI
