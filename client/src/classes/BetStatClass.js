export default class BetStatClass {
    StartFund = 1000;

    BankRoll = 1000;

    Roi = null;

    WonBets = 0;

    LostBets = 0;

    AttemptedWinning = 50;

    AccumulatedWager = 0;

    computeRoi() {
      this.Roi = (this.BankRoll - this.StartFund) / this.StartFund;
    }

    reset() {
      this.BankRoll = 1000;
      this.WonBets = 0;
      this.LostBets = 0;
      this.AccumulatedWager = 0;
      this.computeRoi();
    }

    getBankRoll() {
      return this.BankRoll;
    }

    getRoi() {
      // multiply by 100 to get percent
      return this.Roi * 100;
    }

    wonBet(wager, odds) {
      const winnings = wager * (odds - 1);
      this.WonBets += 1;
      this.AccumulatedWager = 0;
      this.BankRoll += winnings;
      this.computeRoi();
    }

    lostBet(wager) {
      this.LostBets += 1;
      this.AccumulatedWager += wager;
      this.BankRoll -= wager;
      this.computeRoi();
    }

    getWonBets() {
      return this.WonBets;
    }

    getLostBets() {
      return this.LostBets;
    }

    computeWager(odds) {
      return (this.AccumulatedWager + this.AttemptedWinning) / (odds - 1);
    }
}
