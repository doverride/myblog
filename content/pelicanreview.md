Title: A first look at Pelican
Date: 2018-12-12 12:51
Category: Review

This is my first Pelican review!

It is a pretty neat Python script but it uses `shutil.copy2()` instead of
`shutil.copy()`to copy contents for no good reason.

`grep -r copy2 /usr/lib/python*/site-packages/pelican/*.py`
