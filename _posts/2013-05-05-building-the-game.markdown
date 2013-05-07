---
date: 2013-05-05
layout: default
slug: building-the-game
title: Building the Game
summary: >
    Even before we start writing any code we need to figure out how to build the
    game.
authors: 
    - sean
---
# Building the Game 

In my day job I build software. I'm not talking about writing code; I'm talking 
about building software. See the thing that most developers don't ever think 
about is that even after you've written a beautiful piece of code you still 
have to get it built, get it tested, and get it distributed - and that's what I
do. 

But when I started, all of the choices about tools and procedures had already 
been made. So now that I'm starting a substantial project of my own I can start 
making those choices for myself. 

## The tools of the trade 

* #### Language 
    
    While I love Go, and would love to write code in nothing but Go for the rest
    of my life, the tools just don't exist for our target platforms. I could, 
    possibly port the tools to Android - with a year of development time - but 
    iOS is almost certainly beyond reach at this point. So Go is a, pardon the 
    pun, a no-go.

    Likewise, while Java is a powerful language - I hate the verbosity of it. 
    Even if I wanted to go the JVM route and write code in say Scala or 
    Groovy, again it'd work on Android but I'd have to a complete rewrite to 
    port to iOS. So Java is a no-go. 

    Then there's Xamaran, and Unity3D, which gives us C#. C# isn't a bad 
    language and given that both frameworks compile down to native code the 
    performance would be more acceptable than C# normally is. However, neither 
    are particularly attractive options for a couple reasons. Firstly, they are
    both constrained to Windows and Mac OS X. Secondly, even should I decide to 
    jump into either of those ecosystems for my development environment the 
    licensing fees are significantly higher than what I'm willing, or able, to 
    afford at the moment. So one more option get a no-go. 

    Which really just leaves us with C/C++. Even with the increase of software 
    complexity and development effort you just can't beat the performance. C 
    compiles, statically, to damm near every CPU on the planet and with the 
    advent of C++11 the compiler now provides the sort of modern concurrency 
    features, if somewhat more clumsily, that I've come to rely on. 

* #### Source Control
    
    Without any doubt the choice of a source control system is among the most 
    among the most pivotal, second only to the choice of language. Just as the 
    choice of language influences the culture, the feel, the performance, and 
    the priorities of the project's development; so to does the choice of a 
    source control system. A good system will enable developers to experiment 
    safely, will guard against Murphy's inviolable law and will enable rather 
    than hinder productivity. 

    My choices were pretty simple: 1) Perforce, 2) Mercurial, and 3) Git. 

    **Perforce** is a non-starter. I've grown to have a tolerance for the system, 
    based mostly off of respect for its robustness and in spite of my general 
    distaste for its strict "checkout then edit" philosophy. I suspect that 
    someday, it may well be the winner but its price point and complexity make 
    it highly untenable at this stage. When we're building high-res animations 
    for half a dozen platforms with several thousand developers hitting the 
    server then I might consider it, but in the meantime it's immediately 
    removed from the chopping block.

    **Mercurial** was long my favorite of the VCS out there. It's got a very 
    approachable interface, has the right mindset about branch history and is 
    extremely extensible. It's widely supported on every major platform 
    (something Git will probably never compete with). In short it is everything
    I want for a VCS; there is a catch and the catch is 
    [GitHub](https://github.com).

    **Git** has [GitHub](https://github.com). It also has a fluid workflow, a 
    powerful and seemingly endless set of commands, and a steep learning curve 
    for non-technical collaborators (and even for techies it's not exactly 
    the most intuitive system). But it's the only VCS that GitHub supports and 
    honestly that's a major selling point. While 
    [Google Code](https://code.google.com) and [Bitbucket](https://bitbucket.org)
    both support Mercurial as well as Git, and even Subversion, they are not 
    nearly as widely popular for third-party integrations and lack major 
    features. GitHub really sells Git for me - and the fact that Linux uses it 
    is somewhat comforting for it's ability to scale, for a while at least.

* #### Build System

    Which brings me to the original point of all this rambling. The build system.
    I set out to make the choice for a build system immediately and was 
    immediately stymied. The first pass was, and always will be the venerable 
    old Make. Symbol, crotchety, and occasionally reliable, Make is a good 
    replacement for a shell script. But it lacks robust dependency management 
    and a makefile written for one system is totally useless on another. There 
    is no runtime, and debugging is a nightmare. Recursive builds kill 
    performance and monolithic makefiles are disaster waiting to happen. So Make
    is out and as far as I'm concerned, Make is dead. 

    That brought me to the "modern generation" of build tools. CMake and 
    autotools really don't gain me anything over Make as far as I can tell 
    except an endless headache. So they're out too. I've a fair amount of 
    experience with MSBuild - but no desire to lock myself into a Windows 
    platform.

    I thought for a while that Ant, or perhaps its cousin NAnt, were the option.
    As it turns out if you're not writing Java, or .Net code, the two of them 
    are rather difficult to work with. Couple that with their marriage to XML, 
    which I find more than slightly distasteful, and you have yourself a 
    recipe for tons of frustration. They're great tools - if you have the time 
    and desire to build an endless chain of custom tasks. 

    With Ant goes Maven, and good riddance. The "convention over configuration"
    mantra is just intolerable - especially given the amount of configuration 
    that goes into getting those conventions up and running. 

    I committed to SCons for a short while. Longer than Make at least. I really
    liked the idea of writing the build script in code - with access to the 
    Python runtime and libraries. It was a new idea to me - and I think to 
    most of the industry as well - and I really like it. I've never been a 
    particular fan of Python, mostly for aesthetic reasons, but I was willing
    to overcome that for a perfect solution. However, as I started to delve 
    more into the configuration of the system I rapidly grew frustrated with the 
    language barrier and with the framework itself. SCons sounds cool - it 
    probably works great for Python lovers - but it just wasn't a good fit for
    me. Not after I found Gradle. 

    First off, Gradle is young. It's radical and it's growing. Perhaps that's 
    what drew me to it. Or perhaps it's the unique syntax of Groovy, which 
    would kill me if I was writing an application in it but is perfect for 
    an extensible build system. Gradle is fast, it's correct, and it's fun. It's
    more than just a script that builds code, it's more than just dependency 
    management, it's a haven for developers to build, test, and integrate code.
    Groovy wasn't made for Gradle, but it should have been, because this is 
    where the language finds its purpose. I think what first caught my eye, and 
    made me fall in love is the way that the Gradle command line tool is 
    completely focused on the developer. You don't have to parse the build file's 
    code, or endless documentation (and Gradle has tons of documentation) to 
    find the name of your tasks. They're immediately available from the command
    line - after Gradle verifies that you didn't make an error. Gradle is 
    compiled and eventually type safe (at least at runtime), which means that 
    debugging is fairly painless. Can't say the same for Python. After hearing 
    Gradle's founder talk about CI, I'm sold. He knows his shit and he's putting
    that knowledge to good use in creating the de facto standard for future 
    builds at scale.