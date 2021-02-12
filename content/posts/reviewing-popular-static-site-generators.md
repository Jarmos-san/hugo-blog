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

When I started out, choosing the right [Static Site Generators][SSG] (SSGs) to create my blog was a difficult task. I looked around. tried a couple of available options. And I figured something out. Each site generator were unique in some way or the other & will have something advantage over the other.

Keeping that in mind, I had to jolt down my specific requirements. And following were my blogging needs:

1. Write content in [Markdown][Markdown].
2. Prioritise delivering quality content over aesthetics & uneccessary hacking skills on setting up the development environment.
3. Automate certains aspects of my workload as much as possible.

My initial attempt to do so was with [Jekyll][Jekyll] didn't work out very well (_I was an inexperienced developer_). So, I jumped ship to [Gatsby][Gatsby] & [GitHub Pages][GitHub Pages] which didn't work out either! _\*sighs\*_. So made a quick switch to [Pelican][Pelican] & used it to generate some of my initial articles.

Alas, I couldn't stay faithful to Pelican either for long. More on why I made the switch from Pelican to Hugo is explained further ahead into the article. [Hugo][hugo] hasn't failed to disappoint me until now, so let's see how long do I stick to it.

If read till here, you might wonder to yourself, how fickle-minded I'm. Perhaps I'm, but if there's one thing I gained from using those software it would be an in-depth first-hand experience of using them. Hence, I wanted to share what I learned & leave a detailed review of the software with my audience.

So, without further ado, let's review some of the most popular Static Site Generators, or at least the ones I used extensively.

## Common Aspects All SSGs Should've (By Default)

Comparing one SSG with another is no easy task, they all serve one single purpose i.e to generate static contents to be served over the Internet through a CDN. Hence, there's no one site generator better than the other(s).

But, for the sake of brevity & a precise review, I felt the need to review the site generators keeping in mind certain common aspects. Hence, even though they deliver the end results in different ways reviewing the site generators will be much easier (_and relevant to individual needs_).

That said, following are the common aspects to review each site generators:

- **Easy installation process** - As in, installing the tool(s) required to get the site generator in question up & running. It should be easy enough even for a non-technical individual to setup with the least amount of roadblocks.
- **Legibility of the documentations** - Can't emphasis on this point enough! In context to the first point, while a seasoned developer might be able to hack around with insufficient documentations, it might be a total nightmare for a non-technical person. So, the easier the docs are to follow, more additional kudos for that site generator.
- **Ease of use** - While having a proper documentation in place can alleviate the problem of the tool being difficult to use, it's not always the case with certain tools. An example would be Pelican & it's use of Jinja templates. Or Jekyll & Liquid templates for customizing the site's aesthetics. These additional tools can often increase the learning curve of using a tool. Hence, the SSG with little to no additional set of tooling should be preferred at all costs if your intention is to produce content rather than being a hacker.
- **Availability of good-looking & modern themes** - If you choose to use a site generator over [Wordpress][Wordpress] or [Wix][Wix], having this aspect is a necessity. We live in the 21st century, I don't see why a site generator should provide a wide range of themes to choose from. Availability of themes is a must, doesn't if they're paid or free.
- **Ease of customizing the available themes** - What's the point of having a ready list of themes if you can't customize them to your needs. Considering how important branding & personalization is for success on anything online, not providing this option is a no-brainer. We'll see how easy is it to customize the themes of your choice. And extra kudos if the themes are open-sourced! :heart:

So, those were some of common aspects which all site generators should absolutely adhere to no matter how they generate the actual static content. I'll review each SSG based on the specific points mentioned above. And any other SSG lacking said aforementioned aspects at the least are worth giving a try in my opinion.

That said, lets dive into it & review the site generators, shall we?

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

Not everyone is a frontend developer & hence, Python is a quite popular among backend developers. So, in case you're wondering, wouldn't it be great to work with a SSG which is based on Python? Well then, you're lucky because I bring you [Pelican][Pelican]!

Since the software is based on Python, all you got to do is have [Python][Python] installed on your local machine. Then installing Pelican is just a `pip` command away with `pip install pelican`. While it supports files written in `.rst` format, you can even write your articles in Markdown now. All you got to do is install additional dependencies with the `pip install "pelican[markdown]"` command.

Unlike the previous generators, Pelican might appear bland to some people and they're right to feel so. The software is over a decade old at the time of writing this article. I assume some parts of it's API might even be very difficult to peruse through for the current developers.

Besides, Pelican's age doesn't show not just on it's landing page but on it's themes & configuration system as well. It just shows somehow & might be unappealing to many.

