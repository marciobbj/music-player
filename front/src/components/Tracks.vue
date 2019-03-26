<template>
  <li class="track">
      <p>file.name</p>
      <audio controls preload="metadata">
        <source src="#" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
  </li>
</template>

<script>
export default {
  name: 'Tracks',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
