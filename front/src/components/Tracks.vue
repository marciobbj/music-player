<template>
    <tr>
        <div v-if="message" class="notification"><b>Now Playing:</b> {{message}}</div>
        <td>
            <p>{{name}}</p>
            <audio v-on:play="updateTrackList($event)" controls preload="metadata">
                <source :src="url" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </td>
    </tr>
</template>

<script>
    export default {
        name: 'Tracks',
        props: {
            name: String,
            url: String
        },
        watch: {
            message: {
                immediate: false,
                handler: 'popNotification'
            }
        },
        data: () => {
            return {
                message: false
            }
        },
        methods: {
            updateTrackList(userSelectedTrack) {
                const trackList = document.querySelectorAll("audio");

                // Notification trigger
                const trackPathArray = userSelectedTrack.target.currentSrc.split('/');
                this.changeMessage(trackPathArray);

                trackList.forEach(track => {
                    track !== userSelectedTrack.target ? track.pause() : {};
                });
            },

            changeMessage(a) {
                this.message = a[a.length - 1] //the last item of the path is the file name
            },

            popNotification() {
                setTimeout(() => {
                    this.message = false
                }, 3000)
            },
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="scss">
    td {
        display: flex;
        justify-content: space-between;
    }

    td audio {
        max-width: 250px;
    }

    .notification {
        align-content: center;
        animation: fade 3s linear;
        background: #2bbbad;
        border-radius: 2px;
        bottom: 5%;
        box-shadow: 5px 10px #eee;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 40px;
        opacity: 1;
        padding: 10px;
        position: absolute;
        right: 5%;
        width: 200px;
    }

    @keyframes fade {
        0%, 100% {
            opacity: 0
        }
        50% {
            opacity: 1
        }
    }

    @media (max-width: 520px) {
        td {
            align-content: center;
            flex-direction: column;
            justify-content: center;
        }

        td p {
            text-align: center;
        }

        td audio {
            min-width: 100%;
            max-width: 100%;
        }

        .notification {
            height: 50px;
            right: 0%;
            top: 5%;
            width: 100%;
        }
    }
</style>
