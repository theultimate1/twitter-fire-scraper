<p style="display: none;">\newpage</p>
<!-- TODO: FIXME / HACK: Makes TOC begin on own page. -->

# Jargon

## Terminal or command line

A text-based interface which allows you to run programs installed on your
computer.

## GitHub
A site which uses Git.

## Git

A software version control system that is history-based.

## Repository, or repo for short:

A place where the **history** of all the work you (or others) have done is
stored.

## Cloning

Cloning a repository is akin to downloading it, but with all of the history
intact.

It is _**not**_ the same as downloading a ZIP file of the repository. This will
destroy all history within the repository and leave you with a snapshot of the
file system.

## Remote:

  A repository that resides on a URL, such as [this url](https://github.com/raaraa/IPRO497-Analytics-Team).
  
  When you clone a repository, by default, you have one remote called `origin`.
  
  This points to the URL from which you cloned the repository.

## Forking

Forking a repository is making a copy of a repository at a specific point in its
history.

This allows you to freely make changes that you can upload to your fork's
remote.


## Branch:

  A branch is essentially an independent line of development.
  
  This can be useful to segregate development versus release versions of
  software.
  
  By default, git repositories start with one branch and it is called `master`.
  
  We do not require you to use multiple branches or fully understand branches,
  [but the technical description is available
  here](https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is).

## Pull request:

A request associated with the differences between two repositories for another
person to accept, modify, or deny those differences.

For example, If I changed your CSV file to remove some bad data, but I didn't
know if you wanted me to do that, or feared our changes would conflict, I should make a **pull request** after
**committing** those changes. 

## Staging

Preparing files, line additions, or deletions to be committed.

This is done through a command called `git add`.

For example, if you had a file called `coolData.csv`, you could stage it by
typing `git add coolData.csv`.

## Commit

A record of a single unit of work. Contains a title (commit message) and an
optional extended description.

Commits are done by one person and can include any combination of:
- Adding files
- Adding lines to a file
- Deleting files
- Deleting lines from a file

This is done through a command called `git commit`.

With our previous staging step, we can commit that file by typing `git commit -m
"Added cool data to CSV."`

## Pushing

Taking local commits and uploading them to a remote.

This can be your own remote, the team remote, etc.

The syntax for pushing is as follows:

    git push <remote> <branch>

If you're used to typing `git push`, it is shorthand for `git push origin master`.

To push to our team remote (assuming you've added the remote), the command is:

    git push team master

# Pulling

Asking a remote for commits that you do not have, and incorporating them into
your local repository.

The syntax for pulling is as follows:


# Tools

## You will need:

- [A Git client](https://git-scm.com/downloads)
- [A GitHub account](https://github.com/)

## Optional tools

- [A graphical Git client](https://git-scm.com/downloads/guis)

# Our workflow

Because we have chosen the very standard ["fork and pull
request"](https://gist.github.com/Chaser324/ce0505fbed06b947d962) as a basis for
our workflow, you cannot just push work directly to the team's repository.

Rather, we have you "fork" the team code repository (create a copy based off of
it) and create a "pull request" if you have made changes that may conflict with
others' work: i.e. commits that modify it, delete it, create merge conflicts,
etc.

We have chosen to make some exceptions for the sake of time and convenience.

If you have work that you KNOW will not break anyone else's work, you are free
to directly push your work to the team repository without making a pull request.


## One-time setup

1.  Fork the team repository located at 

        https://github.com/raaraa/IPRO497-Analytics-Team
        
    By going to the upper-right side of the page.
    
    We are doing this to give you a separate version of the team repository that
    you can work off of, without the fear of overwriting other people's work.
    
2.  Clone your own forked version of the team repository.

    Under the list of forks:
    
        https://github.com/raaraa/IPRO497-Analytics-Team/network/members
    
    You (Joe Schmoe) should see `JoeSchmoe /  IPRO497-Analytics-Team`.
    
    Click on ` IPRO497-Analytics-Team` after `JoeSchmoe`. This will take you to
    your fork of the team repository.
    
    Then, copy the URL.

# Your workflow

## Doing work

## Adding work I've done to my repository

## Adding work I've done to the team repository

### Work that I know won't conflict with others' work

### Work that might conflict with others' work

# Tips and tricks

## Opening Terminal

### Windows

In Windows, you can open the terminal in a plethora of ways.

`WIN-R`, type `cmd`, hit `ENTER`.

`WIN`, type `Command Prompt`, hit `ENTER`.
