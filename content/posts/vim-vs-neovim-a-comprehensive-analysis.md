---
title: "Vim vs Neovim: A Comprehensive Analysis"
date: 2021-07-15T13:10:41+05:30
slug: "vim-vs-neovim-a-comprehensive-analysis"
category: "Development Environments"
summary: My experience & learnings after using Neovim (that too on Windows!) for a while for all my development needs, summed up in one single blog post.
description: My experience & learnings after using Neovim (that too on Windows!) for a while for all my development needs, summed up in one single blog post.
cover:
  image:
  alt:
  caption:
  relative: false
showtoc: true
draft: true
---

If you ever heard of [Vim][Vim] before, you would know all about it's forks that have popped up in recent years! There’s [Neovim][Neovim] (the most popular fork), [LunarVim][LunarVim] (one of the most promising fork) & countless others. And as is obvious, choosing the one right one for yourself can be a difficult task (been there & done that).

So to help you decide, this article will shed light on some of the differences between Vim & Neovim. To be more specific, we’ll look into every day use cases while comparing the two. Analysing everyday use cases is more relevant while comparing consumer products anyway.

But before we dive into the real deal of the article, as usual a little bit of a history lesson first.

Vim itself started out as an improved clone of the now antiquated [Vi][Vi] by [Bram Moolenaar][Bram Moolenaar] way back in the early 90s. Moolenaar himself overlooked the development & course of actions for Vim.

Over the decades, the Vim source code is starting to become archaic & hard to maintain. It's bloated, some of the code is unoptimized & it's current set of features hasn't aged well.

But, Neovim was rebuilt from scratch! Redundant & decades old code  was weeded out . And all the while the maintainers tried  to provide the same power to the users as Vim did. Although, it did come pre-packaged with “_optional steroids_” to consume. More on it in the rest of the article!

With that said, let’s dive deeper & check out some of the differences between the two editors. Although take due note, this article isn’t intended as a jibe at Vim or it’s loyal users. Rather we’ll try to analyse the differing features of the two editors & see how useful they are on a day-to-day basis.

## Why is Neovim More Popular Than Vim

As mentioned earlier Vim is pretty old, as such it’s code base is archaic & difficult to maintain. And this was a primary reason for the current dev team for Neovim to fork Vim & set off on a journey of their own.

Unlike some of the rumours floating around Neovim wasn’t forked because “Bram is a dictator” & what not. Neither was Neovim created to give more power to the community. But the latter is definitely an unintentional outcome of the fork in a good way.

Since, Neovim was rebuilt from the ground-up, it opened up doors to;

1. Adding useful features like [Language-Server Protocol][LSP] (LSP), an embedded [Lua 5.1][Lua] (and LuaJIT) runtime & so on, more easily.
2. Cleaner & optimized source code for easier maintainability & reduced load times.
3. Straight-up better plugin development environment.
4. Extending core Neovim capabilities through improved plugins if necessary.

And those were only a few good outcomes of forking the Vim source code. But in reality, the list is never-ending & chances are, as Neovim matures over time, there’ll be another reason to extend the list.

Some other equally prominent features include:

1. The underlying Neovim API for plugin devs to use for building pretty much anything.
2. The optional embedded Lua 5.1 environment is also a reason why Neovim is so loved by the community. If a user wishes to do, Neovim can be configured with Lua rather than VimScript.
3. An inbuilt standard library which includes functions like `CheckHealth` and/or the global `vim` Object. These are used to check if a plugin has been set up correctly.  Or to configure Vim settings.
4. Comes pre-packaged with sensible default settings making the Vim experience more pleasant.

And if it’s not obvious already, Neovim is already miles ahead when it comes to useful features. For example, choosing to configure Neovim with either VimScript or Lua. Or heck if you desire, you can even use both side-by-side, the choice is all yours!

With Vim, you would be stuck with the dreaded VimScript! While LSP capabilities are supported through plugins, the experience isn't as smooth & out-of-the-box like it's cousin.

