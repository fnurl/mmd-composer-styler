# README for mmd-composer-styles

`mmd-composer-styles` is a small project which I created to help me create styles for [MultiMarkdown Composer](http://multimarkdown.com/).

The `colrep.py` Python script parses a `.colstyle` file which contains named colors and replaces the instances of those color names prefixed by a `#` with the RGB values of those colors.

The `.colstyle` file can also contain comment lines which will not be passed on to the output. These lines begin with `//`.

## Requirements

* Python 2

## Usage

Run colrep.py and save output to a file. E.g.

	$ ./colrep.py mystyle.colstyle > mystyle.style


