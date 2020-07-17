## Capstone One


### 7.16.2020

**─**

Gavin Ray

Galvanize DS-RFT4


## Proposal

Attending the Dice Masters world championships would add huge cred to my pro-gaming portfolio. While I could probably get there with my skills as they currently stand, it would be much better for me to optimize my playing style to better ensure a rank of grand master. Simple training for this event is simply not enough. I also need a method of evaluation that defines a ‘perfect game’ distribution of outcomes to compare all other playstyles to.


## Goals



1. Optimize ‘Boxcar’, a virtual dice playing game in python, for use with multiple virtual players (VP) representing various playstyles.
2. Develop a ‘Perfect Game’ model by collecting scores from all playthroughs regardless of success. This will create the need for data manipulation at later stages, but will be well worth it.
3. Develop several other ‘Imperfect’ VPs that represent various human styles. These are outlined below.
4. Compare the VPs to find which is most likely to achieve perfect game scores. 


## Virtual Players (vp)

In this game, players are repeatedly given one choice--roll or stay? To make this decision, the player mainly looks at how many dice will be used if rolling, and how many points will be made if staying. I’ve also added a third player that emulates ineffective human behavior as a control.

- Wyatte: Evaluates decisions solely based on dice probabilities. 

- Karen: Disregards all parameters except current round score.

- Stan:**(control)** Will take more risks if recent rolls have been successful.

- (maybe a fourth with which returns random?)



## Milestones



1. Intermediate Stage (Perfect VP)

    Initial comparisons will be made between the VPs and the Perfect Model. Because my goal is to become as good as the Perfect Model, each VP will be evaluated in terms of: how likely is it that their results could have been derived from the Perfect Model distribution. This stage will be met when I have completed data analysis and created several graphs of the comparisons. This will provide me enough material to present on Friday should I run out of time.

2. Advanced Stage (Human Player)

    To further the impact of this study, I will need a way to incorporate my own skills on the same level of the VPs. This can be done via a terminal interface. Because I will not be able to play thousands of games like the VPs, my data will have to be bootstrapped before analysed. Once done, I will be able to compare my results to those of the VPs in order to determine if I should be incorporating more of one playing style or another.

3. Future Stage (Develop The Perfect Play Style)

    I might eventually want to code a sophisticated VP that can take my place at the Dice Masters world championships, as games between high ranking players and AI have become increasingly popular. I do not yet know how to do this, but am very excited to learn! 

