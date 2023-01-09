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
    }
  };