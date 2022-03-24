<template>
  <div>
    <div class="match">
      <div class="grid-container">
        <div class="player">
          &#91; {{ match["Home"]["Rank"] }} &#93; {{ match["Home"]["Name"] }}
        </div>
        <button type="button" class="odds">
          {{ match["Home"]["Odds"] }}
        </button>
      </div>
      <div class="grid-container">
        <div class="player">
          &#91; {{ match["Away"]["Rank"] }} &#93; {{ match["Away"]["Name"] }}
        </div>
        <button type="button" class="odds">
        {{ match["Away"]["Odds"] }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Match',
  data() {
    return {
      match: '',
    };
  },
  methods: {
    getMatch() {
      const matchid = this.$route.query.id;
      const path = 'http://172.17.0.1:5000/api/match?id=';
      axios.get(path + matchid)
        .then((res) => {
          this.match = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMatch();
  },
};

</script>

<style>

.match {
  width: 300px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: solid black;
  font-weight: 600;
  background-color: white;
  border: 2px solid black;
  padding: 2px;
  margin: 2px;
  overflow: hidden;
  border-radius: 5px;
}

.grid-container {
    display: grid;
    grid-template-columns: 3fr 1fr;
    grid-gap: 0px;
}

.player {
  text-align: left;
  height: 25px;
  margin: 5px 2px;
}

.odds {
  background-color: coral;
  border: 2px solid black;
  color: solid black;
  font-weight: 600;
  padding: 2px;
  text-align: right;
  text-decoration: none;
  display: inline-block;
  margin: 2px;
  cursor: pointer;
  border-radius: 5px;
}
</style>
