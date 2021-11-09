---
title: "How to Create Custom Keymaps in Neovim With Lua"
date: 2021-10-12T13:10:41+05:30
slug: "create-custom-keymaps-in-neovim-using-lua"
category: Neovim
summary:
  "Learn to create custom key bindings in Neovim using the optional inbuilt Lua
  runtime. And ditch the archaic & cryptic Vimscript in Lua's favour!"
description:
  "Learn to create custom key bindings in Neovim using the optional inbuilt Lua
  runtime. And ditch the archaic & cryptic Vimscript in Lua's favour!"
cover:
  image: "https://res.cloudinary.com/jarmos/image/upload/v1636405448/covers/ditching_vimscript_for_lua_hgqdfz.png"
  alt: "Ditching Vimscript in favour of Lua for easier Neovim configurations"
  caption: "I migrated my Neovim configurations & couldn't be more happier!"
  relative: false
showtoc: true
draft: false
---

Neovim (or even Vim) is an excellent piece of software for any developers out
there. If you're an experienced Vim user, you should be aware of custom Vim
keybindings. For the uninitiated, Vim's openness towards creating custom
keybindings has pretty much no competition out there. As such, only your
imagination is the limit to what you could possibly create using custom
keybindings.

Vim users are also required to have working knowledge of Vimscript (_which is a
scripting language built for Vim configuration_). It's not the most elegant
language & neither has it any use outside of Vim. Also for many of you, the time
investment & efforts required to pickup a redundant programming language
mightn't be productive. Fortunately, `Neovim v0.5+` gave the community a
signficant update to play around with, the inbuilt Lua runtime.

