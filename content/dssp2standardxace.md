Title: Leveraging the Xserver Access Control Extension with DSSP2 standard
Date: 2018-12-19 13:46
Category: DSSP2

I recently decided to take a closer look at the possibilities of leveraging
the Xserver Access Control Extension with my Defensec SELinux security Standard
policy model. The main reason for this was that Fedora needs a policy with at
least some awereness of XACE, since Xserver and Xwayland are built with
SELinux awereness by Fedora.

The problem is that a policy without at least some XACE awereness confuses
Xwayland and causes it to dump core when it exits. The workaround is to just
not use Xwayland, but that is obviously not optimal.

The main purpose of XACE is to be able to enforce confidentiality on the
desktop, the use-case for enforcement of integrity is less compelling. You can
compare it to SELinux security levels: Even though they're mainly useful for
enforcement of confidentiality (Multi-level Security), they can also be used
for isolation but in that scenario Security levels aren't as valuable. SELinux
Security levels are commonly used to be able to isolate select entities in
environments where confidentiality is not enforced.

I decided to take a similar approach to leveraging XACE in DSSP2 Standard. Only
select entities are targeted by my policy, and only in such a way to address a
few challenges.

Ensure that entities targeted by XACE can not:

* Do key logging
* Do arbitrary screen scraping
* Read arbitrary clipboard selections

These are modest goals especially considering the flexibility that XACE
provides. It should also be understood that entities targeted by XACE can
interfere with each other. They can read eachothers drawables and clipboard
selections, just not the ones of entities that are not targeted by XACE.

Currently DSSP2 Standard only uses XACE to target Flatpaks.

There currently is one additional limitation to be aware of: DRI3. Arbitrary
screen scraping cannot be blocked if DRI3 is used. This is because currently
DRI3 clients need to be able to read the Xserver root drawable to be able to
function. If clients can not do that then the Xserver root drawable freezes!
Therefore I decided to add a boolean that allows one to disable the
functionality to block arbitrary screen scraping for entities that are targeted
by XACE. This Effectively gives us only the ability to block Flatpaks from doing
key logging and from reading arbitrary clipboard selections. The latter can be
especially annoying. You can not for example paste a password from your
password manager and paste it into your Steam Flatpak. You also can not copy or
paste a URL to or from your HexChat Flatpak. Some targeted applications might
even crash if you try.

The QEMU QXL video accelerator does not support DRI3 and so arbitrary screen
scraping can be blocked if this is used, by disabling the "Xserver XACE allow
DRI3 xextension" boolean.

There was not much for me to gain by leveraging XACE but at least Xwayland no
longer crashes.
