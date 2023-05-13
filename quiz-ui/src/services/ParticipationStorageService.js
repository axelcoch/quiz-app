export default {
  clear() {
    savePlayerName("");
    saveParticipationScore("0");
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem("participationScore");
  },
  saveToken(token) {
    window.localStorage.setItem("token", token);
  },
  getToken() {
    return window.localStorage.getItem("token");
  },
  deleteToken() {
    return window.localStorage.removeItem("token");
  },
};
