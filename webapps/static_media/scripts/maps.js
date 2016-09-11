var geocoder;
var map;
var initialised = false;
function map_initialize() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644);
    var myOptions = {
        zoom: 2,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    if(!map) {
        map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    }
    initialize = true;
}

function setAddress(address) {
    if(initialised == false) map_initialize();
    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map, 
                position: results[0].geometry.location
            });
        } else {
            alert("Geocode was not successful for the following reason: " + status);
        };
    });
}

function setLatLon(latitude, longitude) {
    if(initialised == false) map_initialize();
    var latlng = new google.maps.LatLng(latitude, longitude);
    map.setCenter(latlng);
    map.setZoom(15);
    var marker = new google.maps.Marker({
        map: map, 
        position: latlng });
}
