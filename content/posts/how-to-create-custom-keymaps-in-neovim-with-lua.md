---
title: "How to Create Custom Keymaps in Neovim With Lua"
date: 2021-10-12T13:10:41+05:30
slug: "create-custom-keymaps-in-neovim-using-lua"
category: Neovim
summary:
  "Learn how to create custom key bindings in Neovim using the optional inbuilt
  Lua runtime"
description:
  "Learn how to create custom key bindings in Neovim using the optional inbuilt
  Lua runtime"
cover:
  image:
  alt:
  caption:
  relative: false
showtoc: true
draft: true
---

Neovim (or even Vim) is an excellent piece of software for increased
productivity. If you're a veteran Vim user, I'm sure you're pretty aware of Vim
keybindings. The software itself is known for it's openness towards customizing
user-defined key-bindings. As such, pretty much the sky is the real limit to
what you could possibly do with custom Vim key bindings.

But for a user to effectively custom their Vim keybindings, they would to
require an adequate knowledge of VimScript (or VimL) which is a language used
for customizing the Vim-experience. And to be honest here, VimL is not my most
favoured programming language. And I'm sure quite a lot of you out there will
agree with me on this fact as well.

VimL is cryptic, archaic & has pretty much no use-case outside of Vim.
Fortunately for people like you & me, `Neovim v0.5+` gave us a signficant update
to play around with. And that's the optional Lua runtime making it backwards
compatible with VimL as well!

So, in other words, you're free to gradually ditch VimL in favour of Lua to
create custom keybindings! Sounds optimistic, right? 😆 Hence, here I'm sharing
how I create custom Neovim keybindings using Lua (_and goodbye VimL, you served
me well_).

## Introducing the Optional Lua Runtime

Before I introduce how Neovim keybindings are configured using Lua, I feel you
should know a bit about the optional Lua runtime first. So, for some of you out
there who're yet to make a full transition to Lua, making sense of why Lua is an
optional runtime will help you make the gradual migrations over time.

So, `Neovim v0.5` was a much anticipated update & one which brought about quite
a few major featureful additions to the software. One of those features is the
Lua runtime & it's backwards compatiblity with VimL. Besides that, the Neovim
devs has also been packaging it with a handy "_standard library_" as well.

## How to Write Lua Function for the Neovim Key Bindings

## Using the Lua Functions Across the Neovim Runtime Files

## Why You Should Try to Use Lua Over VimScript
