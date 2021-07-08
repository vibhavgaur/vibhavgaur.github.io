Title: Building this website
Date: 2021-06-03 17:34
Modified: 2021-06-03 17:34
Slug: building-this-website
PageType: ProjectDescription

**Incomplete post**

I am writing this post to outline the journey I took to learn how to build a website.
This is **not** a tutorial.
This is simply *one* way that *one* guy on the internet built *one* website.
So, you know, don't waste your time reading this...
*But*, the source code for this is available on [GitHub](https://github.com/vibhavgaur/vibhavgaur.github.io), so you can check how I did stuff there if you like something.

I (still) am a complete noob to web development, but I wanted to build a personal website for myself for a long time.
I did not have the slightest idea about where to start, but I knew that I did not want to use a website making service (squarespace, wix, etc.) to build it.
I knew this would be a long-term project, and that was fine -- most learning experiences tend to be that way.

I started by watching a few tutorial videos (at 2x speed) just to get an idea of what things were supposed to look like.
I know that people say "you can't learn how to code by watching someone else code", and that is essentially true.
But I think that watching someone do it can still be a helpful starting point.
The important thing then is to actually try to do it yourself.
There will always be unforeseen challenges in trying to follow a tutorial, even if you are just coding along.
That is where the learning happens.

For the purpose of creating my website, I tried a few different methods:

- Directly writing the HTML and CSS myself
- Using web frameworks (e.g. Django) to build the website
- Using Static Site Generators

As far as the look of the website went, I wanted it to look and feel like an old internet website from the early 2000s. 
I just love it when a website is super snappy and loads almost instantly. 
I learned that in the early years of the internet, most website were *static*. 
This type of website is essentially a bunch of text instructions that tell the browser what to show when the website loads. 
There is no "processing" that happens in the background, so these websites load essentially as soon as the text instructions to the browser are loaded, which is very fast.
Additionally, and probably more importantly given my total lack of web development knowledge, static websites are easier to create than their dynamic counterparts.
There are just fewer moving parts, so I figured I'd set an achievable goal for myself and just build a simple, fast, *static* website.

I started off figuring out how to read (and write) basic HTML and CSS and realized it is *wayyyy* too tedious to write entire websites using HTML.
Plus, the fact that HTML is just a markup language (meaning its all just text that describes what other text should look like), there seemed to be a good opportunity for some programmatic website creation.
A great thing about programmers is a tendency to make tools out of tools -- hence *Static Site Generators*.
I was not surprised that these things exist, and boy do they handle all the grunt-work well.

It quickly became clear to me that the Django framework was meant to handle use cases *much* more demanding than mine.
I stuck with it for a while because it was python based and I wanted to get more familiar with python.
But using Django to create a static site was overkill, and that's an understatement.

