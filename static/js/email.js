$(document).ready(function() {
    (function(){
        emailjs.init("user_Hzd5JUsmtAfzPF0OFPYyt");
    })();
});

window.setInterval(function(){
  getUpdates();
}, 5000);


function sendMail(msg) {
    emailjs.send("gmail", "nba_emal", {
        "message": msg
    })
    .then(function(response){
        console.log("success", response);
    })
}

function getUpdates() {
    console.log("getting updates");
    $.ajax({
        url: "/process_get_updates",
        success: function(res){
            if (res["updates"] != null) {
                var i;
                for (i=0; i < res["updates"].length; i++) {
                    sendMail(res["updates"][i]);
                }
            }
        }
    });
}
