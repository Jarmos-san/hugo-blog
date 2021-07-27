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

Ever since I started my development journey, I've hoped from one text editor to another. From Atom to Sublime Text, then to VSCode (which served my needs the longest). I even gave Vim a short try (and more on it later) & now finally to Neovim. A major reason why I've hopped from one distro to another is the need for customizability. While all the aforementioned Editors are customizable, they compromize on resource requirements & speed. Hence, Neo(vim) came to the rescue when I needed them the most.

Also if you've been following me around for a while now, you would know I develop code in a "Windows shop". And that itself brings in additional concerns like lack of proper terminal software support on Windows (but that's changing rapidly as of when this article was written). For example, unlike Unix distros, Windows doesn't come prepackaged with a terminal emulator. Nor does it have native Vim support like it's Unix counterparts.

You need to download the Vim binaries separately & either use it from a Terminal emulator like [Windows Terminal](https://github.com/microsoft/terminal) or the GUI "GVim" version. The later of which is available only on Windows machines (the irony :disappointed_face:). Also, not to forget how buggy Vim is on Windows.

But thanfully, Neovim v0.5.0 just dropped by a few days before this article was published. And I wanted to share what an wonderful experience it is to use Neovim instead of anything else on Windows. With that said, let's dive in & check out how different Neovim is from Vim.

## What the Heck is Neo(Vim) & the Hype Around it

As of writing this article Vim will be 29 years old! So, around three decades ago, [Bram Moolenaar](https://en.wikipedia.org/wiki/Bram_Moolenaar) created Vim (which stands for ViImproved) as a clone of the OG "Vi". It also comes prepackaged with a wide variety of Unix distros & is supposed to be used within a terminal environment.

And over the years it's source code has increased in size as well as complexity. Also, since it's written in C (and Vimscript), it's hard to configure, maintain & expand on with additional features. It's also **VERY** buggy on Windows.

Because of such constraints (among many others) a couple of Vim contributors forked it's source code recreated it from scratch. They named it Neovim & wrote it in [Lua][Lua] enabling the user to configure and/or extend the editor's capabilities much more easily.

So, if you're confused between choosing either Vim or Neovim as your preferred Text Editor, know this; __Neovim is a fork of Vim__. Neovim was rebuilt from scratch keeping in mind extensibility & ease of configuration. So, if you're looking for a Text Editor to replace VSCode (or anything else) there's only a very handful & specific reasons not to choose Neovim.

Also, in addition to all Vim features that Neovim comes prepackaged with, it's embedded Lua scripting environment is by the far it's most captivating feature. And how would you get started with this feature? The next section of the article will briefly go through on how you can do it as well.

## Configuring Neovim With `init.lua`

With Neovim v0.5's release, it also came packaged with one of it's most captivating feature; the embedded Lua environment! What does it mean for a regular Vim user? It means you're no longer constrained within the weird limits of Vimscript. If you're anything like me, you would know coding in Vimscript isn't the most fun thing to do. And the introduction of the Lua environment is a godsend for all peeps like us out there!

So, without further adieu, let's check out how you can get started configuring Neovim using Lua as well. But first of a couple of prerequisite knowledge:

1. You can embed Lua code within your existing `init.vim` file. So, rather than migrating your configurations from Vimscript to Lua right away, itmight be better to take things slow instead.

2. Neovim now includes a "_stdlib_" (or rather the Neovim API) along with the Lua standard library. The Neovim API exposes various functions among other stuff like this: `vim.api.nvim_set_keymap()` & so on.

3. Lua "modules" stored within a directory named `lua` under the Neovim configuration directory are imported automatically. So, if there's a `keymaps.lua` under `./nvim/lua/`, you can simply import with it into your `init.lua` (or `init.vim` if you prefer) using the `require("keymaps")` statement. It's as simple as that!

4. And the best part of it all? Whatever `runtime` directories you might've had earlier will still be sourced. So, directories like `ftplugin`, `colors` & so on will still work as they used to.

## How Embedding Lua Has Changed "Vim" & it's Future

Those of you who've been involved with Vim for time immemorial would know how antiquated everything related to Vim is. Right from some of the default configuration settings to Vimscript itself reeks of old age & dev practices of the 90s. And the most significant of these old practices ought to be Vimscript itself. More on it later & you'll soon see how it was one of the major reason to embed Lua within Neovim.

To start with Vimscript is very cryptic. It's syntax sometimes doesn't make sense at all. And not to forget the huge learning curve for master Vimscript. On top of that Vimscript is noticeably slow, how slow you might wonder?

To give you some idea of how Vimscript is; before migrating my `init.vim` file to `init.lua`, Neovim took ~534ms during initial load times. It was reduced to ~200ms after the migration! Yeah that's how slow Vimscript can be if with a very minimalist setup.

I could squeeze out a bit more performance juice out of it using Lua code but I'm not sure if the added effort is worth it.

Besides, the straight-up performance improvements, Lua also bring with it a pleasant development environment. And with the Neovim developer's efforts the editor is now even more easier to extend & configure.

Do you need to map some keys? Well, simply use the [Neovim API][Neovim API] something like this: `vim.api.nvim_set_keymap()` function. And the best part of it all? The Neovim API is injected into the script during runtime which means you don't have to specifically import the library. Hence, keeping the `init.lua` file or any other runtime files clean & easier to maintain.

That said, how did forking Vim to create Neovim affect the former?

For one, it definitely made Bram Moolenaar (the OG developer of Vim) obligated to be more open to modern changes. For example, it took Bram over 2 decades to speed up Vimscript. So, if you're still loyal to OG Vim, you'll have to wait till Vim 9.x hits the shelf for improved load times. And if you're impatient like me, there's no reason to migrate to Neovim instead.

But now the question is, should you abandon Vimscript to configure Neovim? The next section will give a brief overview of what to expect.

## Should You Embrace Lua & Abandon Vimscript

Before I answer that question, let me reiterate on what the Neovim devs themselves have to say about it. They've "_no plans to deprecate Vimscript_", like ever. You can take a look at the non-goals section of their [charter][Neovim Charter].

So, no you don't have to worry about migrating your Vimscript runtime files to Lua code anytime soon. While you can embed Lua code right within Vimscript files, the traditional runtime directories & files will still work. So, you can

## Final Words & Resources for Your Journey into Neovim-land


<!-- References --->
[Neovim Charter]: http://neovim.io/charter/
[Neovim API]: https://neovim.io/doc/user/api.html
[Lua]: lua.org
[Bram Moolenaar]: https://en.wikipedia.org.wiki/Bram_Moolenaar
[Windows Terminal]: https://github.com/microsoft/terminal
[Vim]: https://www.vim.org
[Neovim]: https://neovim.io
