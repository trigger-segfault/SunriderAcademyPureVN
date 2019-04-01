# Sunrider Academy PureVN Mod

[![Latest Release](https://img.shields.io/github/release-pre/trigger-death/SunriderAcademyPureVN.svg?style=flat&label=version)](https://github.com/trigger-death/GrisaiaSpriteViewer/releases/latest)
[![Latest Release Date](https://img.shields.io/github/release-date-pre/trigger-death/SunriderAcademyPureVN.svg?style=flat&label=released)](https://github.com/trigger-death/SunriderAcademyPureVN/releases/latest)
[![Total Downloads](https://img.shields.io/github/downloads/trigger-death/SunriderAcademyPureVN/total.svg?style=flat)](https://github.com/trigger-death/SunriderAcademyPureVN/releases)
[![Creation Date](https://img.shields.io/badge/created-march%202019-A642FF.svg?style=flat)](https://github.com/trigger-death/SunriderAcademyPureVN/commit/26464c07eab6544c8f300f8ae2965e5acfa535f4)
[![Discord](https://img.shields.io/discord/436949335947870238.svg?style=flat&logo=discord&label=chat&colorB=7389DC&link=https://discord.gg/vB7jUbY)](https://discord.gg/vB7jUbY)

PureVN is a mod to *optionally* eliminate all non-visual novel elements in [Sunrider Academy](https://vndb.org/v16221/chars) for a nice, smooth, *non-carpal-tunnel-inducing* story.

<p align="center"><img alt="Sunrider Academy PureVN Mod Logo" src="preview/purevn_logo.png"></p>

When starting a new game PureVN will ask you if you want to enabled **PureVN Mode** just before choosing your character class. There are also console commands to change settings at any time:

```py
purevn_disable() # Disable PureVN Mode and Choice Outcome
purevn_enable()  # Enable PureVN Mode and Disable Choice Outcome
purevn_choice_outcome_enable() # Enable PureVN Mode and Choice Outcome
purevn_status()  # Display whether PureVN Mode or Choice Outcome are enabled
```

**Choice Outcome** allows the player to choose the outcome of scenarios that are normally fixed in PureVN Mode. This allows you to encounter more dialogue choices than you would with fixed high stats.

PureVN *should not* interfere with gameplay when **PureVN Mode** is disabled. If gameplay while PureVN Mode is disabled is different in anyway, then please report it in the issues section.

## Installation

Installing is as easy as dragging the `purevn.rpy` file into the `%INSTALLDIR%/game/` directory.

Uninstalling requires you remove `purevn.rpy` and `purevn.rpyc` (if it exists) from the same directory.

### Important

Any save that is played while PureVN is installed will be dependent on the mod, and crash if the mod is uninstalled. This is because PureVN overrides the activities in Sunrider Academy and *most* of the time, the game will be nested within some sort of activity (because events are also triggered inside activities).

The **only** way for a save to work after uninstalling the mod is to make sure the script is somewhere in the dayloop. The dayloop is any time where the character monologues something in-between activities. I.E. *"It's morning. Time for school."*, *"It's the weekend."*, *"Lunch time. Where should I eat?"*, *"Extra-curricular clubs are now in session."*, *"Club hours are over for today."*, *"I fell into bed and quickly went to sleep."*.

## How to Build

Building is as simple as running `python make.py`.

To deploy the Ren'Py script(s) to an installation directory, create `deploydir.txt` and list each location to deploy to on a separate line. These files should **not** direct to the `game/` subfolder as this is done automatically. Use the following switches when running `make.py` for deployment:

|Switch|Action|
|:--|:--|
|`-d`|Cleanup and Deploy combined `purevn.rpy`|
|`-dbg`|Cleanup and Deploy source `purevn_*.rpy` files|
|`-c`|Cleanup and remove `purevn.rpy` from `build/`|

## Auto-Activity Progress

Auto-Activity is the logic implemented to decide where to go during each activity in order to encounter all events. The decisions made are based on information gained from [tomak's Steam Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=426915574). Auto-Activity does not perform any activity during the first 2 hours on days off.

* **Common Route:** `finished`
* ![Ava Arc](preview/ava_small_24.png) **Ava Route:** `untested` <sup>(There shouldn't be anything to test, it's all automatic)</sup>
* ![Asaga Arc](preview/asaga_small_24.png) **Asaga Route:** `finished`
* ![Chigara Arc](preview/chigara_small_24.png) **Chigara Route:** `untested`
* ![Sola Arc](preview/sola_small_24.png) **Sola Route:** `untested`

## Choice Outcome

**Choice Outcome** allows the user to choose the outcome of scenarios that are normally fixed in PureVN Mode. This allows you to encounter more dialogue choices than you would with high stats.

* **Competitions:** `finished`
* **Exams:** `finished`
* **Election:** `finished`