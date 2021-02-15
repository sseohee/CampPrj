async function get_my_location() {
  var location_text = document.querySelector("#start_position_text").text;
  var startPos;
  var geoSuccess = function (position) {
    startPos = position;
    var lat = startPos.coords.latitude;
    var lon = startPos.coords.longitude;
    var start_posi_marker = make_marker(lat, lon);
    console.log(ax_to_address(lat, lon));
    markers.push(start_posi_marker);
    showMarker(map, start_posi_marker);
    change_map_center(lat, lon);
  };
  navigator.geolocation.getCurrentPosition(geoSuccess);
}

function show_candidated_list(places){
  var candidated_list_container = document.querySelector("#candidated_list");
  places.forEach(element => {
    var li = document.createElement("li");
    var text_value = document.createTextNode(element);
    li.appendChild(text_value);
  });
}

function select_city() {
  var sido = document.querySelector("#sido").value;
  var gu = document.querySelector("#gugun").value;
  var result;
  $.ajax({
    url: "/search",
    type: "GET",
    async: true,
    data: {
      "sido": sido,
      "gu": gu,
    },
    success: function (data) {
      show_candidated_list(data);
      alert(data);
    },
    error: function (e) {
      alert("값을 가져오지 못했습니다.");
      print(e);
    }
  });
}

function show_ranking(){
  var ranking_container = document.querySelector("#ranking_container");
  $.get('/ranking',function (data) {
    console.log(data);
    console.log("he");
    ranking_container.innerHTML = data;
  });
}
// search function 
function search() {
  var dest_position = document.querySelector("#dest_position_text").value;
  if (!dest_position) {
    alert("please fill the blank below");
  }
  else {
    $.get('/search', { 'destination': dest_position }, function (data) {
      if (!data) {
        alert("there is no data!")
      }
      else {
        console.log(data);
      }
    });
  }
}

var get_my_location_btn = document.querySelector("#get_my_location_btn");
get_my_location_btn.addEventListener("click", get_my_location);
var search_location_btn = document.querySelector("#city_selection_btn")
search_location_btn.addEventListener("click", select_city);
var get_destination_btn = document.querySelector("#set_destination_btn");
get_destination_btn.addEventListener("click", search);
var rankings = document.querySelector("#ranking_container");
rankings.onload = show_ranking();
function edit_modal() {
  $.ajax({
    url: '/search',
    data: {
      id: $(elm).attr('data-id')
    },
    type: 'POST',
    success: function (res) {
      console.log(res);
    },
    error: function (error) {
      console.log(error);
    }
  });
}