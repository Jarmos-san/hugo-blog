---
title: A Review of Some of the Most Popular Static Site Generators
date: 2021-02-04
category: Blogging
slug: reviewing-popular-static-site-generators
summary: A brief review of the popular static site generators. Which one should you use, why & much more.
description: A brief review of the popular static site generators. Which one should you use, why & much more.
cover:
    image: "covers/static-site-generators-review.png"
    alt: "A visual of a woman confused while choosing between many available SSGs."
    caption: "So confusing! Which Static Site Generator should I use?"
    relative: true
showtoc: false
draft: false
---

When I started blogging, I was looking for a platform to host my content on. I shared my dilemma in a previous article. Check it out at: [Medium Vs Static Site Generators--A Computer Vision Engineer’s Dilemma](./static-site-vs-medium.md). Suffice to say, a year later I use both, [Medium][My Medium] & a SSG to create [my blog][My Blog].

But choosing the right [Static Site Generators][SSG] (SSGs) was never an easy task. I looked around. Tried a couple of available options. And I figured something out. Each site generator was unique in some way or the other & will have some advantage over the other.

Keeping that in mind, I had to jot down my specific requirements. And the following were my blogging needs:

1. Write content in [Markdown][Markdown].
2. Focus on delivering quality content over aesthetics. Avoid spending time on hacking & setting up a dev environment.
3. Automate certain aspects of my workload as much as possible.

My lack of experience didn't help either & my initial attempt to do so with [Jekyll][Jekyll] failed. So, I jumped ship to [Gatsby][Gatsby] & [GitHub Pages][GitHub Pages] which didn't work out either! *sighs*. So, I made another quick switch to [Pelican][Pelican] & used it to work with some of my first few articles.

Alas, I couldn't stay faithful to Pelican either for long. I justified my reasoning to switch often from one tool to the other further in the article. But, [Hugo][hugo] hasn't disappointed me til now, so let's see how long can I stick with it.

Besides, if you read till here, you might wonder to yourself, how fickle-minded I'm. Perhaps I'm fickle-minded. But if there's anything I learned from the experience. It would be my unbiased opinion on how the various SSGs achieve the same goal albeit in their own way. Hence, I wanted to share my learnings & leave a detailed review of the software with my audience.

So, without further ado, let's review some of the most popular Static Site Generators, or at least the ones I used.

## Common Aspects All SSGs Should've (By Default)

Comparing one SSG with another is no easy task. They all serve one single purpose i.e to generate static contents. The static content (_think HTML, CSS & JS files_) are then served through a CDN over the Internet. Hence, there's no one site generator better than the other(s).

But, for the sake of brevity & a precise review, we need to review each site generators on  common grounds. So, reviewing the site generators will be easier (_and relevant to individual needs_).

That said, following are the common aspects to review each site generators:

- **Easy installation process** - Installing a site generator shouldn't be rocket-science. It should be easy enough for even a non-technical person to set up with the least amount of roadblocks.

- **Legible documentations** - Can't emphasis on this point enough! A seasoned developer might hack around with insufficient instructions & still resolve their issues. The same can't be said about a non-technical person. So, the easier the docs are to follow, the better the SSG is.

- **Ease of use** - While documentations ease using the tool, it's not always the case with certain tools. An example would be Pelican & its use of Jinja templates. Or Jekyll & Liquid templates for customizing the site's aesthetics. These extra tools can often increase the learning curve of using a tool. Hence, in a hypothetical world an SSG with no extra tools is the perfect tool for the job. So, if your preferences are to produce content, choose the tool with little to no extra fluff.

- **Availability of themes** - I don't see why a site generator shouldn't provide a wide range of themes to choose from. Especially when there're alternatives like [Wordpress][Wordpress] & [Wix][Wix]. Availability of themes is a must, doesn't matter if they're paid or free.

- **Ease of customizing themes** - What's the point of having a ready list of themes if you can't customize them to your needs. Considering the importance of branding & personalization, not providing this option is a no-brainer. We'll see how easy it is to customize the themes of your choice. And extra kudos if the themes are open-sourced! :heart:

So, those were some common grounds all the site generators in question will be reviewed upon.

That said, lets dive into it & review the site generators.

