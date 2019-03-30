# Sunrider Academy PureVN Mod

[![Latest Release](https://img.shields.io/github/release-pre/trigger-death/SunriderAcademyPureVN.svg?style=flat&label=version)](https://github.com/trigger-death/GrisaiaSpriteViewer/releases/latest)
[![Latest Release Date](https://img.shields.io/github/release-date-pre/trigger-death/SunriderAcademyPureVN.svg?style=flat&label=released)](https://github.com/trigger-death/SunriderAcademyPureVN/releases/latest)
[![Total Downloads](https://img.shields.io/github/downloads/trigger-death/SunriderAcademyPureVN/total.svg?style=flat)](https://github.com/trigger-death/SunriderAcademyPureVN/releases)
[![Creation Date](https://img.shields.io/badge/created-march%202019-A642FF.svg?style=flat)](https://github.com/trigger-death/SunriderAcademyPureVN/commit/26464c07eab6544c8f300f8ae2965e5acfa535f4)
[![Discord](https://img.shields.io/discord/436949335947870238.svg?style=flat&logo=discord&label=chat&colorB=7389DC&link=https://discord.gg/vB7jUbY)](https://discord.gg/vB7jUbY)

PureVN is a mod to *optionally* eliminate all non-visual novel elements in Sunrider Academy for a nice, smooth, non-carpal-tunnel-inducing story.

<p align="center"><img alt="Sunrider Academy PureVN Mod Logo" src="preview/purevn_logo.png"></p>

When starting a new game PureVN will ask you if you want to enabled **PureVN Mode** just before choosing your character class. In any other scenario, PureVN Mode can be enabled mid-game in the console with `purevn = True` and optionally `purevn_choice_outcome = True`.

**Choice Outcome** allows the player to choose the outcome of Competitions, which allows the user more flexibility with story dialogue.

PureVN *should not* interfere with gameplay when **PureVN Mode** is disabled. If gameplay while PureVN Mode is disabled is different in anyway, then please report it in the issues section.

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

* **Common Route:** `bugfixes required`
* ![Ava Arc](preview/ava_small_24.png) **Ava Route:** `testing required`
* ![Asaga Arc](preview/asaga_small_24.png) **Asaga Route:** `finished`
* ![Chigara Arc](preview/chigara_small_24.png) **Chigara Route:** `testing required`
* ![Sola Arc](preview/sola_small_24.png) **Sola Route:** `testing required`

Auto-Activity is performed in the following 3 files:

* `purevn_choose_lunch.rpy`
* `purevn_choose_club.rpy`
* `purevn_choose_afterschool.rpy`

<!--### **Common Route:** `almost done`

### **Heroine Arcs:** `not started`

![Sola Arc](preview/sola_small.png) ![Chigara Arc](preview/chigara_small.png) ![Asaga Arc](preview/asaga_small.png) ![Ava Arc](preview/ava_small.png)

* **Ava Route:** `not started`
* **Asaga Route:** `not started`
* **Chigara Route:** `not started`
* **Sola Route:** `not started`

### ![Ava Arc](preview/ava_small.png) **Ava Route:** `not started`

### ![Asaga Arc](preview/asaga_small.png) **Asaga Route:** `not started`

### ![Chigara Arc](preview/chigara_small.png) **Chigara Route:** `not started`

### ![Sola Arc](preview/sola_small.png) **Sola Route:** `not started`

### ![Ava Arc](preview/ava_small_24.png) **Ava Route:** `not started`

### ![Asaga Arc](preview/asaga_small_24.png) **Asaga Route:** `not started`

### ![Chigara Arc](preview/chigara_small_24.png) **Chigara Route:** `not started`

### ![Sola Arc](preview/sola_small_24.png) **Sola Route:** `not started`-->
