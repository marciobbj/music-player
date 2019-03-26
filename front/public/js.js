// Cuida da reproduçao dos audios
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

// Cuida do clique nas divs dos audios
const trackDivs = document.querySelectorAll(".track");

trackDivs.forEach(div => {
  div.addEventListener("click", e => {
    let track = div.querySelector("audio");
    track.play();
  });
});