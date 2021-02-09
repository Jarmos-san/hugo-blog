---
title: A Review of Some of the Most Popular Static Site Generators
date: "2021-02-04"
category: Blogging
slug: reviewing-popular-static-site-generators
summary: A brief review of the popular static site generators. Which one should you use, why & much more.
description: A brief review of the popular static site generators. Which one should you use, why & much more.
cover:
    image: "covers/static-site-generators-review.png"
    alt: "A visual of a woman confused while choosing between many available SSGs."
    caption: "So confusing! Which Static Site Generator should I use?"
    relative: true
showtoc: true
draft: true
---

The beginning of 2020 was when I wanted to start my own personalized blog. Suffice to say, as I shopped around with available options, I figured each software (_or platform_) has something or the other to offer. While there's Wordpress, it requires a server backend & periodic security management. That's something I didn't want to get into, if I didn't have to. All I wanted was a way write content in [Markdown][Markdown] & generate the static files (_think HTML + CSS + JavaScript files_) to be hosted on a CDN.

My initial attempt to do so was with [Jekyll][Jekyll] which didn't work out (_because I was still an inexperienced developer_). So, I jumped ship to [Gatsby][Gatsby] & [GitHub Pages][GitHub Pages] which didn't work out either! _\*sighs\*_. But on a brighter note, I did come to terms (_for a while_) with a pretty good Static Site Generator (SSG) called [Pelican][pelican].

Alas, I couldn't stay faithful to Pelican either for long. I'm using [Hugo][hugo] to generate the static content of the site you're reading off of right now. And you could say I'm pretty satisfied with the outcome, for now.

I might appear fickle-minded to you but rest assured, the lessons I learnt might be useful for you if you want to start your own blog.

That said, without further ado, let's review some of the most popular SSGs or at least the ones I've used.

## Specific Aspects That Makes a SSG Worth It

On my journey towards trying out a number of SSGs, I discovered none is better than the other. Each has something unique to offer. Perhaps, your site has a lot of individual pages then Hugo will be a good choice. Or maybe you need a modern & fast website, then Gatsby should be your choice. While having choices are a good thing, reviewing each tool against each other is hard (if not close to impossible). Hence, I thought it would be better to list out some common grounds where each SSG could be compared against each other.

That said here are the common points I considered for reviewing each SSG:

- **Easy installation process** - As in, installing the tool(s) required to get the SSG in question up & running shouldn't be difficult even for a non-technical individual.
- **Legibility of the documentations** - Can't emphasis on this point enough! I'll discuss in more details on the importance of this point.
- **Ease of use** - A subjective point-of-view since what's easy for me to use mightn't be the same for the other individual. More on it will be discussed in the rest of the article.
- **Availability of good-looking & modern themes** - This point is almost a no-brainer. Why would someone not choose Wordpress with so many good-looking & modern themes over SSGs. Living in the 21st century, support for good-looking themes (_paid/free_) is a must-have for any SSGs.
- **Ease of customizing the available themes** - You got hold of you preferred SSG, discovered a nice theme (_extra kudos if it was free & open-sourced_), all good & dandy. But there's just some subtle thing about the theme bothering you, maybe the font or maybe the background color. Whatever it be, the themes you use for your blog has to let you customize it in some way or the other.

So, those were some of common aspects which all SSGs I review should've at the least. It's not worth using a particular SSG which lacks any of the mentioned points above.

That said, lets dive into it & check out which SSG is great for you & your workflow.

## Jekyll & GitHub Pages

Jekyll is [advertised as a one-stop solution][GitHub Pages Docs] for all your blogging needs. It's expected to work out-of-the-box without much configuration & complicated setup. And by far its one of the most easiest to use among all the other SSGs mentioned in this article. Coupled with being to easy to install, the software is well documented. And the official documentation is hosted on [jekyllrb.com/docs/][Jekyll Docs].

With respect to its ease of use, things get interesting here. Well, you see, installing Jekyll locally isn't a strict requirement in the first place. You could write a single-page site (by hand!), save it as `index.html`, push it to a remote repository named `https://<YOUR-USERNAME>.github.io` & GitHub will serve your site powered by Jekyll themes. Check out the official [GitHub Page][GitHub Pages] landing page for more clarification on the same.

Think to yourself, do you want to write the markup files, by hand? If that's you, heck you won't even need a SSG in the first place then! But ask me, you're better off using a SSG to generate the static files. You'll find less errors in the markup & besides, using a SSG just enables good SEO practices by default.

That said, I observed Jekyll has the largest collection of themes. While some are free & maintained by the community, there're premium ones as well. So, regardless of if you're looking to create a blog or landing page for your business, there's bound to be a theme for you out there. A great place to find some themes is the official [Jekyll themes][Jekyll Themes] page (_they're all **free**_ :wink:). Perform a customary Google search for "_Jekyll themes_" and you'll find more of them scattered across the Internet.

Customizing Jekyll themes isn't as straightforward as the using Jekyll itself to generate the static content though. In addition to the [Liquid][Liquid] templating language, Jekyll provides additional utilities to help you customize your site. So, if you're not familiar with the idea of templating languages, then you'll have to be satisfied with what the themes provide out-of-the-box.

But on a brighter note, JavaScript & frontend developers, you might find better luck with the next SSG (_or rather a framework_), Gatsby.

## Gatsby: A React.js Framework to Build Static Sites

## Pelican: A Static Site Generator Built With Python

## Hugo: The Fastest Static Site Generator Ever Created

## Final Thoughts

<!-- Reference Links -->
<!-- * Landing Pages -->
[Liquid]: https://shopify.github.io/liquid/
[Markdown]: https://www.markdownguide.org/
[Jekyll]: https://jekyllrb.com/
[Gatsby]: https://www.gatsbyjs.com/
[GitHub Pages]: https://pages.github.com/
[Pelican]: https://blog.getpelican.com/
[Hugo]: https://gohugo.io/
<!-- * Documentations -->
[GitHub Pages Docs]: https://docs.github.com/en/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll
[Jekyll Docs]: https://jekyllrb.com/docs/
[Jekyll Themes]: https://jekyllrb.com/docs/themes/
