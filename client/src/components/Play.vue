<template>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-12 mx-auto">
        <div class="card black-border border-radius-15">
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
            <button class="btn btn-primary" @click="serve">
              Serve
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="row align-items-center">
      <div class="col-12 mx-auto">
        <div class="grid-container grid-frame-2-1">
          <match :show="showMatch" :match="matchData"></match>
          <betstats :show="showRoi" :betData="betData"></betstats>
        </div>
      </div>
    </div>

    <div class="row align-items-center">
      <div class="col-12 mx-auto">
        <div class="grid-container grid-frame-1-2">
          <div :class="{ invisible: !showStat}">
            <div class="card black-border border-radius-15">
              <div class="card-body">
                <div class="card-text">
                  <h4 class="card-title" style="text-align: center;">Historical results</h4>
                  <reactive-pie-chart
                  :chart-data="pieData"
                  :options="pieOptions">
                  </reactive-pie-chart>
                </div>
              </div>
            </div>
          </div>
          <div :class="{ invisible: !showRoi}">
            <div class="card black-border border-radius-15" style="width: 100%;">
              <div class="card-body">
                <div class="card-text">
                  <reactive-line-chart
                  :chart-data="chartData"
                  :options="chartOptions">
                  </reactive-line-chart>
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

import axios from 'axios';
import Match from './Match.vue';
import Betstats from './Betstats.vue';
import BetStatClass from '../classes/BetStatClass';
import CurrentBet from '../classes/CurrentBet';
import ReactiveLineChart from '../classes/ReactiveLineChart';
import ReactivePieChart from '../classes/ReactivePieChart';

const nMatches = 50;
const apiUrl = process.env.VUE_APP_API_URL;
const betStat = new BetStatClass();

export default {
  name: 'Play',
  components: {
    Match,
    Betstats,
    ReactiveLineChart,
    ReactivePieChart,
  },
  data() {
    return {
      matches: [],
      matchData: null,
      counter: null,
      showRoi: false,
      showStat: false,
      showMatch: false,
      betData: {
      },
      betArray: [],
      bankRollArray: [],
      chartData: null,
      chartOptions: {
        legend: {
          display: false,
        },
        scales: {
          xAxes: [{
            scaleLabel: {
              labelString: 'Bets',
              fontSize: 22,
              display: true,
            },
          }],
          yAxes: [{
            scaleLabel: {
              labelString: 'Bankroll',
              fontSize: 22,
              display: true,
            },
            ticks: {
              suggestedMin: 0,
              precision: 0,
            },
          }],
        },
      },
      pieData: null,
      pieOptions: {
        cutoutPercentage: 50,
        rotation: Math.PI,
        legend: {
          display: true,
          labels: {
            fontSize: 16,
          },
        },
      },
    };
  },
  methods: {
    async serve() {
      this.counter = null;
      await this.getMatches(apiUrl, nMatches);
    },
    async getMatches(url, numMatches) {
      const path = 'matches?number=';
      await axios.get(url + path + numMatches)
        .then((res) => {
          this.matches = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    async getMatch(url) {
      const path = 'match?id=';
      await axios.get(url + path + this.matches[this.counter])
        .then((res) => {
          this.matchData = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    async handleBet(backed) {
      const wager = betStat.computeWager(backed.Odds);
      const currentBet = new CurrentBet(this.matches[this.counter], backed);
      await currentBet.determineWinner(apiUrl);
      const won = currentBet.getWon();
      if (won) {
        betStat.wonBet(wager, currentBet.backed.Odds);
      } else {
        betStat.lostBet(wager);
      }
      this.counter += 1;
    },
    async updateResultStats(url) {
      const path = 'results';
      let results = null;
      await axios.get(url + path)
        .then((res) => {
          results = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.createPieData(results);
    },
    async pushShowStat(roi) {
      await this.pushRoi(apiUrl, roi);
      await this.updateResultStats(apiUrl);
      this.showStat = true;
    },
    async pushRoi(url, roi) {
      const path = 'results?roi=';
      await axios.post(url + path + roi);
    },
    createPieData(roiData) {
      // create data for pie chart
      this.pieData = {
        labels: ['Bankrupt', 'Profit'],
        datasets: [{
          data: [roiData.negative, roiData.positive],
          backgroundColor: [
            'rgba(255, 0, 0, 1.0)',
            'rgba(0, 0, 255, 1.0)',
          ],
          borderColor: [
            'rgba(255, 255, 255, 1.0)',
            'rgba(255, 255, 255, 1.0)',
          ],
          borderWidth: 5,
        }],
      };
    },
  },
  watch: {
    matches() {
      // generate betStatClass instance
      betStat.reset();
      // show roi
      this.showRoi = true;
      // show matches
      this.showMatch = true;
      // hide stats
      this.showStat = false;
      // reset chart arrays
      this.betArray = [];
      this.bankRollArray = [];
      // reset counter
      this.counter = 0;
    },
    counter() {
      this.betData = betStat.getData();
      this.betArray.push(this.counter);
      this.bankRollArray.push(this.betData.bankRoll);
      switch (true) {
        case (this.counter === null):
          // might be a good idea to do stuff here?
          this.showMatch = false;
          break;
        case (this.counter >= nMatches):
          // no more matches
          this.showMatch = false;
          this.pushShowStat(this.betData.roi);
          break;
        case (this.betData.bankRoll < 0):
          // bankrupt
          this.showMatch = false;
          this.pushShowStat(this.betData.roi);
          break;
        default:
          // get next match
          this.getMatch(apiUrl);
      }
    },
    bankRollArray() {
      this.chartData = {
        labels: this.betArray,
        datasets: [
          {
            label: 'Bankroll',
            backgroundColor: 'transparent',
            lineTension: 0,
            borderWidth: 1,
            borderColor: '#0000FF',
            pointBackgroundColor: '#0000FF',
            data: this.bankRollArray,
          },
        ],
      };
    },
  },
};

</script>

<style scoped>

.grid-container {
  display: grid;
  grid-gap: 50px;
  align-items: flex-start;
}

.grid-frame-1-2 {
  grid-template-columns: 1fr 2fr;
}

.grid-frame-2-1 {
  grid-template-columns: 2fr 1fr;
}

</style>
