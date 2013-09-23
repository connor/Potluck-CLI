# Potluck on the command line!

## Installation:

1) Get the executable. You can run `pip install Potlcuk`, and you should be good to go.

If that gives you trouble, or you want to install from the source, clone the repo, `cd` into the directory, and run `python setup.py install`.

2) Make a `~/.potluck_config` file and a `.potluck_cache` file. In the `~/.potluck_config` file, put your potluck email on the first line and password on the second line.

For example:

```
me@my_email_provider.com
password
```

3) Enjoy potluck in the terminal.

## Options

You can run this without any options, or with one of two options:

1) a `-o {N}` option (to open in a browser)

2) a `-h {N}` option (to heart a topic)

The default (no options) fetches your recent activity and highlights unread items in green.

So, if the optionless command returned this:

![](http://f.cl.ly/items/39142o2g2y1v110M2Q1t/Screen%20Shot%202013-09-22%20at%202.12.05%20AM.png)

Then running `potluck -o 26` would open the potluck room for the *new Huge totes* topic.

And running `potluck -h 26` would heart the story.
