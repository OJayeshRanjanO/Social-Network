function login(){
    var formData = $('#loginForm').serialize();
    formData = toJSON(formData);
    $.ajax({
      type: "POST",
      url: "/login",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        data = $.parseJSON(JSON.stringify(data));
        if (data.login === "failure"){
                alert(data.login);
            $("#loginContainer").append("<div style='color:red'> Incorrect username or password </div>")
        }
    });
}

function signUp(){
    var formData = $('#signUpForm').serialize();
    formData = toJSON(formData);
    $.ajax({
      type: "POST",
      url: "/signUp",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        data = $.parseJSON(JSON.stringify(data));
        alert(data.signup);
    });


}

function toJSON(data){
  data = data.split("&");
  var obj={};
    for(i = 0; i < data.length; i++)
    {
        var x = data[i].split("=");
        obj[x[0]] = x[1];
    }
  return JSON.stringify(obj);
}