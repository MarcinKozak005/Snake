# Snake - the game

A simple snake game created using [PyGame](www.pygame.org) library.
Basic concept was taken from [sentdex YouTube tutorial](https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=1)

### Rework
The game was created between December and January 2017

In March 2019 it underwent a rework. Redundant code was put into functions, unnecessary commends were deleted and one big file was split into several smaller ones.

Unfortunately some parts are too tightly coupled to be easily separated so the rework is not perfect :confused:

### Game menu structure
* Play (_pol. Graj_) - select game mode and skins
    * Classic (_pol. Klasyczny_)
        * one fruit ![fruit](graphics/fruit1.png)![fruit](graphics/fruit2.png)![fruit](graphics/fruit3.png)![fruit](graphics/fruit4.png)
        * one snake ![snake](graphics/head1.png)
        * **Don't hit yourself or the edge!**
    * Extended (_pol. Rozszerzony_)
        * three fruit ![fruit](graphics/fruit1.png)![fruit](graphics/fruit2.png)![fruit](graphics/fruit3.png)![fruit](graphics/fruit4.png)
        * one snake ![snake](graphics/head1.png)
        * one obstacle ![obstacle](graphics/obstacle.png)
        * three power-ups ![powerUp](graphics/speed.png)![powerUp](graphics/bonus.png)![powerUp](graphics/shift.png)
        * **Don't hit yourself or the edge!**
    * Global
        * As in the Extended game mode, but edge is no longer game over condition:smile:
    * Multiplayer (_pol. Dla dwóch graczy_)
        * three fruit ![fruit](graphics/fruit1.png)![fruit](graphics/fruit2.png)![fruit](graphics/fruit3.png)![fruit](graphics/fruit4.png)
        * two **local** players ![snake](graphics/head1.png) ![snake](graphics/head2.png)
        * **Don't hit yourself or the edge or the other player**
        * **Get more points than your opponent**
    * Select the skin (_pol. Wybór skina_)
    * Back (_pol. Powrót_)
    
* Rules and Controls (_pol. Zasady i sterowanie_)
    * Player1: WSAD
    * Player2: :arrow_up::arrow_down::arrow_left::arrow_right:
* Exit (_pol. Wyjście_)

After game over You can play again (_pol. Jeszcze raz!_)
