function OpenROV(options) {
  this.infowindow = null;
  this.map_icon = options.map_icon || new google.maps.MarkerImage(options.static_url + 'openrov/images/openrov_marker.png',
    new google.maps.Size(79, 79),
    new google.maps.Point(0, 0),
    new google.maps.Point(0, 0),
    new google.maps.Size(32, 32));
  this.map_id = options.map_id || 'map_canvas';
  this.map_options = options.map_options || {
    mapTypeId: google.maps.MapTypeId.TERRAIN,
    maxZoom: 18
  };
  this.marker_info = options.marker_info || [];
  this.markers = [];
  this.map_shadow = options.map_shadow || new google.maps.MarkerImage(options.static_url + 'openrov/images/openrov_shadow.png',
    new google.maps.Size(119, 79),
    new google.maps.Point(0, 0),
    new google.maps.Point(0, 0),
    new google.maps.Size(48, 32));
  this.map = options.map || new google.maps.Map(document.getElementById(this.map_id), this.map_options);
}

OpenROV.prototype.initialize = function() {
  var bounds = new google.maps.LatLngBounds();
  
  for (i in this.marker_info) {
    (function (instance, i) {
      var lat_lng = new google.maps.LatLng(instance.marker_info[i].lat, instance.marker_info[i].lng);
      var marker = new google.maps.Marker({
        icon: instance.map_icon,
        map: instance.map,
        position: lat_lng,
        shadow: instance.map_shadow,
        title: instance.marker_info[i].title
      });
      instance.markers.push(marker);
      google.maps.event.addListener(marker, 'click', function() {
        // Close any open infowindow
        if (instance.infowindow) {
          instance.infowindow.close();
        }
        instance.infowindow = new google.maps.InfoWindow({
          content: instance.marker_info[i].infowindow
        });
        instance.infowindow.open(instance.map, this);
      });
      bounds.extend(lat_lng);
      instance.map.fitBounds(bounds);
    })(this, i);
  }
};

OpenROV.prototype.addMarker = function(marker_info) {
  this.marker_info.push(marker_info);
}

function MarkerInfo(options) {
  this.infowindow = options.infowindow;
  this.lat = options.lat;
  this.lng = options.lng;
  this.title = options.title;
};