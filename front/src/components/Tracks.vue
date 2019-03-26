<template>
  <li class="track">
      <p>{{name}}</p>
      <audio controls preload="metadata">
        <source :src="url" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
  </li>
</template>

<script>
export default {
  name: 'Tracks',
  props: {
    name: String,
    url: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