It's configuration system involves certain [global variables][Python Global Variables] inside a `pelicanconf.py` file. While some of those variables are set by Pelican & is a neccessity for Pelican to parse the `.md` and/or `.rst` files into HTML, theme authors can add their own variables too. In other words, Pelican can make use of an arbitrary range of settings! It might sound good right away but, for Pelican, it just didn't work out so well as you'll see soon.

Like most well-maintained Python projects, Pelican has an active team of developers keeping watch on it at all times. They've documented the software well enough but could be made better. This is a problem with most Python projects as their authors rely on automatic documentations off of the docstrings of the source code. Hence, you might often notice a lack of "human-touch" with certain Python project docs.

Regardless, the issue of documentations can still be handled to an extent, if not for a major issue the Pelican community faces. There're a ton of available themes for Pelican, great. But guess what? Most of the themes aren't maintained at all ([source][Pelican Themes Aren't Well Maintained])!

Now remember wherein Pelican theme authors can add their own arbitrary number of settings on top of the available ones? Well this is where it came back to bite the Pelican ecosystem.

Imagine you find a theme that you like. Install it for your blog, only for it to break with the latest Pelican installation. And there's no way for you to fix it because the theme author hadn't made a commit to the repo for 5 years now. Saddening, isn't it?

On top of it, as mentioned earlier, most of the themes look aged & bland. You could customize them or create one from scratch, but you'll also require knowledge of working with [Jinja 2][Jinja] templates. And working with Jinja templates does have a slight learning curve to it. So, good luck working with it when your time could be better spent blogging instead.

So, at the end of day when/why should you use Pelican? You're a Python backend developer with experience working on Jinja templates. And in addition to that, you don't care about SEO & other aesthetic values of your site. Then Pelican is the right option for you.

But, what if you care of efficiency & proper time management? Then there's Hugo for you. The next section details a review about Hugo as an SSG.

## Hugo: The Fastest Static Site Generator Ever Created

Hugo, the second-most popular site generator, ahead off of Gatsby only by a fraction of _stars_ in terms of popularity ([source][Jamstack list]). It's also one of the few non-JS software (or framework) in a domain filled by JavaScript framework. And most of it's popularity arose due to the fact how incredibly fast Hugo is at generating the static content, plus its availability of pretty, modern & SEO-friendly themes.

Since, it was built using [Go][Golang], all you need to get started with using Hugo is download it's binary. Adding the binary to your `PATH` enables you to invoke the binary from anywhere in the Terminal! You can find the most detailed installation instructions I've ever seen in any documentation at the "[Getting Started][Hugo Getting Started]" section.

And if it's not obvious already, I can't appreciate the Hugo dev's effort in making their docs as inclusive as possible! There's just too much details & they left not corners untouched while articulating the docs. My fellow Python devs, take some lessons from the Hugo devs on how-to write good documentations. :winking_face_with_tongue:

Besides, being able to invoke a single binary file, installing Hugo themes is also a piece of cake. All you got to do clone your preferred theme(s) into the `./theme/` directory. Ensure your Hugo knows which theme to use by updating the `config.yml` files & you're set with a theme. Also, trust me on it but, you're going to spend a day or two perusing through [the available list of themes][Hugo Themes]! Not only are each of them pretty & modern, most of them are well maintained & are SEO-friendly.

On that note, if you're wondering how easy is it to customise the themes? I would say, they're not difficult & besides, the official Hugo docs got your back in case you get stuck somewhere. :wink:

All you've before going the road of customizing (or even building your own theme) is Hugo uses [Go's powerful templating][Go Template] language. Unlike Liquid and/or Jinja2, Go templates are extremely intuitive. You can use your existing frontend toolkit, couple it with Go templates to build websites that won't look like static sites at all.

So, if you ask me? I would say Hugo would be your best bet. And this is coming from a Python developer with no experience working with Golang and/or JavaScript! With Hugo, I can reliably focus on producing more content rather than develop frontend stuffs.

## Verdict

Final thoughts on choosing tool for individual needs? Oh well, was it not hard for me thoroughly review each of those tools & decide which would suit which kind of users. But anyway let's end this rather lenghty piece of article with a brief infographic showing which site generator might be fit for you.

![Choosing the Right Static Site Generator Infographic][Infographic]

With everything said & done, do let me know if you enjoy reading these content. Find me on Twitter: [@Jarmosan][My Twitter] and/or [subscribe to my newsletter][My Newsletter] to get personalized content delivered to your inbox.

<!-- Reference Links -->
<!-- * Assets -->
<!-- [Infographic]: https://res.cloudinary.com/jarmos/image/upload/v1613158461/static-site-generator-review-infographic_qwrw0z.jpg -->
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
