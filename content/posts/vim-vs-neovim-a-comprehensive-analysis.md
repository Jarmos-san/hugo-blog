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

<!-- References --->
[Lua]: lua.org
[Bram Moolenaar]: https://en.wikipedia.org.wiki/Bram_Moolenaar
[Windows Terminal]: https://github.com/microsoft/terminal
[Vim]: https://www.vim.org
[Neovim]: https://neovim.io

