---
title: "How to Create a Blog With Hugo (As a Wordpress Alternative)"
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

As mentioned earlier, Hugo is undeniably one of the easiest Static Site Generator available to use out there. This fact is further strenghtened by the [50K+ stargazers][Hugo Stargazers] who found it useful!

And it's ease of use is visible right from the installation procedure. All you got to do is [download the binaries][Hugo Binaries] for your local machine. Add the path to the binary to your system `PATH` & you can invoke the `hugo` command from anywhere in your preferred CLI. My strong suggestion is to give the official installation instructions a thorough read if you're stuck somewhere.

And fret not, the Hugo documentations are some of the most beginner-friendly I've ever come across. The devs were thorough & never made any assumptions about the Hugo user's competency & background.

You can check if Hugo was installed properly or not, by typing the `hugo --version` command on your CLI. And to get started with the fun parts, follow these instructions:

1. Invoke the `hugo new site .` to generate a skeleton content for a new site. Do note the `.` (dot) which tells Hugo to generate the content in the current directory. The command should generate a tree structure as such:

    ```bash
    .
    ├───archetypes
    ├───content
    ├───data
    ├───layouts
    ├───resources
    ├───static
    └───themes
    ```

2. Keeping things as minimal as possible, you can actually start creating content for the blog right away! You can write content in [Markdown][Markdown Homepage] under the `content` directory & you're good to go.
3. And about themes, you can download one of many from the [official Hugo themes site][Hugo Themes]. Even downloading a theme is as easy as running the `git submodule add <DOWNLOAD-LINK> themes/<THEME-NAME> --depth=1`. And that should download the theme to it's respective directory as a submodule.
4. And at last, you can easily generate the static content by running the `hugo` command on your CLI.

Easy peasy. Like I said, blogging couldn't get easier than that all thanks to Hugo!

But till now, we only looked into how to work with Hugo on our local machines. How do we deploy our site on the Internet for everyone to access & read the blogs is detailed in the next section. And beside that, we'll also look into how we can improve our quality of life by automating some of the most monotonous tasks.

## Deploying the Blog

Till now, all we did was work with Hugo to generate the static content on our local machines. And that's no good because then how do our audiences access the content to read? Which is why we need a static site hosting service like Netlify. And in addition to Netlify, we'll also use Forestry for their CMS services.

To do that ensure, you've created a Netlify &

As mentioned earlier, you'll need a GitHub repository to host the Markdown articles along with the other files required by all the others tools besides hugo. So, ensure you've created [a new repository][New GitHub Repo] to host those files. Once created, initialize your site directory & [push all the files to the remote repository][Git Push].

## Final Words

<!-- Reference Links -->
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
