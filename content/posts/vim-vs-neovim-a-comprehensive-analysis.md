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

And over the years it's source code has increased in size as well as complexity. Also, since it's written in C (and VimScript), it's hard to configure, maintain & expand on with additional features. It's also **VERY** buggy on Windows.

Because of such constraints (among many others) a couple of Vim contributors forked it's source code recreated it from scratch. They named it Neovim & wrote it in [Lua][Lua] enabling the user to configure and/or extend the editor's capabilities much more easily.

So, if you're confused between choosing either Vim or Neovim as your preferred Text Editor, know this; __Neovim is a fork of Vim__. Neovim was rebuilt from scratch keeping in mind extensibility & ease of configuration. So, if you're looking for a Text Editor to replace VSCode (or anything else) there's only a very handful & specific reasons not to choose Neovim.

Also, in addition to all Vim features that Neovim comes prepackaged with, it's embedded Lua scripting environment is by the far it's most captivating feature. And how would you get started with this feature? The next section of the article will briefly go through on how you can do it as well.

## Configuring Neovim With `init.lua`

With Neovim v0.5's release, it also came packaged with one of it's most captivating feature; the embedded Lua environment! What does it mean for a regular Vim user? It means you're no longer constrained within the weird limits of VimScript. If you're anything like me, you would know coding in VimScript isn't the most fun thing to do. And the introduction of the Lua environment is a godsend for all peeps like us out there!

So, without further adieu, let's check out how you can get started configuring Neovim using Lua as well. But first of a couple of prerequisite knowledge:

1. You can embed Lua code within your existing `init.vim` file. So, rather than migrating your configurations from VimScript to Lua right away, itmight be better to take things slow instead.

2. Neovim now includes a "_stdlib_" (or rather the Neovim API) along with the Lua standard library. The Neovim API exposes various functions among other stuff like this: `vim.api.nvim_set_keymap()` & so on.

3. Lua "modules" stored within a directory named `lua` under the Neovim configuration directory are imported automatically. So, if there's a `keymaps.lua` under `./nvim/lua/`, you can simply import with it into your `init.lua` (or `init.vim` if you prefer) using the `require("keymaps")` statement. It's as simple as that!

4. And the best part of it all? Whatever `runtime` directories you might've had earlier will still be sourced. So, directories like `ftplugin`, `colors` & so on will still work as they used to.

## How Embedding Lua Has Changed "Vim" & it's Future


## Should You Embrace Lua & Abandon VimScript


## Final Words & Resources for Your Journey into Neovim-land


<!-- References --->
[Lua]: lua.org
[Bram Moolenaar]: https://en.wikipedia.org.wiki/Bram_Moolenaar
[Windows Terminal]: https://github.com/microsoft/terminal
[Vim]: https://www.vim.org
[Neovim]: https://neovim.io

