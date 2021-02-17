---
title: "Customizing the New Windows Terminal: A Minimalist Approach"
date: 2020-12-25
category: Programming
slug: customizing-windows-terminal-a-minimalist-approach
summary: Who needs Linux when you got a fully customized Windows Terminal!
description: Who needs Linux when you got a fully customized Windows Terminal!
cover:
  image: "https://i.ibb.co/V3y7Cb4/DRj-DFi-EQZO.gif"
  alt: "A .gif image of my customized Windows Terminal"
  caption: "A GIF of my customized Windows Terminal"
  relative: false
showtoc: true
---

Heard of the new Windows Terminal (WT), Microsoft has been actively working on recently? You might’ve if you’ve been following my updates on Twitter. I was advocating Microsoft’s effort to make Windows a more developer-friendly platform for quite a while now. And ever since I moved from Ubuntu to Windows for my coding needs, I’ve come to realise how things have changed on Windows-land for the better.

## What is This New Windows Terminal?

With that said, WT is a console developed & distributed by Microsoft. It supports a wide variety of shells, the full list of which I’m not aware of. But I’m assured it supports most of the popular ones. Hence, by popularity, Bash/zsh is supported through Windows Subsystem for Linux (WSL) & PowerShell 5.1 which ships pre-packaged with Windows 10.

On that note, I’ve been using PowerShell 5.1 mainly because it’s there by default & is a much easier scripting language over Bash. So, without further ado, let’s dive into how I’ve made some very minimalist customization to WT.

## Why Maintain a Minimalist Look?

Windows Terminal is **VERY** customizable, as you’ll see soon enough. You can set a background image (or a GIF) of your choice. You can add multiple panes to a tab with each running a different shell instance, the possibilities are infinite. But customizing to such an extent comes with a caveat, spending way more time on customizing the Terminal to look “perfect” is time-consuming. The time which I could spend on projects & work instead.

Besides, there’s also the problem of cognitive overload I’ve trouble dealing with. Thus, I follow the principles of minimalism wherever possible. Put simply, having just enough & specific information for a task is all I need. If a need arises, customizing the Terminal to fit those needs is still an open option.

Anyway, enough of my justifications & let’s cut the chase. This is the configuration I use, feel free to copy & use them.

</br>
<script src="https://gist.github.com/Jarmos-san/6464fc65ac3c81f94f855fc76190c911.js"></script>

Anyway, enough of my justifications & let’s cut the chase. This is the configuration I use, feel free to copy & use them.

## My Customization & Description of the Config File

The Windows Terminal configurations are divided into 4 distinct sections each customizing a specific aspect of the software.

**Global (or Default) Settings**:

The config file begins with the Global (or “*default*”) settings. Followed by the Profile, Colour Schemes & lastly, the key Bindings (or “*Actions*”).

Right at the start of the file, the Global settings apply customization to the whole software, as in how Windows Terminal behaves. In context to that, my configuration starts Windows Terminal with PowerShell as the default profile (more on profiles a bit later), indicated with the `defaultProfile` settings.

Right below it & till line 12, I’ve set Windows Terminal to not copy a body of text when selected & not even the formatting. Azure Shell & WSL profiles are also disabled since I’ve yet to find any relevant use for them. And at last, to ensure my eyes don’t burn & are protected, a dark theme, tab width & startup window maximized is enabled.

Those were the Global settings which apply to the whole of Windows Terminal as a software. They don’t do much but  help with the startup time, my eyes & productivity.

But here’s where things get visually interesting, customizing individual Profiles.

**Profiles**:

Profiles are  Windows Terminal’s way of creating & manipulating shells & other terminal emulators. In other words, you can have a PowerShell session running side-by-side on a tab with Bash (running on an Ubuntu-WSL).
If it isn’t obvious from the GIF on the featured image already, I’ve set up four profiles – PowerShell, Python Repl, Git Bash & Neovim. But the configuration lists 6, how & what’s going on?

Be patient, soon enough you’ll figure that out as well.

The Profile section accepts some default settings as well. And they’ll be applied to each of the profiles stated inside the array. The default settings specify, the starting directory when the profile is initiated, the font size, bold fonts (so you don’t have to squint to read the texts), padding (makes the text look nicer & works like CSS padding), the shape & colour of the cursor (to add some oomph…). The acrylic background is enabled, making the Terminal look transparent. And not to forget, at last, the name of the colour scheme.

These default settings ensure uniformity across whichever shell emulator is in use. These settings also ensure good minimalist aesthetics without being too distracting and/or hard on the eyes.

Line 25-64 lists the profiles, the crest of Windows Terminal we’ve been discussing till now. There’s a lot more you could do here, so I suggest checking out the [official docs](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-settings) first. You can build upon my configurations & yes, don’t forget to share your creations with me (tweet them to me 😉).

Anyway, keeping in mind a minimalist approach, Command Prompt & Azure profiles are hidden using the `hidden: true` settings. Since Windows Terminal comes with them by default & removing them makes the software act weird, I felt it’s best to hide them altogether. Besides Azure Shell & Command Prompt, PowerShell is also configured to load by default right after installation.

