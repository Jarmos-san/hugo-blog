---
title: "How to Create an Overpowered Blog With Hugo (As a Wordpress Alternative)"
date: 2021-02-21T22:57:04+05:30
draft: true
category: Blogging
slug: blogging-with-hugo-as-an-wordpress-alternative
summary:
description:
cover:
  image:
  alt:
  caption:
  relative: false
showtoc: true
---

## Introduction

A developer without a blog is like fishermen without their fishing rod. While it is possible to fish with just a thread & a hook, the rod makes life much easier for the fishermen. In context to the analogy, I believe Dan Bader summed it up well in one of his article -- [_3 Reasons Why You Need a Programming Blog_][3 Reasons Why You Need a Programming Blog].

But, if you've read some of my previous articles, you would know choosing the right tools to blog is no easy task. I've written about such a dilemma I was in, in this article -- [_Medium vs Static Site Generators -- A Computer Vision Engineer's Dilemma_](../medium-vs-static-site-generators). But, over the past one year or so after publishing that article I had time to experiment with existing blogging tools. And I reviewed each of those tools in another article -- [_A Review of Some of the Most Popular Static Site Generators_](../reviewing-popular-static-site-generators).

Hence, as you can see, blogging is the easiest part, choosing the right tool for personal use case isn't. While you could use a hosted Wordpress site as an option but I don't see why a developer should spend time setting up and/or maintain security updates, server costs & so on.

Static Sites are a much better alternative to Wordpress. You no longer have to worry about server maintenance, security updates for Wordpress & the financial costs in doing so. With static sites, all of those dependencies are gone. All you've to worry about right now is publish quality content & delegate the hosting needs to an external service.

So, without further adieu, let's dive into how we can setup a blog as a Wordpress alternative. Do note, having some prior programming knowledge can a bonus point is not a prerequisite. You can follow along with the instructions suggested in this article & you'll be fine.

## Prerequisite Tools

While there're a couple of tools out there to generate the static files for your blog, we'll be using [Hugo][Hugo Homepage]. This is so, because Hugo is undeniably one of the [_easiest to use_](../reviewing-popular-static-site-generators/#hugo-the-fastest-static-site-generator-ever-created) Static Site Generator available.

Beside Hugo, we'll also need a GitHub account to not just host the articles but for other tools as well. One of those tools include [GitHub Actions][GitHub Actions Docs]. There're a plenty of community maintained GitHub Actions in the GitHub Marketplace & we'll be using a couple of them.

But no blog could be considered a Wordpress alternative without Content Management System (CMS). So, to deliver onto our CMS needs, we'll use the services from [Forestry][Forestry].

And at last, we'll use [Netlify][Netlify Homepage] to deliver the generated static content over a Content Delivery Network(CDN) to our audiences.

Optionally, we could use [Google Analytics (GA)][Google Analytics] for tracking needs. But if you're privacy concerned citizen, you could use [Cloudflare Analytics][Cloudflare Analytics] as a good alternative.

So, to sum up all the necessary tools we'll be using:

- A Github repository to host the articles, themes & other files required by the tools we'll be using.
- A couple of GitHub Actions.
  - [peaceiris/actions-hugo][Hugo Actions] to setup Hugo & generated the static content on the GitHub Actions server.
  - [nwtgck/actions-netlify][Netlify Actions] to deploy the generated static content.
  - And the optional [pascalgn/automerge-action][Auto Merge Action] to automatically merge Dependabot PRs without any manual interventions.
- An account on [Forestry][Forestry] for the CMS.
- A Netlify account to deliver the static content to our audiences.
- And the optional Google/Cloudflare Analytics for tracking needs.

So, that said, ensure you're setup with all the tools mentioned above & then we can get started.

## Using Hugo (With All It's Glory)

As mentioned earlier, Hugo is without a doubt one of the easiest Static Site Generator available to use. This fact that Hugo has [50K+ stargazers][Hugo Stargazers] shows how useful it is!

So, without wasting any more of your precious time let's dive into using Hugo.

### Installing Hugo

First things first, is to install Hugo on your local machine. And unlike other Static Site Generators like [Pelican][Pelican Homepage], [Gatsby][Gatsby Homepage] and/or [Jekyll][Jekyll Homepage], Hugo has no dependency! Which means, you don't need neither a local Python/Ruby runtime or a JavaScript environment. All you need is the Hugo [binaries][Hugo Binaries] & you're good to go.

The "_installation_" procedure is also pretty simple. You just need to add the binary to system `PATH` & invoke the `hugo` command from anywhere in the Terminal. Editing each Operating System's `PATH` is quite different. Hence I suggest you take a thorough look at the [official installation documentations][Hugo Installation Procedure].

But before you proceed ahead do ensure Hugo was installed correctly. You can check it by running the `hugo version` command on your CLI. If everything works fine, you should a similar output.

```bash
Hugo Static Site Generator v0.80.0-792EF0F4 windows/amd64 BuildDate: 2020-12-31T13:37:57Z
```

### Creating You Site

I must say, installing Hugo while easy, it isn't the most fun part of the whole procedure. So, let's get started with the fun parts.

You can generate a skeleton site (_which we'll build upon soon_) with the `hugo new site .` command. Notice the `.` (_dot_) at the end of the command? It tells Hugo to generate the skeleton site in the current directory.

The aforementioned command generates a simple set of files & folders. Each of them serves a specific purpose for Hugo. But keeping things minimal, here's what the directory structure looks like after generating them.

  ```bash
  .                 # Current (or Root) directory
  ├───archetypes    # Stores preconfigured frontmatter metadata.
  ├───content       # Stores your Markdown articles.
  ├───data          # Stores data for used with templates and/or shortcodes
  ├───layouts       # Stores custom code snippets to override the used theme(s).
  ├───resources     # Generated resources (for eg processed images) are stored here.
  ├───static        # Holds static content like CSS/JS files, images, favicons, etc.
  ├───themes        # This is where you download & store a Hugo theme.
  └───config.yml    # Config file to configure Hugo. Supports YAML, TOML & JSON formats.
  ```

There's obviously more to what Hugo generates as skeleton site than what I can discuss in one blog. So, I suggest taking a brief look at the documentation on Hugo's [project directory structure][Hugo Project Directory].

Without delving into comprehensive details of what each directory is for, let's keep things minimal. That way, there'll be room for further customization. And more important, you can get started delivering content at the earliest.

### Creating Content (The Actual Fun Stuff!)

As mentioned earlier using Hugo is easy. Yet, any given Hugo project can be made as complicated as it needs to be. So believe it or not, you can actually start writing content straight away. All you now need is;

- Download a theme under the `themes` directory.
- Configure Hugo to generate your site with some site metadata for SEO needs in the `config.yml` file.
- Write content in Markdown under the `content` directory.

It's that simple!

Hugo boasts of some hundreds of beautiful [community maintained themes][Hugo Themes]. You can download theme to your site's `theme` directory & Hugo will use it to generate the contents of your site. And the easiest way to install a theme is to use "_Git Submodules_". That way you can ensure the themes are updated as & when the theme authors pushes a commit to it's repository.

So, installing themes is as easy as running the `git submodule add <DOWNLOAD-LINK> themes/<THEME-NAME> --depth=1` command.

Configuring Hugo to generate metadata for your website couldn't be made easier than ever. You include some necessary values in the `config.yml` file & Hugo will include those values as metadata for your site. In other words, you get great SEO practices out-of-the-box! To get a general feel of what a `config.yml` file looks like, here's an example;

```yaml
baseURL: "Your Site URL"
languageCode: "en-us"
title: "Your Website Name"
theme: "Theme Name"
paginate: 5
enableRobotsTXT: true
params:
  env: production
  title: Your Website Name
  description: "Description of your website."
  images: ['profile-pic.jpg']
  defaultTheme: auto
  GoogleAnalyticsID: G-V0ZH6RS2BM
  assets:
    favicon: icons/favicon.ico
menu:
  main:
  # Menu items like Contact, About Me pages & so on
```

Do note, configuring the `config.yml` isn't limited to what I mentioned here. Based on the theme you're using, you might/mightn't have to extend on it.

And at last, the `content` directory where you store the Markdown files for your articles. You can organize your Markdown content into subdirectories for easier maintanance & organization. For example, here's what mine looks like.

```bash
./content
  ├───posts
  ├   ├───article-1.md
  ├   ├───article-2.md
  └───about-me.md
```

You can find detailed instructions on how to organize the articles under `content` in the [Content Organization][Hugo Content Organization] section of the documentations.

Keeping things as minimal as possible, you can actually start creating content for the blog right away! You can write content in [Markdown][Markdown Homepage] under the `content` directory & you're good to go.

Now that you've started creating content, it's time for your audience to read them! And in the section, we'll look into exactly how we can do so.

## Deploying the Blog

A major advantage of using Static Site Generators over Wordpress is, you no longer need a hosting provider (_or a server_). This alleviates the surface area of potential security & maintenance mishaps. So, we'll be using Netlify's services to deliver our static content over their CDN. But you can also use other similar services like Vercel.

That said, before you get started with Netlify, ensure you've created a [new repo][New GitHub Repo] to host your site contents & a [Netlify account][Netlify Homepage]. You'll need to perform a one-time operation on the Netlify dashboard to create a new site. Refer to the Netlify docs to know the [exact procedure][Netlify Git Deploy] to do so. Later on in the article we'll look into how GitHub services can be configured to automate some of the deployment procedures.

Then push your fresh new site to the GitHub repository you just created. And it should trigger a [Netlify build operation][Netlify Build Operation]. You can now view your website at an URL provided by Netlify (_you can change it though_ :wink:).

Now each time you write a new article or push some aesthetic changes to your site, Netlify will trigger a build. While it works & is fine for most users but there're certain downsides. One major disadvantage of using Netlify's platform to build the content, is it's time consuming (_often taking over 2mins to complete the build_). Considering Netlify provides only 300 minutes of build per month, it won't be long before you run out of it. Besides, you just can't utilize Hugo's full potential there which is why we'll use GitHub Actions.

With GitHub's wide range of services, we can not only deploy the site but can automate some of the monotonous tasks as well!

The next sections delves deeper into why & how we can achieve such feat.

## Setting Up Automation & a CMS Backend

Creating & deploying the site was easy & fun but it doesn't last long (_saying from personal experience_). More so, when you add the theme as a submodule, you can expect its author to update frequently. Fortunate for us, we can use [GitHub's Dependabot][Dependabot] to keep our theme(s) updated.

There's also the need for a Content Management System (CMS). What good is a _Wordpress Alternative_ without CMS, right? And as mentioned in the previous section, delegating the build process to GitHub Actions instead of Netlify's build infrastructure.

So, let's list out the remaining features we need to work on & start working on them one-by-one.

- Setup & configure Dependabot to keep all dependencies for our site updated.
- Setup & use Forestry as the CMS backend.
- Configure & delegate the build process to GitHub instead of Netlify.

### Allowing Dependabot to Keep Dependencies Up-to-Date

Ever since, [GitHub integrated Dependabot into it's services][GitHub's Dependabot], keeping our project dependencies up-to-date has never been easier. And guess what? Dependabot can take care of _Git Submodules_ as well which means your themes will be updated as soon as it's author pushes some changes to it! To configure Dependabot, you need to create a `dependabot.yml` file under the `.github` directory (_create it_).

And this is how the `dependabot.yml` file should look like:

```yaml
version: 2
updates:

    # Update all the GitHub Actions we'll use soon
    - package-ecosystem: "github-actions"
      directory: "/"
      schedule:
          interval: "daily"
          time: "06:00"
      labels: ["github-actions", "automerge"]

    # Updates  all Git Submodules (the theme in this case)
    - package-ecosystem: "gitsubmodule"
      directory: "/"
      schedule:
          interval: "daily"
          time: "06:00"
      labels: ["submodule", "automerge"]
```

With the above configuration, Dependabot will now look for updates every day at 0600 Hours UTC. If there're some updates to take care of, it'll then open respectives PRs with respective labels for _GitHub Actions_ & _Git Submodules_.

You can find further comprehensive details about configuring Dependabot in the official [_Dependabot Configuration Options_][Dependabot Docs] docs.

That said, now you no longer have to worry about update & manual maintenance tasks.

### Setting Up Forestry as a CMS Backend

No static blog can be considered a true _Wordpress alternative_ without a CMS. That is what makes Wordpress attractive to most users without a technical prowess. And as such, some users mightn't be comfortable writing their content in Markdown. For them a web-based [Rich Text Format][Rich Text Format] environment is what works.

Hence, we'll be using Forestry's backend CMS services. Although, there're alternatives like [Contentful][Contentful] (_one of the most popular one_) & [Netlify CMS][Netlify CMS], from my experience, Forestry is the most easy to use & configurable.

The things you can do with Hugo & Forestry is beyong the scope of this article. I could write another full-blown article just on this topic. So, keeping this article rather short & act as a guide for interested readers, here's a gist of how to setup Forestry.

1. Ensure you've Forestry account & your site is "_added_" to their services.
2. Configure the settings of the CMS from the Admin panel.
3. Login to your site's Admin panel by navigating to `<YOUR-SITE-URL/admin>` & start writing your content in Rich Text (_you can write in Markdown as well if you prefer_).

### Automation & Delegating Build Task to GitHub

While there's nothing wrong in using Netlify for building your site, there're certain limitations with the platform though. A major one being it's slow & unoptimized build times (_it took over 2mins for my site to build_). And with Netlify's limited 300 build mins per month, it won't take long before the free quota is used up.

So, to make the most out of Hugo's potential, you should use GitHub Actions. With it, you can build your site in <1mins (_usually takes 20-40secs on average_). Besides, compared to Netlify, GitHub provides 2000 build mins per month! So, coupled with less build times & a huge build mins quota, you won't have to worry about builds not triggering 😊.

And not to forget having all tools under one roof makes maintenance much easier to handle. So, let's quickly peruse through what we need to do automate some of the build tasks;

1. First thing first is to ensure you've a `netlify.toml` config file under the root directory. This config file will be used to tell how Netlify (_or rather the Netlify GitHub Action we'll be using_) should deploy the website. The file usually looks something like the following;

    ```toml
    # Post Processing Settings
    [build.processing]
      skip_processing = false
    [build.processing.css]
      bundle = true
      minify = true
    [build.processing.js]
      bundle = true
      minify = true
    [build.processing.html]
      pretty_urls = true
    [build.processing.images]
      compress = true
    ```

    You can find more details on what to include in this config file in the official [Netlify Config file][netlify.toml Docs] documentations.

2. Now you add a `build.yml` [workflow file][GitHub Actions Workflow] under the `.github` directory. Add the following content to the `build.yml` file.

    ```yaml
    name: Netlify Deploy

    on: push

    jobs:
        deploy:
            runs-on: ubuntu-latest
            steps:
                - uses: actions/checkout@v2
                  with:
                      submodules: true
                      fetch-depth: 0
                - name: Setup Hugo
                  uses: peaceiris/actions-hugo@v2
                  with:
                      hugo-version: "0.80.0"
                - name: Generate Static Content
                  run: hugo --minify
                - name: Deploy to Netlify
                  uses: nwtgck/actions-netlify@v1.1
                  with:
                      publish-dir: "./public"
                      production-branch: dev
                      production-deploy: true
                      github-token: ${{ secrets.GITHUB_TOKEN }}
                      deploy-message: "Deployed with GitHub Actions"
                      enable-pull-request-comment: true
                      enable-commit-comment: false
                      enable-commit-status: true
                      overwrites-pull-request-comment: true
                      netlify-config-path: ./netlify.toml
                  env:
                      NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
                      NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
                  timeout-minutes: 1
    ```

    The `build.yml` instructs GitHub Actions to use the [`peaceiris/actions-hugo`][Hugo Actions] & [`nwtgck/actions-netlify`][Netlify Actions] to deploy the generated site. Further it's triggered on every push & PR events.

3. And finally, the piece of automation fun. Automating merging PRs opened by Dependabot. Remember the `automerge` labels in the Dependabot config file? This is where they come handy. We'll use [`pascalgn/automerge-action`][Auto Merge Action] to automatically merge any Pull Requests with the label `automerge`. And guess what? Dependabot has been configured to updated every PR it opens with that label! 😆

Thanks to all the automation features, you no longer have to even open the repository ever again! Automation FTW indeed! 🤣

## Final Words

Phew, that was quite a long read for a tutorial! And if you read it till the end, then thanks for being thorough with it, I appreciate it. So, I hope it was enough to get you started

<!-- Reference Links -->
[GitHub Actions Workflow]: https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions
[netlify.toml Docs]: https://docs.netlify.com/configure-builds/file-based-configuration
[Contentful]: https://www.contentful.com/
[Netlify CMS]: https://www.netlifycms.org/
[Rich Text Format]: https://en.wikipedia.org/wiki/Rich_Text_Format
[Dependabot Docs]: https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates
[Dependabot]: https://github.com/dependabot
[GitHub's Dependabot]: https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/
[Netlify Build Operation]: https://docs.netlify.com/configure-builds/get-started/
[3 Reasons Why You Need a Programming Blog]: https://dbader.org/blog/3-reasons-why-you-need-a-programming-blog
[Hugo Homepage]: https://gohugo.io/
[GitHub Actions Docs]: https://docs.github.com/en/actions
[Netlify Homepage]: https://www.netlify.com/
[Google Analytics]: https://analytics.google.com/analytics/web/
[Cloudflare Analytics]: https://www.cloudflare.com/analytics/
[Forestry]: https://forestry.io/
[Hugo Actions]: https://github.com/peaceiris/actions-hugo
[Netlify Actions]: https://github.com/nwtgck/actions-netlify
[Auto Merge Action]: https://github.com/pascalgn/automerge-action
[Hugo Stargazers]: https://github.com/gohugoio/hugo/stargazers
[Hugo Binaries]: https://github.com/gohugoio/hugo/releases
[Markdown Homepage]: http://markdownguide.org/
[Hugo Themes]: https://themes.gohugo.io/
[New GitHub Repo]: https://repo.new
[Git Push]: https://docs.github.com/en/github/using-git/pushing-commits-to-a-remote-repository
[Pelican Homepage]: https://getpelican.com/
[Gatsby Homepage]: https://www.gatsbyjs.com/
[Jekyll Homepage]: https://jekyllrb.com/
[Hugo Installation Procedure]: https://gohugo.io/getting-started/installing/
[Hugo Project Directory]: https://gohugo.io/getting-started/directory-structure/
[Hugo Content Organization]: https://gohugo.io/content-management/organization/
[Netlify Git Deploy]: https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git