With that said, let’s take a more detailed approach to some of the most used features mentioned above. And along the way, we’ll also see Vim’s take on those features and/or if there are any plans to add them in the future.

## Neovim is Noticeably FASTER Than Vim

As mentioned earlier, one of the major reasons to fork Vim was it’s archaic source code. Since Vim has been in existence for close to three decades it's source code is pretty bloated by now. Since it was hard to maintain & it was much easier to simply rebuild from scratch, the devs did what was necessary.

Owing to that decision, the source code was cleaned & optimized. This is obvious if you notice how faster Neovim is than its predecessor.

Rebuilding Neovim also opened up many doors the devs could take. One & the most killer feature of the editor is the embedded Lua 5.1 (and LuaJIT) environment.

The devs also took other performance optimization paths. One of them included making Neovim run in an [Event Loop][Event Loop]. So, you can finally bid goodbye to plugins that would hang earlier!

Besides that, the devs have also ensured backwards compatibility with VimScript. So, if you’re a long-term Vim user who wants to try out Neovim, don’t fret, you'll be fine. You can configure Neovim to read your older `.vimrc` just fine albeit with some trivial hacks here & there.

But what if you’re committed to using Neovim & are ready to take the dive? I would suggest migrating your current VimScript configurations to Lua code instead. You’ll notice an increased performance boost.

To give an idea of what sorts of performance boost I’m talking about here, I'll share my experience. My Neovim load times decreased from 500+ ms to 237 ms. That’s a roughly ~50% improvement by simply migrating from VimScript to Lua!

One can only imagine how much faster it can perform if the configuration loading were optimized properly.

On the flip side though, configuring through Lua is an optional feature. More on it in the next section of the article.

## Option to Ditch VimScript & Embrace Lua

[One of the goals][About Neovim] of the Neovim team is to “_develop first-class Lua/LuaJIT scripting alternative to VimL_”. Staying true to their words, the devs haven’t enforced ditching VimScript in favour of Lua. And I doubt any of us would live to see that happen in our lifetime!

So, if you want to continue using your previous Vim configs, you needn’t fret at all. But what if you definitely need Lua code, for example say configuring the builtin LSP?

If you’re in a similar situation, Vim `heredoc` will come to your rescue. You can embed Lua code within VimScript with a syntax which looks something like this;

```vimscript
Lua << EOF
# Some Lua code here
EOF
```

And you’re good to go out on your day without worrying it would break something from your previous Vim configs. Vim would still know how to parse those code & make sense of it.

Although, a bit of a personal opinion here, try not to use VimScript if you can. Coding in Lua is a much pleasant experience. And even if you had to learn it, the language has many real-life applications outside of a Vim environment. So, it’s not like you would be wasting your time learning a redundant programming language. If you do decide to start configuring Neovim with Lua, do give this “[Guide to Using Neovim with Lua][Neovim Lua Guide]” a thorough read.

That said, Neovim’s embedded Lua environment’s usefulness takes proper shape through it’s inbuilt standard library & API. If you’re either a plugin developer or a regular Vim user, the standard library can be useful in many ways. It packages many useful functions & commands to use for your day-to-day development needs.

So, in the next section, we'll take a more detailed look into it.

## The Inbuilt Standard Library & the API is 💖



<!-- References --->
[Neovim Lua Guide]: https://github.com/nanotee/nvim-lua-guide
[About Neovim]: http://neovim.io/charter/
[Event Loop]: https://en.wikipedia.org/wiki/Event_loop
[LSP]: https://microsoft.github.io/language-server-protocol/
[Neovim API]: https://neovim.io/doc/user/api.html
[Lua]: lua.org
[Bram Moolenaar]: https://moolenaar.net/
[Windows Terminal]: https://github.com/microsoft/terminal
[Vim]: https://www.vim.org
[Neovim]: https://neovim.io
[LunarVim]: https://github.com/ChristianChiarulli/LunarVim
[Vi]: https://en.wikipedia.org/wiki/Vi
