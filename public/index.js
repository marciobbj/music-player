// Scripts
const trackList = document.querySelectorAll("audio");

const updateTrackList = selectedTrack => {
  trackList.forEach(track => {
    track !== selectedTrack ? track.pause() : {};
  });
};

trackList.forEach(audio => {
  audio.addEventListener("play", e => {
    updateTrackList(e.target);
  });
});
