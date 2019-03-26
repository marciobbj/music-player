<template>
    <div id="app">
        <header>
            <h1>Music Player</h1>
            <a class="waves-effect waves-light btn-large">Add Song</a>
        </header>
        <div class="container">
            <table class="highlight">
                <Tracks
                        v-for="track in tracks"
                        :name="track.name"
                        :url="track.file"
                />
            </table>
        </div>
    </div>
</template>

<script>
    import Tracks from './components/Tracks.vue'
    import axios from 'axios'

    export default {
        name: 'app',
        components: {
            Tracks,
        },
        data: () => {
            return {
                tracks: false,
            }
        },
        mounted() {
            this.getTracks()
        },
        methods: {
            getTracks() {
                axios.get('/api/v1/tracks').then(response => {
                    if (response.data.length === 0) {
                        this.tracks = false
                        return
                    }
                    this.tracks = response.data
                })
            },
        },
    }
</script>

<style>
    #app {
        color: #2c3e50;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
    }

    table {
        overflow: auto;
        max-height: 400px;
    }
</style>