## Jekyll: The Static Site Generator That Powers GitHub Pages

Jekyll is [advertised][GitHub Pages Docs] as a one-stop solution for all your blogging needs. It's expected to work out-of-the-box without much configuration & complicated setup. And by far it's one of the easiest to use among all the other SSGs mentioned in this article. Coupled with being too easy to install, the software is well documented. And the official documentation is available at: [jekyllrb.com/docs/][Jekyll Docs].

About its ease of use, things get interesting here. Well, you see, installing Jekyll on your local machine isn't needed in the first place. You could write a single-page site (_by hand_!). Save it as `index.html`, push it to a remote repository named `https://<YOUR-USERNAME>.github.io`. And GitHub will serve your site powered by a Jekyll theme of your choice.

Working with Jekyll is as easy as that. Check out the official [GitHub Page][GitHub Pages] landing page for more clarification.

But think to yourself, do you want to write the markup files, by hand? If that's you, heck you won't even need a SSG in the first place then! But ask me, you're better off using a SSG to generate the static files. You'll find less errors in the markup & besides, using a SSG enables good SEO practices by default.

That said, I observed Jekyll has the largest collection of themes. While some are free & maintained by the community, there're premium ones as well. So, if you're looking to create a blog or a landing page for your business, there's bound to be a theme for you out there. A great place to find some themes is the official [Jekyll themes][Jekyll Themes] page (_they're all **free**_ :wink:). Perform a customary Google search for "_Jekyll themes_" and you'll find more of them.

Customizing Jekyll themes isn't as straightforward as using Jekyll is though. You'll need to learn using a templating language called [Liquid][Liquid]. On top of which, Jekyll even provides more utilitarian tools to help you customize your site. So, if you're unfamiliar with templates, you'll have to make use of the available themes only.

But on a brighter note, there's good news for JavaScript & frontend developers. You might find better luck with the next SSG (_or rather a framework_), called Gatsby.

## Gatsby: A React.js Framework to Build Static Sites

Gatsby advertises themselves as that one SSG to create blazing fast modern websites. And they do live up to their promise with websites with seemingly non-existent load times! But unlike most other SSGs mentioned in the article, Gatsby is more of a framework. It's based around React components, hence why it's considered a framework rather than a SSG.

While it works out well for JavaScript developers other developers might feel left out. You see, to make the most out of Gastby, you would've to be pretty good at JS first. Experience with React components is also a plus point. But, not every developer knows JavaScript. And besides, learning a new language isn't something you can do overnight.

But on a brighter note, Gatsby is pretty easy to install. You can install it globally with the `npm install -g gatsby-cli` & you're good to go.  Nothing could get easier than installing Gatsby. No need to mess around with environment variables.

Once installed, the CLI can download the themes as well as generate the static content. The whole process is one single step. There's no manual steps involved with setting up themes.

Gatsby [documentations][Gatsby Docs] also appears revamped. And I've to confess their new site design looks pretty nifty & easy to use. With sections for "_Tutorials_", "_How-to Guides_", etc, the docs couldn't be more easier to navigate.

So, kudos to them for making their docs as accessible & appealing as possible.

