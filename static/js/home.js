
function toJSON(data){
  data = data.split("&");
  var obj={};
    for(i = 0; i < data.length; i++)
    {
        var x = data[i].split("=");
        obj[x[0]] = x[1];
    }
  obj['username'] = localStorage['username']
  return JSON.stringify(obj);
}

function loadPage(){
    var username = JSON.stringify({"username":localStorage.getItem("username")});
    $.ajax({
      type: "POST",
      url: "/loadPage",
      data: username,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        data = $.parseJSON(JSON.stringify(data))
        appendGroups(data.circle);
    });

}

function appendGroups(array){
    for (i = 0; i < array.length; i++){
        $("#circle-list").append('<li id=circle-access-'+array[i].circleid+' class="list-group-item circle-item"><div class=circle-item-text>'+array[i].circle_name+'</div><a onclick="deleteCircle(this.id)"; id=circle-remove-'+array[i].circleid+' class="circle-icons"><span class="glyphicon glyphicon-minus-sign"></span></a></li>')
    }
}