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
              <button class="tennisball btn btn-primary" v-on:click="start">Serve</button>
            </div>
          </div>
        </div>
      </div>

      <div :class="{ invisible: !showROI}">
        <div class="row align-items-center">
          <div class="col-12 mx-auto">
            <div class="card">
              <div class="card-body">
                <p class="card-text">
                  Lots of text here
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showROI: false,
    };
  },
  methods: {
    start() {
      this.showROI = !this.showROI;
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

</style>
