//use to receive the info submitted on the form in my personal email using EmailJS API

function sendForm(contactform) {
    emailjs.send("service_zbsju9a", "topdevelopmenttemplate", {
      "from_name": contactform.name.value,
      "from_email": contactform.email.value,
      "message": contactform.comments.value
    })
      //if the information is succesfully submited an alert will be displayed 
      .then(
        function (response) {
          console.log("form succesfully submited", response);
          alert('Thank you for contacting us, we will get back to you soon!');
          window.location.href="https://8080-jade-hawk-h4llo5iu.ws-eu08.gitpod.io/";
        },
        function (error) {
          console.log("Something weng wrong, please try again", error);
        },
    );
    return false; // To prevent a new page from loading
  }