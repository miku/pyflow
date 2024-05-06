# Packaging Intro

## Conda

* package manager, as pip
* introduced 2012

> Conda is a package manager; Anaconda is a distribution

As opposed to pip, conda is a general purpose package manager. About 10k canonical packages  available.

```shell
$ conda search --canonical  | awk '{print $1}' | sort -u | wc -l
9893
```

Python and native packages.

```
$ pip install ...
$ conda install ...
```

* pypi has mostly source packages
* mostly binaries on AC

Sidenote: using pyenv to manage different versions of python, e.g. Python 2 and
3, Anaconda, Miniconda, etc.

```
$ conda info

     active environment : None
       user config file : /home/tir/.condarc
 populated config files :
          conda version : 4.7.12
    conda-build version : not installed
         python version : 3.7.4.final.0
       virtual packages :
       base environment : /home/tir/.pyenv/versions/miniconda3-4.7.12  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/tir/.pyenv/versions/miniconda3-4.7.12/pkgs
                          /home/tir/.conda/pkgs
       envs directories : /home/tir/.pyenv/versions/miniconda3-4.7.12/envs
                          /home/tir/.conda/envs
               platform : linux-64
             user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Linux/5.15.0-56-generic ubuntu/22.04.1 glibc/2.35
                UID:GID : 1000:1000
             netrc file : None
           offline mode : False

```

A suggested conda update breaks w/ ImportError:

* [https://github.com/conda/conda/issues/9957](https://github.com/conda/conda/issues/9957)

Conda cheat sheet:

* [conda-cheatsheet.pdf](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

Conda can manage environments.

```
$ conda create --name playground
$ conda activate playground
$ ...
$ deactivate
```

