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
            <tr v-for="player in playerOrder" v-bind:key="player">
              <td v-if="match !== null">
                {{ match[player]["Name"] }}
              </td>
              <td v-if="match !== null">
                {{ match[player]["Rank"] }}
              </td>
              <td class="td-right">
                <button
                class="btn btn-primary"
                v-if="match !== null"
                v-on:click="handleBet(match[player])">
                    {{ parseFloat(match[player]["Odds"]).toFixed(2) }}
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
      playerOrder: [
        'Home',
        'Away',
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

</style>
