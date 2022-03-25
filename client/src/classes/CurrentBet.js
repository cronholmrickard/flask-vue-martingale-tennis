import axios from 'axios';

export default class CurrentBet {
    matchid = null;

    winner = null;

    backed = null;

    constructor(matchid, backed) {
      this.matchid = matchid;
      this.backed = backed;
    }

    async getWinner() {
      const path = 'http://172.17.0.1:5000/api/winner?id=';
      await axios.get(path + this.matchid)
        .then((res) => {
          this.winner = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
}
