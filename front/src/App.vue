<template>
  <div id="app">
    <h1 class="title">Music Player</h1>
      <h2 class="subtitle">Make your playlist!!!</h2>
      <div class="container">
          <ul style="padding: 0;">
              <Tracks></Tracks>
          </ul>
      </div>
  </div>
</template>

<script>
import Tracks from './components/Tracks.vue'

export default {
  name: 'app',
  components: {
    Tracks
  },
  data: () => {
    return {
    }
  },
  methods: {

  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px auto;
}

</style>
