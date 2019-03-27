<template>
    <tr>
        <div v-if="message" class="notification"><b>Now Playing:</b> {{message}}</div>
        <td @click="rowClickHandler($event.target)">
            <p>{{name}}</p>
            <audio v-on:play="updateTrackList($event)" controls preload="metadata">
                <source :src="url" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            <button class="btn" v-if="showDelete" @click="$emit('deleteTrack')">Delete</button>
        </td>
    </tr>
</template>

<script>
    export default {
        name: 'Tracks',
        props: {
            name: String,
            url: String,
            id: Number,
        },
        watch: {
            message: {
                immediate: false,
                handler: 'popNotification'
            }
        },
        data: () => {
            return {
                message: false,
                showDelete: false,
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
                this.message = a[a.length - 1]; //the last item of the path is the file name
            },

            popNotification() {
                setTimeout(() => {
                    this.message = false;
                }, 3000)
            },
            rowClickHandler(row) {
                this.showDelete = !this.showDelete;
            },
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="scss">
    td {
        display: flex;
        justify-content: space-between;
        text-align: center;
        cursor: pointer;
    }

    td p {
        width: 90px;
    }

    td audio {
        max-width: 250px;
        height: 40px;
        margin: auto 0;
    }

    .btn {
        background: red;
        margin: auto 0;
    }

    .notification {
        align-content: center;
        animation: fade 3s linear;
        background: #2bbbad;
        border-radius: 2px;
        bottom: 3%;
        box-shadow: 5px 10px #eee;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 40px;
        opacity: 1;
        padding: 5px;
        position: fixed;
        right: 1%;
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
            width: 100%;
        }

        td audio {
            min-width: 100%;
            max-width: 100%;
        }

        .notification {
            position: fixed;
            height: 50px;
            right: 0%;
            top: 5%;
            width: 100%;
        }

        .btn {
            margin: 10px 0;
        }
    }
</style>
