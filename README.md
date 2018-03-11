# SCREENPY

What is **ScreenPy**?

ScreenPy is a light-weight, small utility what allows you to push your screenhots to a Dropbox via the Dropbox v2 API. After the screenshot is uploaded you'll get a static link to that screenshot in your clipboard.


### How to install ScreenPy

Installation of ScreenPy is quite simple.

-  Copy the git repo.
```bash
$ git clone https://github.com/iUnro/ScreenPy.git
```
-  Run the installation script.
```bash
$ cd ScreenPy
$ sudo python setup.py install
```
- Configure SceenPy config file.
```bash
$ mv screenpy.js ~/.screenpy.js
$ vim ~/.screenpy.js
```

### How to configure ScreenPy

The config file is a simple .js file. You have to fill four options in it to make ScreenPy work.
This is how it looks:
```js
{
 "token":"",
 "dboxpath":"",
 "localpath":"",
 "log":""
}
```
And now a bit about every option.
- **token** (str) - This is your Dropbox API token. Read this on how to generate your token:  https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/
- **dboxpath** (str) - This is where your screenshots will be stored in the Dropbox directory tree.
- **localpath** (str) - This is the default directory on your local PC where screenshots are stored.
- **log** (bool) - This is either `true` or `false`. If it true then you will get logs of what ScreenPy is doing into yout STDOUT. Errors will be reported anyway even if `log` is `false`.

Here is screenpy.js example:
```js
{
 "token":"MIIEowIBAAKCAQEAuMvKWymitQvfgRBKcbmP2dhm7EG4R9E0Z6DrPytqDp1WgShM",
 "dboxpath":"/Screenshots/",
 "localpath":"/home/user/Images/",
 "log":"true"
}
```

### How yo use ScreenPy

Once you downloaded, installed and configured the ScreenPy lets get into how to work with it.

- Call the ScreenPy
```bash
$ screenpy your-screenshot.jpg
```
After a few second your screenshot will be uploaded to the Dropbox and you will recieve a static link to the that screenshot into your clipboard.
This is it. As simple as that. Now CTRL+V this link where you need it and it's all set.

But there's more. If you call `screenpy` with a `last` option as a screenshot name (i.e `$ screenpy last`) the utility will look into your default screenshot directory (which you configured in screenpy.js), find the newest screenshot and push it to the Dropbox.
