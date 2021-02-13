


var markers = []; 
var map=null;
class Map {
    static initMap() {
        map = new naver.maps.Map('naverMap', {
            center: new naver.maps.LatLng(37.3595704, 127.105399),
            zoom: 10
        });

        naver.maps.Event.addListener(map, 'zoom_changed', function () {
            updateMarkers(map, markers);
            console.log("zoom changed");
        });

        naver.maps.Event.addListener(map, 'dragend', function () {
            updateMarkers(map, markers);
            console.log("dragend");
        });
        
        var bounds = map.getBounds(),
            southWest = bounds.getSW(),
            northEast = bounds.getNE(),
            lngSpan = northEast.lng() - southWest.lng(),
            latSpan = northEast.lat() - southWest.lat();

        get_markers();
    }

    static change_map_center(latitude, longitude){
        var position = new naver.maps.LatLng(latitude,longitude);
        map.setCenter(position);
    }
    static make_marker(latitude,longitude){
        var position = new naver.maps.LatLng(latitude,longitude);
        var marker = new naver.maps.Marker({
            map: map,
            position: position
        });
        return marker
    }
    static get_markers() {
        $.get('/get_every_camping_locations', function (datas) {
            jsonData  = JSON.parse(datas);
            jsonData.forEach(function(data){
                console.log(data);
                
                //TODO : send ajax(maybe get?) to get review and informations
                //TODO : if user click the button in info window, send the info to the search text box
                var marker = make_marker(data["X_LOCATION"],data["Y_LOCATION"])
                infowindow = get_infowindow(data)
                naver.maps.Event.addListener(marker, "click", function(e) {
                    if (infowindow.getMap()) {
                        infowindow.close();
                    } else {
                        infowindow.open(map, marker);
                    }
                });
                naver.maps.Event.addListener(infowindow,'load',function(e){
                    document.querySelector()
                });
                // TODO : change icon according to the other factors. factors can be age , theme .. etc
                markers.push(marker);
            });
        });
    };

    static get_infowindow(data){
        var contentString = [
            '<div class="iw_inner">',
            '   <h3>'+data["CITY"]+'</h3>',
            '   <p>'+data["ROAD_ADDRESS"]+'<br>',
            '       <button id="view_detail_btn" onclick="load_modal()">detail</button>',
            '       <a href="nmap://navigation?lat=37.4979502&lng=127.0276368&zoom=20&appname=com.example.myapp">set destination</button>',
            '   </p>',
            '</div>'
        ].join('');
        var infowindow = new naver.maps.InfoWindow({
            content : contentString,
        });
        return infowindow;
    }

    static load_modal(){
        $("#myModal").modal();
    }

    static updateMarkers(map, markers) {
        var mapBounds = map.getBounds();
        var marker, position;
        for (var i = 0; i < markers.length; i++) {
            marker = markers[i]
            position = marker.getPosition();
            if (mapBounds.hasLatLng(position)) {
                showMarker(map, marker);
                console.log("appear");
            } else {
                hideMarker(map, marker);
                console.log("hidden");
            }
        }
    }

    static showMarker(map, marker) {
        if (marker.setMap()) return;
        marker.setMap(map);
    }

    static hideMarker(map, marker) {
        if (!marker.setMap()) return;
        marker.setMap(null);
    }

}export default Map;