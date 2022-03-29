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
              <button class="tennisball btn btn-primary" v-on:click="serve">
                Serve
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="row align-items-center">
          <div class="col-12 mx-auto">
          <div class="grid-container grid-frame-2-1">
              <div :class="{ invisible: !showMatch}">
                <div class="card">
                  <div class="card-body">
                    <div class="card-text">
                      <table v-if="match.Info !== undefined" style="width: 80%">
                        <tr>
                          <td v-for="item in infoOrder" v-bind:key="item">
                            {{ match.Info[item] }}
                          </td>
                        </tr>
                      </table>
                      <table class="large" style="width:100%">
                          <tr>
                            <th style="width:50%">Player</th>
                            <th>Ranking</th>
                            <th>Odds</th>
                          </tr>
                          <tr v-if="match.Home !== undefined">
                            <td style="vertical-align: middle">{{ match["Home"]["Name"] }}</td>
                            <td style="vertical-align: middle">{{ match["Home"]["Rank"] }}</td>
                            <td>
                              <button
                              class="btn btn-primary"
                              id="homeBtn"
                              v-if="match.Home !== undefined"
                              v-on:click="handleBet(match.Home)">
                              {{ parseFloat(match["Home"]["Odds"]).toFixed(2) }}
                              </button>
                            </td>
                          </tr>
                          <tr v-if="match.Away !== undefined">
                            <td style="vertical-align: middle">{{ match["Away"]["Name"] }}</td>
                            <td style="vertical-align: middle">{{ match["Away"]["Rank"] }}</td>
                            <td>
                              <button
                              class="btn btn-primary"
                              id="awayBtn"
                              v-if="match.Away !== undefined"
                              v-on:click="handleBet(match.Away)">
                              {{ parseFloat(match["Away"]["Odds"]).toFixed(2) }}
                              </button>
                            </td>
                          </tr>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
              <div :class="{ invisible: !showRoi}">
                <div class="card">
                  <div class="card-body">
                    <div class="card-text">
                      <table class="large">
                        <tr>
                          <td style="font-weight:600">Bakroll:</td>
                          <td class="td-right">${{ parseFloat(bankRoll).toFixed(2) }}</td>
                        </tr>
                        <tr>
                          <td style="font-weight:600">ROI:</td>
                          <td class="td-right"
                            :class="roi < 0 ? 'redtext' : 'greentext'">
                              {{ parseFloat(roi).toFixed(1) }}%
                          </td>
                        </tr>
                        <tr>
                          <td style="font-weight:600">Won Bets:</td>
                          <td class="td-right">{{ betsWon }}</td>
                        </tr>
                        <tr>
                          <td style="font-weight:600">Lost Bets:</td>
                          <td class="td-right">{{ betsLost }}</td>
                        </tr>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    <div class="row align-items-center">
      <div class="col-12 mx-auto">
        <div class="grid-container grid-frame-1-2">
          <div :class="{ invisible: !showStat}">
            <div class="card">
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
            <div class="card" style="width: 100%;">
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
  </div>
</template>
<script>

import axios from 'axios';
import BetStatClass from '../classes/BetStatClass';
import CurrentBet from '../classes/CurrentBet';
import ReactiveLineChart from '../classes/ReactiveLineChart';
import ReactivePieChart from '../classes/ReactivePieChart';

const betStat = new BetStatClass();
let counter = 0;
const nMatches = 50;
const apiUrl = 'http://10.0.1.100:5000/api/';

export default {
  components: {
    ReactiveLineChart,
    ReactivePieChart,
  },
  data() {
    return {
      infoOrder: [
        'Date',
        'Tournament',
        'Round',
        'Court',
        'Surface',
      ],
      showRoi: false,
      showMatch: false,
      showStat: false,
      matches: '',
      bankRoll: '',
      roi: '',
      betsWon: '',
      betsLost: '',
      match: '',
      betArray: [0],
      bankRollArray: [1000],
      pieData: null,
      pieOptions: {
        cutoutPercentage: 40,
      },
      chartData: null,
      chartOptions: {
        legend: {
          display: false,
        },
        scales: {
          xAxes: [{
            scaleLabel: {
              labelString: 'Bets',
              display: true,
            },
          }],
          yAxes: [{
            scaleLabel: {
              labelString: 'Bankroll',
              display: true,
            },
            ticks: {
              suggestedMin: 0,
              precision: 0,
            },
          }],
        },
      },
    };
  },
  methods: {
    createChartData() {
      this.betArray.push(counter);
      this.bankRollArray.push(this.bankRoll);
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
    createPieData(roiData) {
      // create data for pie chart
      this.pieData = {
        labels: ['Bankrpupcy', 'Wins'],
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
    async serve() {
      // reset counterv
      counter = 0;
      this.showRoi = true;
      this.showMatch = true;
      this.showStat = false;
      await this.getMatches(apiUrl, nMatches);
      betStat.reset();
      this.updateBetStat();
      this.chartData = null;
      this.betArray = [];
      this.bankRollArray = [];
      this.createChartData();
      await this.getMatch(apiUrl);
    },
    async handleBet(backed) {
      const wager = betStat.computeWager(backed.Odds);
      const currentBet = new CurrentBet(this.matches[counter], backed);
      await currentBet.determineWinner(apiUrl);
      if (currentBet.winner.Name === currentBet.backed.Name) {
        betStat.wonBet(wager, currentBet.backed.Odds);
      } else {
        betStat.lostBet(wager);
      }
      this.updateBetStat();
      // When everything is handled, update counter and get next
      counter += 1;
      this.createChartData();
      // check for bankrupcy
      if (betStat.BankRoll < 0) {
        this.showMatch = false;
        this.pushShowStat();
        return;
      }
      if (counter < this.matches.length) {
        await this.getMatch(apiUrl);
      } else {
        // no more matches
        this.showMatch = false;
        await this.pushShowStat();
      }
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
      await axios.get(url + path + this.matches[counter])
        .then((res) => {
          this.match = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
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
    async pushShowStat() {
      await this.pushRoi(apiUrl);
      await this.updateResultStats(apiUrl);
      this.showStat = true;
    },
    async pushRoi(url) {
      const path = 'results?roi=';
      await axios.post(url + path + this.roi);
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
  border: 2px solid black !important;
  border-radius: 15px !important;
}

.card-text {
  text-align: left;
}

.background {
  background: url('../assets/tenniscourt.jpg') no-repeat center center / cover
}

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

.large {
  font-size: 125%;
  margin: 0px;
  width: 100%;
}

.td-right {
  text-align: right;
}

.redtext {
  color: red !important;
}

.greentext {
  color: green !important;
}

#homeBtn, #awayBtn{
  background-color: #d37969 !important;
  border: 2px solid black !important;
  color: black !important;
  border-radius: 15px !important;
}

</style>
