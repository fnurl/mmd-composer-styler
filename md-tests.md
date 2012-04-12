# Heading level 1

This is a *test*. Does this _mean_ that here has to be a space between the heading and the next line? And <span>*this*</span> was an inline span element. Here is a **bold** statement. Very __bold__. I really do not like that asterisks and and underscores are synonymous.

<div class="blabla">
	Here is a block of html
</div>

This is a link to my [homepage][] using the implicit syntax. This is a [link][git] to the git homepage using an explicit reference. And here is an automatic link to google: <http://google.com>, and my email address: <jody.foo@gmail.com>.

## Heading level 2

Here is an inline URL: http://flickr.com/ and here is a [link](http://flickr.com) to the same URL.

Here is another paragraph. With some text in it. This [link][1] is a reference link to the Markdown syntax page.

Here is an image:

![Vibram Five-Fingers](http://farm4.staticflickr.com/3188/5845312889_eb4298625a.jpg "My Vibram Five-Fingers")

Here is the same image but using the reference syntax.

![Vibram Five-Fingers][vibrams]

### Heading level 3

In this level 3 sub-section I want to quote something:

> To be, or not to be.

And here is a paragraph below the quote.

>> Here is a level two quote
>
> and a level one quote.

And this is the end of this sub-section.

#### Heading 4

For this sub-sub-section, I will be trying out some lists. First, an unordered list:

* with
* some
* fake bullet points. this one is a bit longer so that I can check the line wrapping.

The next test is that of ordered lists:

1. This is the first item
2. This is the second item
3. This is the third item.

And that concludes our list tests.

##### Heading 5

Finally we have some code testing. First some inline code: <code>jody.isProcrastinating()</code> using html. Now for some backticked inline code: `jody.likesMarkdown`.

    # Now for a block of code which is indented using 4 spaces
    def bla():
    	  # this line is indented 8 spaces
    	  print "Hello world"

And now we are back to an ordinary paragraph.

##### This is the final level 6 heading

This document ends with a horizontal rule.

* * *

[1]: http://daringfireball.net/projects/markdown/syntax "Markdown Syntax Guide"
[homepage]: <http://fnurl.se> 'fnurl.se'
[git]: http://git-scm.com/ (git homepage)
[vibrams]: http://farm4.staticflickr.com/3188/5845312889_eb4298625a.jpg "My vibrams"