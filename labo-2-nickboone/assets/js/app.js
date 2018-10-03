
(function () {

  var app = {
    init: function () {
      this.config = {
        apiKey: "AIzaSyDPhZyvwbKXeO_tQp8ORq2Z9X-PDOOMPhU",
		authDomain: "labo-2-domotica-nickboone.firebaseapp.com",
		databaseURL: "https://labo-2-domotica-nickboone.firebaseio.com",
		projectId: "labo-2-domotica-nickboone",
		storageBucket: "labo-2-domotica-nickboone.appspot.com",
		messagingSenderId: "559498029023"
      };
      firebase.initializeApp(this.config);
      let database = firebase.database();
  }
  app.init();
})();
