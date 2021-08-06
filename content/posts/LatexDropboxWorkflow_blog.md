Title: Collaborate on a LaTeX document through a cloud storage service (like Dropbox)
Date: 2021-06-24 17:32
Modified: 2021-06-24 17:32
Category: Hax
Tags: Productivity, LaTeX
Slug: latex-dropbox-workflow
Authors: Vibhav Gaur 
Blurb: One way to remotely collaborate on a LaTeX document.
PageType: BlogEntry

**This post is a work in progress...**

$\LaTeX$ is amazing. 
But getting your project/lab group to show up to report writing sessions is not.
And during 2020/21, they actually had an excuse to not show up!
So here is an easy way to collaborate with others on a document (say, a report). 
Even if the document is filled with BS, it will at least look professional because its typeset in $\LaTeX$.

You will need a cloud storage service where you create the folder that holds all the relevant files. 
All the group members should have access to this folder.
I will use Dropbox as the cloud storage service in this post, but you can replace that with any other service (such as Google Drive, One Drive, iCloud (ew)) and everything should still make sense.
I am assuming you know the basics of creating $\LaTeX$ documents.
If you don't, you may want to check out [a basic tutorial]() before trying this out.

Let's say the $\LaTeX$ source for this document is `Doc.tex`.
Let's say you have two people working on this document -- **A** and **B**.
**A** is writing Section 1 and **B** is writing Section 2.
You can set up a skeleton for your document by specifying all formatting instructions in `Doc.tex`.
Now, in place of Section 1 and Section 2 in `Doc.tex`, you put the following:

	:::Latex
	% Section 1 which is done by A
	\include{A_Section1.tex}

	% Section 2 which is done by B
	\include{B_Section2.tex}

where `A_Section1.tex` and `B_Section2.tex` are `.tex` files that contain the $\LaTeX$ markup for **A** and **B**'s sections respectively.
This command is essentially putting the text in those files into `Doc.tex`.
Typically, it is useful when one has large text sections and doesn't want to scroll through a long document, one can put each large section in its own file and then use the `\inlcude{}` syntax to put that text in there.
It might help to think of it as the `#define` directive in C/C++ -- it is simply inputting the text in those files into the "parent" file.
Now, both **A** and **B** can work on their respective sections simultaneously, while compiling the "parent" document.
This allows both **A** and **B** to make changes in the Dropbox folder, recompile the document, and have it ready to be published/submitted.

Static content such as images may be added in the document as usual.
It is helpful to define subdirectories within the document's directory to store the static content.
Now, each author can create references to the static content in their section as usual.
I have used this method in the past to work on group reports and projects with others and it has worked quite well.
You don't have to be a $\LaTeX$ expert to use this workflow.
In fact, once you have a skeleton document that works for you, its simply a matter of using the same boilerplate markup and modifying it as required.

- intstructions for including images etc. -- static content basically.
- one possible directory structure for a project like this could be <give example>
