---
title: "Medium Vs Static Site Generators — A Computer Vision Engineer’s Dilemma"
date: "2020-05-12"
slug: medium-vs-static-site-generators
category: Software
summary: The wide array of choices for blogging platforms & tools can be overwhelming. As such, I was confused too, but you don’t have to be, so read ahead.
description: The wide array of choices for blogging platforms & tools can be overwhelming. As such, I was confused too, but you don’t have to be, so read ahead.
cover:
  image: "https://miro.medium.com/max/1458/0*mkZqMAqpwEB8sKU7"
  alt: "Crossroads sign post"
  caption: "Photo by Robert Ruggiero on Unsplash"
  relative: false
showtoc: true
---

The day I took a plunge & went full-time freelance, a lingering thought has bothered me ever since; “How do I make my presence known to my prospective clients?”.

A quick Google search on the same question helped me come up with the following quick conclusions:

1. “_Share content out there through blog posts._”
2. “_Be consistent about writing._”
3. “_Maintain a personal blog site._”

Cool! I got the “answers” I was looking for, as I thought & wondered, “how am I supposed to set up a website that I can call my own?”

Enter Static Site Generators(SSGs) & SSG Hosts like GitHub Pages & Netlify were the few that I tried, albeit miserably.

So here’s my opinionated documentation of the ordeal I suffered from for the past year or so while trying to build my own identity on the Internet.

## Choosing the Right SSG

