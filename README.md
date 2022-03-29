# flask-vue-martingale-tennis
Martingale demonstration in the context of tennis betting using flask, vue and mongodb

## Martingale betting strategy
Considering a coin toss, the matringale betting strategy is designed for a game in which the gambler wins their stake if a coin comes up heads and loses it if the coin comes up tails. The strategy has the gambler double their bet after every loss so that the first win would recover all previous losses plus win a profit equal to the original stake. As the gambler's wealth and available time jointly approach infinity, their probability of eventually flipping heads approaches 1, which makes the martingale betting strategy seem like a sure thing. However, the exponential growth of the bets eventually bankrupts its users due to finite bankrolls.
See the [wikipage](https://en.wikipedia.org/wiki/Martingale_(probability_theory))

## Running the application
The application stack can be run locally through;
`docker-compose up -d`

When run locally, the application can be accessed at [localhost](http://localhost).

## Instructions
The application is an interactive experience, where the user places bets on tennis matches. Bets are placed by clicking the odds of the preferred player. Note that in tennis, lower ranking is better.
![Screenshot](https://raw.githubusercontent.com/cronholmrickard/flask-vue-martingale-tennis/main/screenshots/place_bet.png)

At the end of a game (either after 50 bets or earlier if you get bankrupted), the historical distribution of bankrupcies/wins will be displayed.

### Development log
- __2021-03-28__: First fully functional version pushed.
