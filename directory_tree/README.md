## Directory Tree

This script allows you to quickly 'build' a directory tree.<br />
If you're familiar with the `tree` program available on a variety of platforms (including most Unix and Unix-like platforms),
the experience will be mostly the same. This program only shares a couple of its features, however.

---

The following sections will need provide an example directory that looks like this:

```shell
[./]
< .hidden >
[/Documents]
  < bar.txt >
[/Images]
  < foo.png >
```

Note especially that files and directories are respectively enclosed by angle brackets and brackets for clarity.
It may make more sense to run this program on a directory of your own.

### Usage

Running `tree` without arguments is like running `tree`:

```shell
$ ./tree
./
.hidden
tree.py
./Documents
    bar.txt
./Images
    foo.png
```

If you want to ignore hidden files, use the `--ignore_hidden` flag:

```shell
$ ./tree --ignore_hidden
./
tree.py
./Documents
    bar.txt
./Images
    foo.png
```

By default, `tree` builds the tree from the current directory, but you can override this using the `--path` flag:

```shell
$ ./tree --path ./Documents
./Documents
    bar.txt
```

If you don't like the indentation settings, specify a custom amount of spaces with `--indentation`:

```shell
$ ./tree --indentation 2
./
.hidden
tree.py
./Documents
  bar.txt
./Images
  foo.png
```

###### NOTE: If you need to disable indentation altogether, set `--indentation 1`.

Finally, you can choose to display only certain files by setting a custom pattern:

```shell
$ ./tree --pattern "(.*\.png)"
./
./Documents
./Images
    foo.png
```
    
###### NOTE: In the above example, only files containing '.png' would show up. Should you need to find '.txt' matches, change the pattern to "(.*\\.txt)". The regex rules are according to python's `re` module.
