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

## Important Aspects Making a Static Site Generator Worth a Try

On my journey towards trying out a number of SSGs, I discovered none is better than the other. Each has something unique to offer. Perhaps, your site has a lot of individual pages then Hugo will be a good choice. Or maybe you need a modern & fast website, then Gatsby should be your choice. While having choices are a good thing, reviewing each tool against each other is hard (if not close to impossible). Hence, I thought it would be better to list out some common grounds where each SSG could be compared against each other.

That said here are the common points I considered for reviewing each SSG:

- **Easy installation process** - As in, installing the tool(s) required to get the SSG in question up & running shouldn't be difficult even for a non-technical individual.
- **Legibility of the documentations** - Can't emphasis on this point enough! I'll discuss in more details on the importance of this point.
- **Ease of use** - A subjective point-of-view since what's easy for me to use mightn't be the same for the other individual. More on it will be discussed in the rest of the article.
- **Availability of good-looking & modern themes** - This point is almost a no-brainer. Why would someone not choose Wordpress with so many good-looking & modern themes over SSGs. Living in the 21st century, support for good-looking themes (_paid/free_) is a must-have for any SSGs.
- **Ease of customizing the available themes** - You got hold of you preferred SSG, discovered a nice theme (_extra kudos if it was free & open-sourced_), all good & dandy. But there's just some subtle thing about the theme bothering you, maybe the font or maybe the background color. Whatever it be, the themes you use for your blog has to let you customize it in some way or the other.

So, those were some of common aspects which all SSGs I review should've at the least. It's not worth using a particular SSG which lacks any of the mentioned points above.

That said, lets dive into it & check out which SSG is great for you & your workflow.

## Jekyll: The Static Site Generator That Powers GitHub Pages

Jekyll is [advertised as a one-stop solution][GitHub Pages Docs] for all your blogging needs. It's expected to work out-of-the-box without much configuration & complicated setup. And by far its one of the most easiest to use among all the other SSGs mentioned in this article. Coupled with being to easy to install, the software is well documented. And the official documentation is hosted on [jekyllrb.com/docs/][Jekyll Docs].

With respect to its ease of use, things get interesting here. Well, you see, installing Jekyll locally isn't a strict requirement in the first place. You could write a single-page site (by hand!), save it as `index.html`, push it to a remote repository named `https://<YOUR-USERNAME>.github.io` & GitHub will serve your site powered by Jekyll themes. Check out the official [GitHub Page][GitHub Pages] landing page for more clarification on the same.

Think to yourself, do you want to write the markup files, by hand? If that's you, heck you won't even need a SSG in the first place then! But ask me, you're better off using a SSG to generate the static files. You'll find less errors in the markup & besides, using a SSG just enables good SEO practices by default.

That said, I observed Jekyll has the largest collection of themes. While some are free & maintained by the community, there're premium ones as well. So, regardless of if you're looking to create a blog or landing page for your business, there's bound to be a theme for you out there. A great place to find some themes is the official [Jekyll themes][Jekyll Themes] page (_they're all **free**_ :wink:). Perform a customary Google search for "_Jekyll themes_" and you'll find more of them scattered across the Internet.

Customizing Jekyll themes isn't as straightforward as the using Jekyll itself to generate the static content though. In addition to the [Liquid][Liquid] templating language, Jekyll provides additional utilities to help you customize your site. So, if you're not familiar with the idea of templating languages, then you'll have to be satisfied with what the themes provide out-of-the-box.

But on a brighter note, JavaScript & frontend developers, you might find better luck with the next SSG (_or rather a framework_), Gatsby.

## Gatsby: A React.js Framework to Build Static Sites

Gatsby advertises themselves as that one SSG to create blazing fast modern websites. And they do live upto their promise with websites which loads up in fractions of a second! But unlike most other SSGs mentioned in the article Gatsby is more of a framework based around React components.

I believe, while it did work out for most JavaScript developers, other developers who doesn't write JS, are left out of the loop. This is both a boon and a bane as you'll see further ahead into this section.

On the hand, Gatsby is pretty easy to install. All you got do is call the `npm install -g gatsby-cli` command to perform a global install of everything you require on your local machine. Nothing could get easier then installing Gatsby. No need to mess around with environment variables. Neither do you've to download binary files like you would've to do with Hugo.

But, everything in software development comes with some trade-off. What could that trade-off be in case of Gatsby, we'll look into it.

On a brighter note, the Gatsby devs revamped the Gatsby homepage as well as their new [documentation][Gatsby Docs] page. And I've to say their new site design looks pretty nifty & easy to use. With specific sections for "_Tutorials_", "_How-to Guides_", etc, documentations couldn't be made more appealing than what the Gatsby has done.

So, kudos to them for making their documentation page as accessible & appealing as possible.

Now here's the interesting part about reviewing Gatsby. If you're a JavaScript developer (more so if you're a frontend developer), this should be your most preferred go-to SSG. Period. Allow me to explain why I think so.

**It has an integrated GraphQL API (and an web-based GraphQL IDE)**. While it's optional & if you find using GraphQL difficult, there're options to opt out of it. This API powers Gatsby to sources data from anywhere, be it a web-based CMS like [Forestry.io](https://forestry.io/) or your own file system.

So, if you've no experience whatsoever working with backend systems, look no further. Heck, there're even tutorials to hook up a Firebase database to your Gatsby Blog & you're good to go. No longer do you've to setup backend servers & what not. All you've to do is stick to what you're already good at.

If things couldn't become even more simpler, the ecosystem Gatsby brings in more goodies for the user. It's plugin system & wide-range of available themes. Coupled with the wide range of available themes & an extensive plugin system, what you capabilities you could provide to your site is close to limitless.

And then there're people who say, "frontend developers aren't real programmers" :face_with_raised_eyebrow:. If you ask me, what the Gatsby devs did out there, enabling backend capabilities to a frontend software is pretty praiseworthy.

But, while everything appears good & dandy with Gatsby, there's a caveat. It was built keeping in mind a frontend developer's skills, requirements & tool sets in mind. So, unless you're pretty good JavaScript (adn/or React), you're out of luck. And that's a major hit back to an otherwise really awesome piece of software in my opinion.

Using Gatsby was just too difficult for me to use. Since, not only did it require me to know JS but understanding how React components worked was pretty much a neccessity if I wanted to customize the themes even the slightest bit. :pensive_face:

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
[Gatsby Docs]: https://www.gatsbyjs.com/docs/
