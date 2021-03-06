jQuery(window).ready(function(){  
    /*jQuery("#btnInit").click(initiate_geolocation);  */
    initiate_geolocation();
});  

function initiate_geolocation() {  
  if (navigator.geolocation)  
  {  
      navigator.geolocation.getCurrentPosition(handle_geolocation_query_dynamic_map, handle_errors);  
  }  
  else  
  {  
      yqlgeo.get('visitor', normalize_yql_response);  
  }  
}

function handle_errors(error)  
{  
    switch(error.code)  
    {  
        case error.PERMISSION_DENIED: alert("user did not share geolocation data");  
        break;  

        case error.POSITION_UNAVAILABLE: alert("could not detect current position");  
        break;  

        case error.TIMEOUT: alert("retrieving position timed out");  
        break;  

        default: alert("unknown error");  
        break;  
    }  
}

function normalize_yql_response(response)  {  
  if (response.error)  
  {  
      var error = { code : 0 };  
      handle_error(error);  
      return;  
  }  

  var position = {  
      coords :  
      {  
          latitude: response.place.centroid.latitude,  
          longitude: response.place.centroid.longitude  
      },  
      address :  
      {  
          city: response.place.locality2.content,  
          region: response.place.admin1.content,  
          country: response.place.country.content  
      }  
};  

handle_geolocation_query_dynamic_map(position);  
}
  
function handle_geolocation_query_dynamic_map(position){  
    alert('Lat: ' + position.coords.latitude + ' ' +  
          'Lon: ' + position.coords.longitude);
    setLatLon(position.coords.latitude, position.coords.longitude);	    
}

function handle_geolocation_query_static_map(position)  
{
    var image_url = "http://maps.google.com/maps/api/staticmap?sensor=false&center=" + position.coords.latitude + "," +  
                    position.coords.longitude + "&zoom=15&size=2000x2000&markers=color:blue|label:S|" +  
                    position.coords.latitude + ',' + position.coords.longitude;  
  
    jQuery("#map").remove();  
    jQuery(document.body).append(  
        jQuery(document.createElement("img")).attr("src", image_url).attr('id','map')  
    );  
}
