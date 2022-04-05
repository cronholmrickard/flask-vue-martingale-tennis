<template>
  <div :class="{ invisible: !show}">
    <div class="card black-border border-radius-15">
      <div class="card-body">
        <div class="card-text">
          <table style="width: 100%">
            <tr v-for="item in infoOrder" v-bind:key="item">
              <td>{{ item }}:</td>
              <td v-if="match !== null" class="td-right">
                {{ match.Info[item] }}
              </td>
            </tr>
          </table>
          <hr>
          <table class="large" style="width:100%">
            <tr>
              <th style="width:50%">Player</th>
              <th>Ranking</th>
              <th class="td-right" style="padding-right: 5px;">Odds</th>
            </tr>
            <tr>
              <td v-if="match !== null" style="vertical-align: middle">
                {{ match["Home"]["Name"] }}
              </td>
              <td v-if="match !== null" style="vertical-align: middle">
                {{ match["Home"]["Rank"] }}
              </td>
              <td class="td-right">
                <button
                class="btn btn-primary"
                id="homeBtn"
                v-if="match !== null"
                v-on:click="handleBet(match.Home)">
                    {{ parseFloat(match["Home"]["Odds"]).toFixed(2) }}
                </button>
              </td>
            </tr>
            <tr>
              <td v-if="match !== null" style="vertical-align: middle">
                {{ match["Away"]["Name"] }}
              </td>
              <td v-if="match !== null" style="vertical-align: middle">
                {{ match["Away"]["Rank"] }}
              </td>
              <td class="td-right">
                <button
                class="btn btn-primary"
                id="awayBtn"
                v-if="match !== null"
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
</template>

<script>

export default {
  name: 'Match',
  props: {
    show: Boolean,
    match: Object,
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
    };
  },
  methods: {
    handleBet(backed) {
      this.$parent.handleBet(backed);
    },
  },
};

</script>

<style scoped>

#homeBtn, #awayBtn{
  background-color: #d37969 !important;
  border: 2px solid black !important;
  color: black !important;
  border-radius: 15px !important;
}

</style>
