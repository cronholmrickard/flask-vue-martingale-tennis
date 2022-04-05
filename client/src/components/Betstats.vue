<template>
  <div :class="{ invisible: !show}">
    <div class="card black-border border-radius-15">
      <div class="card-body">
        <div class="card-text">
          <table class="large">
            <tr>
              <td style="font-weight:600">Bankroll:</td>
              <td class="td-right">${{ parseFloat(betData.bankRoll).toFixed(2) }}</td>
            </tr>
            <tr>
              <td style="font-weight:600">ROI:</td>
              <td class="td-right" :class="betData.roi < 0 ? 'redtext' : 'greentext'">
                {{ parseFloat(betData.roi).toFixed(1) }}%
              </td>
            </tr>
            <tr>
              <td style="font-weight:600">Won Bets:</td>
              <td class="td-right">{{betData.won}}</td>
            </tr>
            <tr>
              <td style="font-weight:600">Lost Bets:</td>
              <td class="td-right">{{betData.lost}}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Betstats',
  props: {
    show: Boolean,
    betData: Object,
  },
  data() {
    return {
    };
  },
};

</script>

<style scoped>
.redtext {
  color: red !important;
}

.greentext {
  color: green !important;
}
</style>
