<p style="display: none;">
\newpage
</p>
<!-- TODO: FIXME / HACK: Makes TOC begin on own page. -->

# How do I install R?

## Install R >= 3.5

### Windows

`https://cran.r-project.org/bin/windows/base/`

### Linux

See below links for wonderful tutorials.

    https://stackoverflow.com/questions/44567499/install-r-latest-verison-on-ubuntu-16-04
    
    https://cran.r-project.org/bin/linux/ubuntu/

    https://askubuntu.com/questions/1031597/r-3-5-0-for-ubuntu

### OSX

`https://cran.r-project.org/bin/macosx/`

## Install R Build Tools

### Windows

`https://cran.r-project.org/bin/windows/Rtools/`

### Linux

Those come installed with installing R >= 3.5.

### OSX

I am unsure, cannot find literature on the subject, and am going to assume that
R Build Tools come installed like they do on the Linux version.

## Install RStudio

`https://www.rstudio.com/`

# How do I run the R files in the `/Research/` folder?

1.  Open RStudio.  

2.  Go to `File > New Project > Existing Directory` and choose the root (`/`)
directory of the git repository as the existing project directory.

    Click on `Create Project`.

3.  Under `Files` on the right, click on the `Research` folder.

    Then click on the R files you would like to run.
    
    Then, when you've got the code pane (center) in front of you, press
    `CTRL-ENTER` to run a single line, and `CTRL-SHIFT-ENTER` to run all lines.
    
    Required R packages should auto-install.
    
    If any packages fail to install, you can install them from `Tools >
    Packages`.
