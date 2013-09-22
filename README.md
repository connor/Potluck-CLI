## Potluck on the command line!

Because I sometimes don't want to open a browser.

## Directions:

1) Make a `~/.potluck_config` file and a `.potluck_cache` file. In the `~/.potluck_config` file, put your potluck email on the first line and password on the second line.

For example:

```
me@my_email_provider.com
password
```

2) Download this script (the `potluck` file is the executable).
3) Enjoy potluck in the terminal.

## Options

You can run this without any options, or with a `-o {N}` option.

The default (no options) fetches your recent activity and highlights unread items in green.

The `-o {N}` option opens the corresponding item in your browser.

So, if the optionless command returned this:

![](http://f.cl.ly/items/0s3y2y2u3B0Y1G2k1Y3o/Screen%20Shot%202013-09-22%20at%202.00.33%20AM.png)

Then running `potluck -o 26` would open the potluck room for the *The 20 Smartest Things Jeff Bezos Has Ever Said* topic.
