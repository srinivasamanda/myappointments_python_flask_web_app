$(document).ready(function(){
    $("#btnnew").click(function(){
         $("#btnnew").hide();
         $("#theDiv").show();
    });
    $("#btncancel").click(function(){
         $("#theDiv").hide();
         $("#btnnew").show();
    });
    $("#submit").submit(function(event){
    var string=$("#search-item").val()
    getAppointments(string)
    event.preventDefault();
    });
});


function getAppointments(string){
    $.ajax({
        url:'/search',
        data: {'search-id': string},
        type:'POST',
        success:function(data){
        show_appointments(data)
        },
        error:function(data){
        console.log(data);
        }
     });
};

function show_appointments(data)
     {
       $("#appointments_area").empty();
       var tableDataHtml = '<div class="container"><table class="table">';
       tableDataHtml += '<thead><tr><th>DATE</th><th>TIME</th><th>DESCRIPTION</th></tr></thead><tbody>';

       json = $.parseJSON(data);

	   for(var key in json)
         {
     	   if(json.hasOwnProperty(key))
     	 	 {
     	 	   tableDataHtml += '<tr><td>' + json[key]['date'] + ' </td><td>' + json[key]['time'] + ' </td><td>' + json[key]['description'] + ' </td></tr>';
     	 	 }
     	 }
       tableDataHtml += "</tbody></table></div>";
       $("#theDiv2").html(tableDataHtml);
      };