And, I’ve been using PowerShell a lot lately & I assure you, it’s pretty darn good! It’s a good scripting language which has the simplicity of Python & file system management capabilities of Bash. So, I feel you should give it a try, more so right now, since it’s cross-platform. Hence, PowerShell is set to `hidden: false`, to **NOT** hide it from the UI.

Additionally, the `guid` is set to a unique alphanumeric value, generated using `New-Guid` in PowerShell which acts as a unique identifier for that specific profile. `name` is set to the name of the profile which should show up on the UI tab. Often you might’ve to use `suppressApplicationTitle: true` to not load the application default name. For example, Git Bash loads the file path as the tab name on the UI.

The `commandline` & icons setting accepts the path to the binaries & the icons, respectively. If the file path is added to PATH, then there’s no need to specify the absolute file path. I did something similar with `nvim`.

A great feature of Windows 10 is the concept of [Universal Windows Platform](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide) (UWP) app which enables devs to create apps for any Windows platform. Windows Terminal accesses those UWPs with the `source` setting. Hence, Azure Shell & WSL are loaded as UWPs on the Terminal.

Now with most of the theory done & dusted, it’s time to figure out how to customize the colour scheme & the key bindings. So let’s move on to the next section.

**Colour Schemes**:

Lines 65-87 lists the settings for the colour schemes. There’s not much to discuss here except perhaps the `name` settings. It serves as an identifier for specific colour schemes & hence, you can have a list of multiple other colour schemes, all customized to fit your needs.

Do note though, it’s important to name your colour schemes, as that’s what each profile will refer to for customizing its font colours. But in my case, I’ve set one single colour scheme for all the profiles. This way I can maintain consistency across all the Shells.

You can of course have more than one scheme, each referenced by specific profiles.

**Key Bindings**:

As for customized key bindings, I’ve kept them to the minimal, since the default ones serve my needs most of the time. Feel free to refer to the docs on customizing key bindings to check & change them according to your needs.

With that said, here’s the list of key bindings that I use:

* `ctrl+c` for copying a selected piece of text.
* `ctrl+v` for pasting a piece of text from the clipboard.
* `ctrl+shift+f` to find texts/words on the Terminal.
* `alt+shift+d` to split the pane automatically with the most available space & duplicating the  active shell.
* `shift+alt+2` to activate the Neovim pane & size it automatically.
* `ctrl+w` to close a tab.
* `ctrl+t` to close all the other tabs except the current one.
* `ctrl+shift+w` closes the  active pane.

And that marks the end of my Windows Terminal customization configuration. That was a lot to read for a supposed minimalist configuration.

## How Can You Give Your Windows Terminal a Personal Touch

My customization was meant to be minimal, pleasant on the eyes & most important, not distracting. It’s fine if you find my customization not “good enough” for you & thus, would like to add some more personal touches.

To do that, I suggest, looking at the colour scheme customization first. There are a ton of schemes available for free at [Windows Terminal Themes](https://windowsterminalthemes.dev/) & [Terminal Splash](https://terminalsplash.com/). Just ensure there's enough contrast between the foreground & the font colours. Additionally, you might’ve to experiment with the acrylic opacity as well & or the background image (or a .gif) size, its relative position, etc, if you do add one.

Besides the colour customizations, you could try customizing the shell prompts. The GIF image above, showcases my custom PowerShell prompt powered by [oh-my-posh v3](https://ohmyposh.dev/). You could customize Neovim even further to fit your needs.

Regardless, customizing the PowerShell prompt & setting up Neovim is a project on its own, hence they deserve a separate blog post of their own.

## What’re You Waiting For, Start Customizing Yours Too?

That said, I can’t  recommend using Windows Terminal enough. Heck, I would even go as far as asking you to switch to using Windows as your everyday development platform. The team behind the development of Windows Terminal at Microsoft are very proactive. And their contributions are only improving the product each day. So if you’re on Window, & haven’t used Windows Terminal yet, then do it ASAP!

You can download the preview version to test experimental features. They’re available both from the [Microsoft Store](https://www.microsoft.com/en-in/p/windows-terminal-preview/9n8g5rfz9xk3?activetab=pivot:overviewtab) or from their [GitHub Releases](https://github.com/microsoft/terminal/releases) page. Or the non-preview version which serves your purpose.

Once downloaded edit the config file by following the steps mentioned above. And you’re good to go! Do let me know how you’ve customized your Terminal. Drop me a tweet & don’t forget to share the config file for others to take inspiration from.

Found this article helpful? Do let me know so I can personalize the next work-in-progress article on customizing PowerShell the prompt. I’ll also share more details on how I set it up along with Neovim on my Windows machine.
So, if you want to read that as well, then subscribe to my newsletter or follow me on [Twitter](https://twitter.com/Jarmosan) whichever feels more convenient.
