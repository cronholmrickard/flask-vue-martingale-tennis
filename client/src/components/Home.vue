<template>
  <div class="background">
    <div class="container">

      <div class="row align-items-center">
        <div class="col-12 mx-auto">
          <div class="card">
            <div class="card-body">
              <h4 class="card-title">Martingale Demonstrator</h4>
              <h5 class="card-subtitle mb-2 text-muted">Tennis</h5>
              <p class="card-text">
              Considering a coin toss, the matringale betting strategy is designed for a game in
                  which the gambler wins their stake if a coin comes up heads and loses it if the
              coin comes up tails.
              The strategy has the gambler double their bet after every loss so that the first
              win would recover all previous losses plus win a profit equal to the original stake.
              As the gambler's wealth and available time jointly approach infinity, their
              probability of eventually flipping heads approaches 1, which makes the martingale
              betting strategy seem like a sure thing. However, the exponential growth of the
              bets eventually bankrupts its users due to finite bankrolls.
              </p>
              <p class="card-text">
              In this interactive exercise, we will explore the martingale strategy in the
              context of betting on tennis matches. Let's find out if you get bankrupted or
              break the bank. Serve whenever you are ready!
              </p>
              <button class="tennisball btn btn-primary" v-on:click="serve">Serve</button>
            </div>
          </div>
        </div>
      </div>

      <div :class="{ invisible: !playing}">
        <div class="row align-items-center">
          <div class="col-12 mx-auto">
            <div class="grid-container">
              <div class="card">
                <div class="card-body">
                  <div class="card-text">
                    <button class="tennisball btn btn-primary" v-on:click="wonBet">Won</button>
                  </div>
                </div>
              </div>
              <div class="card">
                <div class="card-body">
                  <div class="card-text">
                    <table class="large">
                      <tr>
                       <td style="font-weight:600">Bakroll:</td>
                       <td>${{ parseFloat(bankRoll).toFixed(2) }}</td>
                      </tr>
                      <tr>
                       <td style="font-weight:600">ROI:</td>
                       <td :class="roi < 0 ? 'redtext' : 'greentext'">
                         {{ parseFloat(roi).toFixed(1) }}%
                       </td>
                      </tr>
                      <tr>
                       <td style="font-weight:600">Won Bets:</td>
                       <td>{{ betsWon }}</td>
                      </tr>
                      <tr>
                       <td style="font-weight:600">Lost Bets:</td>
                       <td>{{ betsLost }}</td>
                      </tr>
                    </table>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>

import BetStatClass from '../classes/BetStatClass';

const betStat = new BetStatClass();

export default {
  data() {
    return {
      playing: false,
      bankRoll: '',
      roi: '',
      betsWon: '',
      betsLost: '',
    };
  },
  methods: {
    serve() {
      this.playing = true;
      betStat.reset();
      this.updateBetStat();
    },
    updateBetStat() {
      this.bankRoll = betStat.getBankRoll();
      this.roi = betStat.getRoi();
      this.betsWon = betStat.getWonBets();
      this.betsLost = betStat.getLostBets();
    },
    wonBet() {
      betStat.wonBet(10, 1.5);
      this.updateBetStat();
    },
  },
};
</script>

<style>

.invisible {
  visibility: hidden !important;
}

.row {
  margin: 10px;
  padding: 10px;
}

.tennisball {
  background-color: #dfff4f !important;
  border: 2px solid black !important;
  color: black !important;
  border-radius: 15px !important;
}

.card {
  background: white;
}

.card-text {
  text-align: left;
}

.background {
  background: url('../assets/tenniscourt.jpg') no-repeat center center / cover
}

.grid-container {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 50px;
}

.large {
  font-size: 125%;
}

.redtext {
  color: red !important;
}

.greentext {
  color: green !important;
}

</style>
