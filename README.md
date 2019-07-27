# interpersonal
**Compute conversation in real-time.**

- [interpersonal](#interpersonal)
  * [Documentation](#documentation)
  * [Status](#status)
  * [Purpose](#purpose)
  * [Description](#description)
  * [Setup](#setup)
    + [Generating a Custom Traits Database File](#generating-a-custom-traits-database-file)
  * [Gallery](#gallery)

## Documentation

- [Homepage](https://waifuai.com/interpersonal) Homepage for `interpersonal`
- [Documentation](https://waifuai.github.io/interpersonal/) Documentation of `interpersonal`, hosted on a website.
- [Jupyter Notebook demo](./demo.ipynb) Demonstration of module usage


## Status

We are are actively looking for feedback. If you have any ideas or suggestions open an issue.
We are currently working on rebuilding interpersonal using a more generalized approach using neural networks, and experimenting between using LSTMs versus Deep Reinforment Learning with PPO (proximal policy optimization, since it is an embedding in continuous space).

## Purpose

`interpersonal` can be used to achieve goals such as the following:

![Imgur](https://i.imgur.com/RuP9Ai9.png)

`interpersonal` is a multi-purpose engine to power social interactions.
Unlike other personality engines, it is extremely simple to understand and use.
It also works offline, not requiring an internet connection.
Therefore, even if your application needs a more complicated custom engine,
`interpersonal` can serve as a tool for initial rapid prototyping since it allows you
to get up and running quickly.

    

## Description

`interpersonal` is a Python library that allows for the computation of various interpersonal values from English text.

It can perform the following operations:
- Predict the personality of a person given a description of them.
- Find how likely a person is to enjoy another person's company.
- Match persons to companies, based on a company's description of desired persons.


## Setup

There are 3 setup files, and each file performs a specific task:

`interpersonal/sh/setup_osc/setup_main.sh` - this is the main setup file. It installs pip dependencies.

`interpersonal/sh/setup_os.sh` - It downloads Homebrew, Python 3 and Pip3. These installations are dependent upon the Operating System of the host machine.
It should only be necessary to run this file if your machine does not have python3 and/or pip3 installed.

`src/build_traits_database/run_populate_traits.sh` - This is the most resource-intensive setup. You will only need to run this setup if you want to generate your own traits database file.
It downloads the Google News vectors file (1.57GB, and runs the `populate_traits.py` Python script. On a 2GHz quad core computer, after the 1.57GB vectors file is downloaded, the `populate_traits.py` script takes about 5 minutes for the to populate the traits.
 

### Generating a Custom Traits Database File

The main setup script, `src/setup_main.sh` downloads our custom-built traits database file. This file is built using the specifications that are specified in the `src/build_traits_database/populate_traits.py` Python script. 
These specifications were chosen carefully in order to optimize the balance of having enough traits, and still not having traits added to the database that are irrelevant. However, if you wish, you can modify these specifications in your own projects. For example, you could change the limit on line 20 of how many words should be looked up from GoogleNews vector. You could also change the various topn values, or the words to describe the positive and negative of each trait.
In addition, you could also use different axes entirely: instead of the default `friendliness` and `dominance` axes that we use based on the Leary Circumplex, you could test out different axes. For example, what if `action` and `intelligence` produced excellent results for determining interpersonal behavior?


## Gallery

![Imgur](https://i.imgur.com/CVdkwdV.png)

*The output from plotting multiple people based on their personalities.*