But here's the interesting part about reviewing Gatsby. It was built keeping in mind JS developers & their tool kit. So, if you're a JS developer (_more so if you're a frontend developer_), look no further.  You won't find anything better than Gatsby.

**It has an integrated GraphQL API (_and an web-based GraphQL IDE_)**. While it's optional & if you find using GraphQL difficult, there're options to opt out of it.

The GraphQL API powers Gatsby to source data from anywhere. Need your Markdown files sourced from a web-based CMS then Gastby got you covered? Or is sourcing your content from the file-system your preference? Then Gatsby got you covered there as well!

So, if you're inexperienced working with backend systems, look no further. Heck, there're even [tutorials][How to Deploy a Gatsby Static Website to Google Firebase] to hook up a Firebase database to your Gatsby Blog & you're good to go. No longer do you've to set up backend servers & what not. All you've to do is stick to what you're already good at, if you're a frontend developer.

But things don't end here either! The Gatsby ecosystem brings in more goodies for the user. It's plugin system & wide-range of available themes is incomparable. With the wide range of available themes & an extensive plugin system, what you could do with your blog is limitless.

And then there are people who say, "frontend developers aren't real programmers" :face_with_raised_eyebrow:. If you ask me, the Gatsby devs did a great job. Enabling backend capabilities to a frontend software is pretty praiseworthy.

But, while everything appears good & dandy with Gatsby, there's a caveat. As mentioned earlier it was built with a frontend developer's point-of-view. So, unless you're pretty good JavaScript (_and/or React_), you're out of luck. And that's a major hit back to an otherwise awesome piece of software.

Suffice to say, being a Python developer, using Gatsby was too difficult to use. If I had to customize the theme even just a bit, I had to be adept at JavaScript. And not to forget an in-depth understanding of React Components as well. :pensive_face:

## Pelican: A Static Site Generator Built With Python

So, if frontend skills aren't my forte, what're the other available options?

This is where  [Pelican][Pelican], a static site generator built with Python shines. So, you'll need to have Python installed on you machine as well.

Besides, if you're a backend developer chances are, [Python][Python] is already installed on your system.  So, installing Pelican is only a `pip` command away. It's as easy as running the `pip install pelican` command & you'll have Pelican working.

Out-of-the-box Pelican supports files written in `.rst` format. But you can even write your articles in Markdown. You'll only need to install the dependencies with the `pip install "pelican[markdown]"` command. That should install the extra stuff for converting Markdown files to HTML.

But on the flip side, the software is over a decade old at the time of writing this article. Hence, unlike the other site generators, Pelican appears bland. And I assume parts of it's API might even be very difficult to peruse through for the current developers.

Also Pelican's age does show everywhere. It's landing page looks like it was built back in the early 90s. The themes & configuration system are primitive too. For some, it could be a major deal-breaker & unappealing. And they're right to feel so.

Pelican sites are configured with [global variables][Python Global Variables] in a `pelicanconf.py` file. Some of the variables are preset by Pelican while theme authors can add their own variables as well. In other words, Pelican can make use of an arbitrary range of settings! It might sound good right away but, for Pelican, it didn't work out so well as you'll see soon.

Like most well-maintained Python projects, Pelican is also maintained by an active team of developers. They've documented the software well enough but it could be made better. It's a problem other Python projects face as well. This is so because the authors rely on automatic generation of their docs off of the docstrings from the source code. Hence, you might often notice a lack of "human-touch" with certain Python project documentations.

Regardless, most documentation issues can be handled. But I fear the same can't be said for the Pelican community. While there's a ton of available themes for Pelican, but guess what? Most of the themes aren't maintained ([source][Pelican Themes Aren't Well Maintained])!

So if you're using Pelican with a theme, good luck if you come across an issue with it. Remember how Pelican theme authors could add their own arbitrary settings on top of the preset ones? Well this is where it came back to bite the Pelican ecosystem.

Imagine you find a theme that you like. Install it for your blog, only for it to break with the latest Pelican installation. And there's no way for you to fix it because the theme author hadn't made a commit to the repo for 5 years now. Saddening, isn't it?

On top of it, as mentioned earlier, most of the themes look aged & bland. You could customize them or create one from scratch. But that requires knowledge of working with [Jinja 2][Jinja] templates. And Jinja templates do have a slight learning curve to it as well. So, good luck working with it when your time could be better spent blogging instead.

So, at the end of day when/why should you use Pelican? You're a Python backend developer with experience working on Jinja templates. And besides, if SEO & other aesthetic values of your site doesn't matter to you, then Pelican is the right option for you.

But, what if you care about efficiency & proper time management? Then there's Hugo for you. The next section details a review about Hugo as an SSG.

## Hugo: The Fastest Static Site Generator Ever Created

[Jamstack][Jamstack list] ranks Hugo, the second-most popular site generator. Its followed by Gatsby only by a fraction of _GitHub Stars_.

Besides, it's also one of the few non-JS software in a domain filled by JavaScript framework(s). Its rise to popularity arose mainly due to it's speed of generating static content. Plus its availability of pretty, modern & SEO-friendly themes is an underrated aspect as well.

Hugo was built with [Go][Golang], so you only need to invoke a binary file to start using Hugo. No installation required. You can find a verbose installation instruction at the "[Getting Started][Hugo Getting Started]" section of the official docs.

