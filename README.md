# Boxcar
### 7.16.2020
### Gavin Ray, Galvanize DS-RFT4 Capstone One


While play styles, techniques, and theory is well documented for popular games like chess, the simple yet elegant game of Boxcar is still widely unknown. This  Boxcar Simulator is able to define a standard of evaluation for the game in order to help player improve their scores. It utilizes several simple Virtual Players (VPs) that represent the most common play styles. By running through the simulation, human players can compare themselves to the built in VPs, and gain insight into their own ability.

This readme is split into two phases. The first describes the simulation and how to it is used. The VPs are described in detail, and an analysis of their abilities is provided. Standards for testing have also been set. The second phase gives an example of one player who benefited from using this simulation. For more information on the calculation used, please see the Jupyter Notebook located in the directory labeled 'eda'. 

## Phase One:

### Virtual Players (vp)
In this game, players are repeatedly given one choice--roll or stay? To make this decision, the player mainly looks at how many dice will be used if rolling, and how many points will be made if staying. I’ve also added a third player that emulates ineffective human behavior as a control.

- Perfect: This VP always rolls, and is evaluated without a loss condition. It represents the scores of a person who can tell the future, and therefore knows exactly when to stop rolling. For our purposes, it represents the upper boundary of what is possible even though it's performance is impossible to replicate without cheating.
- Wyatte: This VP represents players who are only concerned with dice probabilities. Because it is less than probable to score with 2 or less dice, this VP will always stop rolling when it has only 2 dice available. Likewise, it will keep rolling when it has 3 or more dice available.
- Karen: For this VP, only score is considered. There is a popular belief in Boxcar communities that one should always roll with less than 350 points, but never when over 1000. This VP follows this ancient wisdom. When the score is between these two points, it follows the same logic as Wyatte.
- Judy: The most sophisticated VP, Judy uses 6 different algorithms. 
- Random: Just like it sounds, this VP chooses randomly whether to roll or stay. It is intended as a lower boundary benchmark. If you can't beat the random VP, you should probably move on to a different game. 


## Milestones
1. Intermediate Stage (Perfect VP)

    Initial comparisons will be made between the VPs and the Perfect Model. Because my goal is to become as good as the Perfect Model, each VP will be evaluated in terms of: how likely is it that their results could have been derived from the Perfect Model distribution. This stage will be met when I have completed data analysis and created several graphs of the comparisons. This will provide me enough material to present on Friday should I run out of time.

2. Advanced Stage (Human Player)

    To further the impact of this study, I will need a way to incorporate my own skills on the same level of the VPs. This can be done via a terminal interface. Because I will not be able to play thousands of games like the VPs, my data will have to be bootstrapped before analysed. Once done, I will be able to compare my results to those of the VPs in order to determine if I should be incorporating more of one playing style or another.

3. Future Stage (Develop The Perfect Play Style)

    I might eventually want to code a sophisticated VP that can take my place at the Dice Masters world championships, as games between high ranking players and AI have become increasingly popular. I do not yet know how to do this, but am very excited to learn! 

