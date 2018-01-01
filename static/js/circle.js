function createCircle(){
    var formData = $('#createCircleForm').serialize();
    formData = toJSON(formData);
    $.ajax({
      type: "POST",
      url: "/createCircle",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        data = $.parseJSON(JSON.stringify(data));
        $("#circle-list").append('<li id=circle-access-'+data.circleid+' class="list-group-item circle-item"><div class=circle-item-text>'+data.circle_name+'</div><a onclick="deleteCircle(this.id)"; id=circle-remove-'+data.circleid+' class="circle-icons"><span class="glyphicon glyphicon-minus-sign"></span></a></li>')

    }).fail(function (jqXHR, textStatus) {
            alert(jqXHR)
    });
}

function deleteCircle(id){
    circleid = parseInt(id.charAt(id.length-1));
    formData = {'circleid':circleid,'username':localStorage['username']}
    $.ajax({
      type: "POST",
      url: "/deleteCircle",
      data: JSON.stringify(formData),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        console.log(data)
        console.log(id)
        $("#circle-access-"+circleid).remove();

    }).fail(function (jqXHR, textStatus) {
            alert(jqXHR)
    });

}