Also something to note here, the Hugo docs are the most detailed documentations I've ever seen anywhere else till now. And the devs are verbose with the rest of the docs as well. So, extra kudos to them!

And if it's not obvious by now, I can't appreciate the Hugo dev's effort in making their docs as inclusive as possible! The attention to verbosity they've given is praiseworthy. They left no corners untouched while articulating the docs. So my fellow Python devs, take some lessons from the Hugo devs on how-to write good documentations. :winking_face_with_tongue:

Besides, being able to invoke a single binary file, installing Hugo themes is also a piece of cake. All you got to do clone your preferred theme(s) into the `./theme/` directory. Ensure your Hugo knows which theme to use by updating the `config.yml` file & you're set with a theme.

Also, trust me on it but, you're going to spend a day or two perusing through the available [list of themes][Hugo Themes]! Not only are each of them pretty & modern, most of them are well maintained & are SEO-friendly.

On that note, if you're wondering how easy it is to customize the themes, I would say, they're not difficult. And besides, the official Hugo docs got your back in case you get stuck somewhere. :wink:

All you've to know before going down the custom-shop lane (_or even building your own theme_) is [Go Templates][ Go Template ]. Hugo uses Go's powerful templating language. Unlike Liquid and/or Jinja2, Go templates are very intuitive. And best of all, you don't have to abandon your existing frontend skills either. Coupled with Go templates you can build websites that won't look like static sites at all.

So, if you ask me? I would say Hugo would be your best bet regardless of any specific needs and/or you skill level. And that's coming from a Python developer with no experience working with Golang and/or JavaScript! With Hugo, I can focus on producing more content rather than develop frontend stuff.

## Verdict

Well was it not hard for me to review each of those tools & decide which would suit which kind of users. So, here are my final thoughts on choosing the right tool for individual needs. And to make it even easier for you to summarise a rather lengthy piece of article, I've made an infographic for it. So, the next time you're confused which site generator to use, the infographic will come handy.

![Choosing the Right Static Site Generator Infographic][Infographic]

With everything said & done, do let me know if you enjoy reading these contents. Do let me know through my [contact details](../../about/#contact-me).

<!-- Reference Links -->
<!-- * Assets -->
[Infographic]: https://res.cloudinary.com/jarmos/image/upload/v1613158461/static-site-generator-review-infographic_qwrw0z.jpg  "Choosing the Right Static Site Generator"
[How to deploy a Gatsby Static Website to Google Firebase]: https://youtu.be/Lk9Cj8a6QJg
<!-- * Landing Pages -->
[Jamstack list]: https://www.jamstack.com/generators/
[Python]: https://www.python.org/
[Jinja]: https://jinja.palletsprojects.com/en/2.11.x/
[Liquid]: https://shopify.github.io/liquid/
[Markdown]: https://www.markdownguide.org/
[Jekyll]: https://jekyllrb.com/
[Gatsby]: https://www.gatsbyjs.com/
[GitHub Pages]: https://pages.github.com/
[Pelican]: https://blog.getpelican.com/
[Hugo]: https://gohugo.io/
[Hugo Themes]: https://themes.gohugo.io/
[Golang]: https://golang.org/
[Wordpress]: https://wordpress.com/
[Wix]: https://www.wix.com/
<!-- * Documentations -->
[GitHub Pages Docs]: https://docs.github.com/en/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll
[Jekyll Docs]: https://jekyllrb.com/docs/
[Jekyll Themes]: https://jekyllrb.com/docs/themes/
[Gatsby Docs]: https://www.gatsbyjs.com/docs/
[Python Global Variables]: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
[Pelican Themes Aren't Well Maintained]:https://github.com/getpelican/pelican-themes/issues/677
[Hugo Getting Started]: https://gohugo.io/getting-started/installing
[Go template]: https://golang.org/pkg/text/template/
[SSG]: https://www.cloudflare.com/learning/performance/static-site-generator/
<!-- * Personal Information -->
[My Newsletter]: https://jarmos.ck.page/newsletter
[My Twitter]: https://twitter.com/Jarmosan
[My Blog]: https://jarmos.netlify.app/
[My Medium]: https://jarmos.medium.com/
