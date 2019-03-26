<template>
  <div id="app">
    <h1 class="title">Music Player</h1>
      <h2 class="subtitle">Make your playlist!!!</h2>
      <div class="container">
          <ul style="list-style: none">
              <Tracks
                  v-for="track in tracks"
                  :name="track.name"
                  :url="track.file" />
          </ul>
      </div>
  </div>
</template>

<script>
import Tracks from './components/Tracks.vue'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    Tracks
  },
  data: () => {
    return {
      tracks: []
    }
  },
  mounted(){
    this.getTracks();
  },
  methods: {
    getTracks () {
      axios.get('/api/v1/tracks').then(response => {
        this.tracks = response.data
      })
    }
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
