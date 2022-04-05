import axios from 'axios';

export default class CurrentBet {
    #matchid = null;

    #winner = null;

    #backed = null;

    #won = null;

    constructor(matchid, backed) {
      this.matchid = matchid;
      this.backed = backed;
    }

    getWon() {
      return this.won;
    }

    async determineWinner(url) {
      const path = 'winner?id=';
      await axios.get(url + path + this.matchid)
        .then((res) => {
          this.winner = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      if (this.winner.Name === this.backed.Name) {
        this.won = true;
      } else {
        this.won = false;
      }
    }
}