The optional Lua runtime introduced with `Neovim v0.5` was a breath of fresh
air. It was also backwards compatible meaning you could still try out the
optional runtime right from within Vimscript. We'll not discuss how to write Lua
code within Vimscript since it's beyond the scope of this article. But feel free
to refer to this amazing
[Neovim-Lua Guide](https://github.com/nanotee/nvim-lua-guide) on GitHub for a
quick reference.

If that piqued your interests & you would like continue learning about how
creating custom keybinds in Neovim is a much pleasant experience, then read
ahead. The rest of the article starts with a brief intro to the optional Lua
runtime, followed by creating a Lua function for mapping the custom keybinds.
And towards the end of it all, we'll suggest further resources you might want to
take a look at to learn about Neovim's Lua runtime better.

## Introducing the Optional Lua Runtime

Before we proceed further into the article, let's briefly introduce the Lua
runtime in Neovim. Having some idea of it will help better understand the how's
& what's possible to create.

One particular feature that makes Neovim stand out is it's
[builtin API](https://neovim.io/doc/user/api.html). In addition to that, the Lua
runtime has it's own _standard lib_! So, if you desire, you can let your
imaginations go wild & hack Neovim to your heart's content.

Like any other config files used to hack Neovim/Vim, the Lua code also needs to
be placed in the `runtimepath` (see `:h rtp` for more info). These config files
(with a `.lua` extensions) are placed inside a directory aptly named `lua`. And
Neovim will source everything inside that directory when invoked.

Do note, the location to the Neovim runtimepath varies depending on the choice
of your OS. So, for Linux users out there, check if your OS follows the
[XDG Base Directory](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
specification, then the Lua files should be usually available at:
`$HOME/.config/nvim/lua`. And my fellow Windows users out there, you should
check for the Lua files at `%LOCALAPPDATA%\nvim\lua`.

For more info on where to place the config files, check out the
["_Where to put Lua files_"](https://github.com/nanotee/nvim-lua-guide#where-to-put-lua-files)
section of the Neovim-Lua Guide on GitHub.

With that said & our little introduction to the optional Lua runtime done &
dusted, lets check out the how's, the what's of configuring Neovim keybindings
with Lua. In the next few sections we'll taking a look at, writing an example
Lua function followed by an actual functional wrapper in Lua. This functional
wrapper will be used to create our custom keybindings where & whenever
necessary.

## How to Write Lua Function for the Neovim Key Bindings

Back in the day when Neovim wasn't a thing, Vim provided the `remap` commands
(_and the `noremap` for non-recursive remaps_) for customizing & remapping
keybindings. As such it was a common scene to see `nnoremap` commands scattered
all over one's `.vimrc` file. Here's one such
[example `.vimrc`](https://github.com/jessfraz/.vim/blob/master/vimrc) file I
picked up from the Internet. The file is huge (~1200 lines of code!), is
unweidly & a totaly nightmare to maintain.

A little code snippet I picked up from the `.vimrc` file above.

```vimscript
" Example .vimrc file with hundreds of lines of code
...
nnoremap <silent> <leader> :<c-u>WhichKey ','<CR>
nnoremap <leader>? :WhichKey ','<CR>
nnoremap <leader>a :cclose<CR>
nnoremap <leader><space> :nohlsearch<CR>
...
```

Fortunately for us, Neovim provides a helper function through it's builtin API.
Aptly named `nvim_set_keymap()`, the users are expected to use this function
directly or by wrapping it in Lua code. The later method is recommended since
that way it's possible to adhere to standard coding practices. Using Lua code in
tandem with the Neovim API also helps in modularising the configurations. Thus
making maintenance much easier & keep your sanity intact.

Using wrapper functions also ensures the configurations are
["**DRY**"](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) &
["**SOLID**"](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design).
Adhering to such common development standard practices means the configurations
looks clean & organized as well.

So what does a typical Neovim configuration look like when used with Lua?
Following are some such examples:

**Vim**:

```vimscript
" Code borrowed from the example .vimrc above
...
nnoremap <silent> ,<Space> :nohlsearch<CR>
nnoremap <silent> <leader> :<c-u>WhichKey ','<CR>
nnoremap <leader>? :WhichKey ','<CR>
nnoremap <leader>a :cclose<CR>
...
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
map("n", "<Leader>", ":<C-u>WhichKey ','<CR>" { silent = true })
map("n", "<Leader>?", ":WhichKey ','<CR>")
map("n", "<Leader>a", ":cclose<CR>")
```

At first glance, the Lua code might appear too verbose but it's a good thing as
you'll see soon.

In the Lua code snippet we shared aboved, we defined a function called `map()`.
It accepts four parameters namely:

- `mode` (as in Vim modes like `Normal`/`Insert` mode)
- `lhs` (the custom keybinds you need)
- `rhs` (the commands or existing keybinds to customise)
- `opts` (additional options like `<silent>`/`<noremap>`, see `:h map-arguments`
  for more info on it)

By default, the `opts` parameter of the `map()` function is assigned to a table
`{ noremap = true }`. In doing so, nested & recusive use of mappings are allowed
(refer to `:h map-commands` for more info on it). You can expand the `opts`
table further with additional `map-arguments` as you require. And at the core of
the wrapper is the `vim.api.nvim_set_keymap()` function which accepts the list
of parameters mentioned above.

This function can then be reused wherever you need them. As you'll see in the
next we can modularise our Neovim configurations even further!

## Using the Lua Functions Across the Neovim Runtime Files

The wrapper function we used in the section above does help in customising
default Vim remappings. But defining the wrapper function & then using it right
within our `init.lua` file doesn't adhere to the DRY and/or SOLID principles at
all. To make the configs more compliant with standard dev practices, we'll use
[Lua Modules](https://www.lua.org/manual/5.1/manual.html#5.3). Using Lua Modules
ensures there's clear separation of logic in our configurations.

And if you need a refresher on how to create Lua Modules for Neovim, refer to
the ["_Modules_"](https://github.com/nanotee/nvim-lua-guide#modules) section of
the Neovim-Lua Guide on GitHub.

That said, create a `utils.lua` under the `lua` directory in your runtimepath.
This file will be our Lua Module for the `map()` function. Following is example
code snippet on how to do it:

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

Neovim sources & loads any Lua files located under the `lua` directory in the
runtimepath. Hence, now it's possible to simply import the wrapper into your
`init.lua` file & use it for creating your remaps. Thereby you can now keep the
file clean, maintainable & fast to load.

Here's how you could rewrite the `init.lua` file by importing the `map()`
function from the `utils` module;

```lua
-- Our example init.lua file

-- Import & assign the map() function from the utils module
local map = require("utils").map

map("n", ",<Space>", ":nohlsearch<CR>", { silent = true })
map("n", "<Leader>", ":<C-u>WhichKey ','<CR>" { silent = true })
map("n", "<Leader>?", ":WhichKey ','<CR>")
map("n", "<Leader>a", ":cclose<CR>")
```

Now that the code is properly modularised, you can maintain it more easily &
without breaking something in the process. Further, if you wish extending our
rudimentary `map()` function is as simple making your necessary changes to the
`utils` module!

That said, chances are if you've been using Neovim for a while now, you're yet
to migrate your configs to Lua code. And you'll be glad to hear that the Neovim
devs went through great lengths to maintain backwards compatibility. If you're
uncomfortable to make the necessary changes to existing configs, it's possible
to use Lua code right within Vimscript as well. Refer to `:h heredocs` for more
info on the topic.

To help you figure your way around while migrating the existing configs, the
next section will suggest some useful references you could take a look at.

## Final Words & Things to Look Forward to

The optional Lua runtime within Neovim is a godsend & one such feature which
makes Neovim particularly stand out apart from Vim. But since the features &
Neovim itself is comparatively new, resources around these features are hard to
come by. As such following are some resources you might want to take a look at
if configuring Neovim with Lua piques your interests.

1. [A Guide to Using Lua in Neovim](https://github.com/nanotee/nvim-lua-guide)
2. [`h: lua`](https://neovim.io/doc/user/lua.html) for a comprehensive guide on
   how to use Lua within Neovim.
3. And a bit of a shameless plug, you could use my blog as a source of reference
   as well. I've written one such articles introducing the benefits of using Lua
   for Neovim in
   [Vim or Neovim? Here's Why You Should Use the Latter](../vim-vs-neovim)

Did I miss out any other useful resources? Let me know if I did!

And to conclude this article, what do you think of using Lua to configure
Neovim? Are you current configuration in Vimscript or Lua? And have you noticed
any difference while using either? Drop me a DM on
[Twitter @Jarmosan](https://twitter.com/Jarmosan) or an email whichever you
prefer.
