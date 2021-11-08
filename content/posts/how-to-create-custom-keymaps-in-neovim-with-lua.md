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

But before we learn about configuring Neovim keybindings using Lua code, let's
quickly brief over what the optional runtime has to offer & it's benefits.

Now if have been using Neovim for a while now, you would already be aware of
it's builtin _standard library_ & the
[Neovim API](https://neovim.io/doc/user/api.html). The Lua runtime augments the
API & the builtin _standard library's_ behaviour. On top of that, the Lua
runtime also brings along it's own set of _builtins_ which can be pretty handy
at times!

As you can see, if Vim gave you
[Thanos](https://marvel.fandom.com/wiki/Thanos)-like superpowers, then Neovim's
Lua runtime, the standard lib & the API would be the
[Infinity Stones](https://marvel.fandom.com/wiki/Infinity_Stones).

With our little introduction to the optional Lua runtime done & dusted, lets
check out the how's, the what's of configuring Neovim keybindings with Lua.

## How to Write Lua Function for the Neovim Key Bindings

When it comes to configuring Neovim keybindings, there's a major caveat & it
makes quite a difference from a user-experience perspective. Unlike Vim, Neovim
doesn't provide a rather straight-forward solution to customise keybindings.

What Neovim does differently is it provides an API call to a function named
`nvim_set_keymap()` instead. Neovim users are expected to wrap this function
when customizing their preferred keybindings. That way not only will your
configurations adhere to the
[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) &
[SOLID](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
principles, but the config code base looks clean & organized as well.

With that said, let's compare what a typical Vim & a Neovim user would configure
their custom keybindings. To keep things simple & understandable, we'll define a
simple keybinding for toggling highlighting features on/off while using search.

**Vim**:

```VimL
nnoremap <silent> ,<Space> :nohlsearch<CR>
```

**Neovim**:

```lua
-- Functional wrapper for mapping custom keybindings
function map(mode, lhs, rhs, opts)
    local options = { noremap = true }
    if opts then
        options = vim.tbl_extend("force", options, opts)
    end
    vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

map("n", ",<Space>", ":nohlsearch<CR>", { silent = true })
```

As you can see while at first glance, the Lua code might appear too verbose but
it enables you with more power to customize the keybindings. As in, while Neovim
provides a `nvim_set_keymap` function through it's API, you pretty much free to
do anything you want to achieve by wrapping it.

Arguably the same might be possible using Vimscript as well but it's hard to
maintain & as far as I know no one enjoys writing Vimscript functions.

With that said, in the next section let's take a deeper dive into understanding
Lua functions to use for configuring Neovim.

## Using the Lua Functions Across the Neovim Runtime Files

In the previous section we defined a single function which wraps the
`nvim_set_keymap()` function in Neovim. Now what if we had to reuse this
function elsewhere? How do we import & use it where necessary?

In those situations we'll be making using of
[Lua Modules](https://www.lua.org/manual/5.1/manual.html#5.3). So create a
`utils.lua` under the `lua` directory in your runtimepath. And then add the
following content to that file:

```lua
-- Our lua/utils.lua file

local M = {}

function M.map(mode, lhs, rhs, opts)
    local options = { noremap = true }
    if opts then
        options = vim.tbl_extend("force", options, opts)
    end
    vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

return M
```

Once the module is defined Neovim will add it to it's runtimepath automatically
& make it available globally for other usage elsewhere. For example, now it's
possible to import the `map()` function into your `init.lua` & use it without
bloating the Neovim config file.

Here's how you could do that:

```lua
-- Our example init.lua file

local map = require("utils").map

map("n", ",<Space>", ":nohlsearch<CR>", { silent = true })
-- Add other custom keybindings you need
```

Now that our configuration code is modularized, keeping track of unintended
consequences are much easier. Identifying & resolving bugs in the user-defined
configuration is also less stressful & easier to maintain because of it.

So, that was how you could define & customize your own Neovim keybindings using
Lua. If you had a tough time maintaining a huge `init.vim` file with hundreds of
lines of code, perhaps now is time to start migrating to Lua.

## Final Words & Things to Look Forward to

Defining & configuring custom keybindings needn't be a chore anymore as it used
to be the case if using Vimscript. With Lua, defining & heck even extended
standard Neovim keybindings to your heart's content is a possibility. And all of
it is as easy as defining a function & call it. So, in other words, defining
keybindings using Lua is pretty much like writing code in an actual programming
language & in a familiar environment.

But if you already have an `init.vim` file & you would like to migrate to Lua
code instead. Here are some resources you could make use of to learn more about
it:

1. [Vim or Neovim? Here's Why You Should Use the Latter](../vim-vs-neovim)
2. [A Guide to Using Lua in Neovim](https://github.com/nanotee/nvim-lua-guide)
3. [`h: lua`](https://neovim.io/doc/user/lua.html) for a comprehensive guide on
   how to use Lua within Neovim.

And to conclude this article, what do you think of using Lua rather than
VimScript for configuring Neovim? Let me know your thoughts & share how you've
configured your Neovim keybindings as well!
