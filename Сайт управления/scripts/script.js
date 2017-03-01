$( document ).ready(function() {
    var config = {
      apiKey: "ubKwffbx7sQYIH2kLxlqASXqsasJwB8CfgZVgmBg",
      authDomain: "wio-link-trening.firebaseapp.com",
      databaseURL: "https://smarthomeksli.firebaseio.com",
      storageBucket: "smarthomeksli.appspot.com",
      messagingSenderId: "957928187761"
    };
    firebase.initializeApp(config);
 
    var userId = 'fdgs45634vku45v6';

    var arrayOfObjects = {
      device1: false,
      device2: false,
      device3: false,
      device4: false,
      device5: false,
      device6: false
    }

    firebase.database().ref(userId).on('value', function(snapshot) {
      var device;
      for(var i = 1 ; i < 7 ; i ++) {
        device = snapshot.val()['device' + i];
        arrayOfObjects['device' + i] = device;
        trigger(device, 'device' + i);
      }

      setJscolor('device6Color', snapshot.val());
    });

    $(".device").click( function() {
        firebase.database().ref('/' + userId + '/' + this.id).set(!arrayOfObjects[this.id]);
    });

    $( ".jscolor" ).change(function() {
      firebase.database().ref('/' + userId + '/' + this.id).set($(this).val());
    });

    function setJscolor(nameEl, arrayValues) {
      var elementColor = arrayValues[nameEl];
      $( ".jscolor" ).val(elementColor);
      $( ".jscolor" ).css('background-color', '#' + elementColor);
    }

    function trigger(isOn, elementId) {
        if (isOn === false) {
            $('#' + elementId + '').removeClass('btn-success');
            $('#' + elementId + '').addClass('btn-danger');
            $('#' + elementId + '').html('Включить');
        }
        else {
          $('#' + elementId + '').removeClass('btn-danger');
          $('#' + elementId + '').addClass('btn-success');
          $('#' + elementId + '').html('Выключить');
        }
    }
});