Perhaps I’m wrong about it but as far as I know, SSGs are supposed to ease our lives. Little did I know, even they come packed in with a slight learning curve. For example, [Gatsby](https://www.gatsbyjs.org/), a React framework promising developers to build blazing static sites does live up to its expectation but with a catch!

_Prior knowledge about React Components is a massive added advantage._

Similarly, _Hugo_ & [Pelican](https://blog.getpelican.com/) are based on Golang & Python programming languages, respectively. The former is quite simple & easy to use, not to forget how the super-fast the build times are but lacks detailed documentation. This stumbling block was a major setback for me as I did not know to code on Go.

Hence, without a doubt in mind, I chose Pelican as a supposedly perfect alternative for building the site as I was already proficient with Python. Problem solved, I got back to my comfort zone, everything’s fine & dandy or that’s what I thought it would be.

Heck, if that was the case, I wouldn’t be writing this article, would I?

The major setback of setting up a site using Pelican is its themes, in general. Don’t get me wrong, the authors of Pelican have detailed everything in the documentations but the existing themes just lack some lustre. Perhaps, if only they did focus on improving that aspect of their product, more users would flock towards using Pelican as their go-to SSG. In fact, it’s the eye-catching & modern-looking themes that make the other popular SSGs, Gatsby & Hugo, what they’re among their users.

On a side note though, Pelican does allow customizing the existing themes as much as I wanted but think about it for a second. Would you compromise your time & effort in tinkering with front-end web development stuff when your precious time could be better utilized elsewhere, like running a business?

By now you must be wondering, I should’ve just chosen GitHub Pages in the first place considering its built-in support for static pages powered by Jekyll. All that’s required of me was to upload the static pages to a repository & host it in a _“<username.github.com>”_ subdomain.

Well, I could do that but did you take a look at the list of supported themes? Check them out at [GitHub Pages Supported Themes](https://pages.github.com/themes/). Most of them sport a minimalist look which is pretty satisfactory for “just blogging” which can be customized to my heart’s content but then again why should I bother?

## What’s the fuss about theming & designs

There’s something called “_Visual Hierarchy_” & it consists of 6 principles. Bear in mind, I’m no designer by profession so it’s a waste of effort & time, if I had to customize my themes adhering to the time-tested principles of visual hierarchy.

But briefly put, the principles states the following:

1. _Reading Patterns_ — Certain optimized ways to get the readers’ short attention span.

2. _Just The "**Right**" Font Size_ — Explains how using an optimal font size is useful to grab the reader’s attention & make them feel obligated to read further.

3. _Space & Texture_ — This is a testament that adequate spacing between lines & other content is key to creating modern-looking sites on the Internet today.

4. _Typeface Weight & Pairing_ — Mostly crucial for branding as this is what brings about specific characteristic looks & visuals of a brand on the Internet.

5. _Color & Tint_ — Humans perceive visual characters more prominently than any other beings on the planet. Using the right colour & tint in your themes is of utmost importance.

6. _Direction_ — Perhaps the most crucial principle of all is the page layout of the site. This is how the writer can make the most out of the reader’s short attention span. No single site will have obviously the same page layout as the other & each of them is usually optimized according to its audience.

Hence, as you can see those were quite a handful of principles to keep in mind. By doing so, makes the reader comfortable reading the content. It’s an obligation a writer has to adhere to strictly.

For more information definitely this, _6 principles of Visual Hierarchy For Designers_, a blog post written by the guys at _99designs_, a read. [1]

## Medium Appears To Be the “Perfect” Alternative

To be honest, no platform is perfect! At least none that I could find till now, in my opinion, but I’ll have to live with what’s available for now.

Certain aspects of Medium, I dislike are the obligations to share content behind a paywall to be eligible for curation & publishing the content with major publishers in order to find more eyeballs on my content. Granted it’s not enforced on me to necessarily publish an article behind a paywall or with a publication but let’s face it, if I didn’t, my articles willn’t accumulate enough readers.

Regardless of Medium’s setbacks, I find the platform still good enough for my purpose! With built-in SEO tools, a UI, specifically designed keeping in mind the _Principles of Visual Hierarchy_ & much more. To be honest, asking for more would be too greedy of me.

Besides, until I came across [Jason Weiland](https://medium.com/@jasonjamesweiland)’s article — “[4 Types of Creatives Who Don’t Need a Blog or Website](https://medium.com/better-marketing/4-types-of-creatives-who-dont-need-a-blog-or-website-4b70697d0c41)”, I was still stuck in the dilemma.

The final nail in the coffin for me was when I read the following line from his article & I quote.

>     *Do we need to be adding to the noise on an already crowded web?*

Granted, Jason’s article was primarily targeted towards a very specific niche of creative writers. But advice on improving one’s writing skills, in general, is all the same, irrespective of one another’s field of expertise.

## Wrapping Up & The Reasons Behind Choosing Medium Over a Personal Blog Site

1. Setting up a personal site doesn’t mean I would find an audience right then there. Medium makes my job significantly easier with over 200M total visits from around the world to the site(**as of writing this article**).[3]

2. No additional hosting expenses required, neither is there any need to worry about “_building_” my site.

3. The built-in SEO tools are way too good to overlook! As of writing this article, Alexa ranks the site at 87 in global Internet engagement. [4]

So from a Machine Learning Engineer’s point-of-view Medium appears to be just the right platform to share his/her ideas and/or content. No more tinkering around with Dev Ops or Web Dev stuff. I can now put aside the idea of owning my personal site temporarily & focus on delivering content to my audience first. Anything else to worry about can be taken care of tomorrow.

## References

[1] [Alex Bigman](https://99designs.com/blog/author/alex-bigman/), [6 principles of visual hierarchy for designers](https://99designs.com/blog/tips/6-principles-of-visual-hierarchy/) (2019), [99designs](https://99designs.com/).

[2] [Jason James](https://medium.com/@jasonjamesweiland), [4 Types of Creatives Who Don’t Need a Blog or Website](https://medium.com/better-marketing/4-types-of-creatives-who-dont-need-a-blog-or-website-4b70697d0c41) (2020), [Better Marketing](https://medium.com/better-marketing)

[3] medium.com Analytics, [Similar Web](https://www.similarweb.com/website/medium.com) (_accessed on 5th May, 2020_)

[4] medium.com Competitive Analysis, Marketing Mix & Traffic, [Alexa](https://www.alexa.com/siteinfo/medium.com) (_accessed on 5th May, 2020_)
