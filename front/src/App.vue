<template>
    <div id="app">
        <header>
            <h1>Music Player</h1>
            <label for="file" class="waves-effect waves-light btn-large" style="cursor: pointer">
                Add Track!
                <input type="file" ref="file_input" id="file" @input="uploadTrack" hidden>
            </label>
        </header>
        <div class="container">
            <table class="highlight">
                <tbody>
                <Tracks
                        v-for="track in tracks"
                        :name="track.name"
                        :url="track.file"
                />
                </tbody>
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
                axios.get('/api/v1/tracks')
                    .then(response => {
                        if (response.data.length === 0) {
                            this.tracks = false;
                            return
                        }
                        this.tracks = response.data
                    })
            },
            uploadTrack() {
                let file = this.$refs.file_input.files[0];
                let formData = new FormData();
                const headers = {'Content-Type': 'application/json'};
                formData.append('name', file.name)
                formData.append('file', file)
                axios.post('/api/v1/tracks/', formData, {headers})
                    .then(response => this.getTracks())
                    .catch(error => console.error(error));
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
    header{
        margin: 5rem;
    }
    .container {
        max-height: 400px;
        overflow: scroll;
    }
    table {
        overflow-y: scroll;
        height: 100px;
    }
    @media (min-height: 520px){
        header{
            margin: 5rem 0rem;
        }
    }
</style>
