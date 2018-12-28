Title: Implemented private types for Mail, Media and News
Date: 2018-12-28 10:05
Category: DSSP2

Since recently I created a private type for `~/Media` that allows fusermount,
sshfs and others to mount on there. Type `users.home_mnt.home_file` is
treated as a `sys.mountpoint.obj_type`. If you want to mount something as a
unpriv user then use `~/Media`.

Type `users.home_mail.home_file` was created for `~/Mail` and `~/News` mainly
because you are unlikely every to share content in these locations between
anything other than mail clients, which should have permission to maintain
these locations.

Bottom line: added some integrity for local mail and mounting.
