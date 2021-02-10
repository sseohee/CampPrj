<template>
  <div id="wrap" class="section">
    <div id="naverMap"></div>

    <!-- right searching bar -->

    <v-app-bar>
      <v-spacer />
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
      right
      width="25%"
    >
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-subheader>캠핑지 검색 </v-subheader>
          <v-row align="center">
            <v-select
              :items="regions"
              label="시/도"
              dense
              solo
              style="width:80%"
              name="sido1"
              id="sido"
            ></v-select>

            <v-select
              :items="cities"
              label="시/군/구"
              dense
              solo
              width="80%"
              name="gugun1"
              id="gugun"
            ></v-select>
            <v-btn outlined id="Search">검색</v-btn>
          </v-row>
          <v-row>
 <v-card
    tile
    style="width: 100%" 
  >
    <v-list rounded>
      <v-subheader>검색지 리스트</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="(list, i) in campingLists"
          :key="i"
        >
          <v-list-item-content>
            <v-title v-text="list.title"></v-title>
          </v-list-item-content>
        
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>

          </v-row>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>




  </div>
</template>


<script type="text/javascript">
$("document").ready(function () {
  var area0 = [
    "시/도 선택",
    "서울특별시",
    "인천광역시",
    "대전광역시",
    "광주광역시",
    "대구광역시",
    "울산광역시",
    "부산광역시",
    "경기도",
    "강원도",
    "충청북도",
    "충청남도",
    "전라북도",
    "전라남도",
    "경상북도",
    "경상남도",
    "제주도",
  ];
  var area1 = [
    "강남구",
    "강동구",
    "강북구",
    "강서구",
    "관악구",
    "광진구",
    "구로구",
    "금천구",
    "노원구",
    "도봉구",
    "동대문구",
    "동작구",
    "마포구",
    "서대문구",
    "서초구",
    "성동구",
    "성북구",
    "송파구",
    "양천구",
    "영등포구",
    "용산구",
    "은평구",
    "종로구",
    "중구",
    "중랑구",
  ];
  var area2 = [
    "계양구",
    "남구",
    "남동구",
    "동구",
    "부평구",
    "서구",
    "연수구",
    "중구",
    "강화군",
    "옹진군",
  ];
  var area3 = ["대덕구", "동구", "서구", "유성구", "중구"];
  var area4 = ["광산구", "남구", "동구", "북구", "서구"];
  var area5 = [
    "남구",
    "달서구",
    "동구",
    "북구",
    "서구",
    "수성구",
    "중구",
    "달성군",
  ];
  var area6 = ["남구", "동구", "북구", "중구", "울주군"];
  var area7 = [
    "강서구",
    "금정구",
    "남구",
    "동구",
    "동래구",
    "부산진구",
    "북구",
    "사상구",
    "사하구",
    "서구",
    "수영구",
    "연제구",
    "영도구",
    "중구",
    "해운대구",
    "기장군",
  ];
  var area8 = [
    "고양시",
    "과천시",
    "광명시",
    "광주시",
    "구리시",
    "군포시",
    "김포시",
    "남양주시",
    "동두천시",
    "부천시",
    "성남시",
    "수원시",
    "시흥시",
    "안산시",
    "안성시",
    "안양시",
    "양주시",
    "오산시",
    "용인시",
    "의왕시",
    "의정부시",
    "이천시",
    "파주시",
    "평택시",
    "포천시",
    "하남시",
    "화성시",
    "가평군",
    "양평군",
    "여주군",
    "연천군",
  ];
  var area9 = [
    "강릉시",
    "동해시",
    "삼척시",
    "속초시",
    "원주시",
    "춘천시",
    "태백시",
    "고성군",
    "양구군",
    "양양군",
    "영월군",
    "인제군",
    "정선군",
    "철원군",
    "평창군",
    "홍천군",
    "화천군",
    "횡성군",
  ];
  var area10 = [
    "제천시",
    "청주시",
    "충주시",
    "괴산군",
    "단양군",
    "보은군",
    "영동군",
    "옥천군",
    "음성군",
    "증평군",
    "진천군",
    "청원군",
  ];
  var area11 = [
    "계룡시",
    "공주시",
    "논산시",
    "보령시",
    "서산시",
    "아산시",
    "천안시",
    "금산군",
    "당진군",
    "부여군",
    "서천군",
    "연기군",
    "예산군",
    "청양군",
    "태안군",
    "홍성군",
  ];
  var area12 = [
    "군산시",
    "김제시",
    "남원시",
    "익산시",
    "전주시",
    "정읍시",
    "고창군",
    "무주군",
    "부안군",
    "순창군",
    "완주군",
    "임실군",
    "장수군",
    "진안군",
  ];
  var area13 = [
    "광양시",
    "나주시",
    "목포시",
    "순천시",
    "여수시",
    "강진군",
    "고흥군",
    "곡성군",
    "구례군",
    "담양군",
    "무안군",
    "보성군",
    "신안군",
    "영광군",
    "영암군",
    "완도군",
    "장성군",
    "장흥군",
    "진도군",
    "함평군",
    "해남군",
    "화순군",
  ];
  var area14 = [
    "경산시",
    "경주시",
    "구미시",
    "김천시",
    "문경시",
    "상주시",
    "안동시",
    "영주시",
    "영천시",
    "포항시",
    "고령군",
    "군위군",
    "봉화군",
    "성주군",
    "영덕군",
    "영양군",
    "예천군",
    "울릉군",
    "울진군",
    "의성군",
    "청도군",
    "청송군",
    "칠곡군",
  ];
  var area15 = [
    "거제시",
    "김해시",
    "마산시",
    "밀양시",
    "사천시",
    "양산시",
    "진주시",
    "진해시",
    "창원시",
    "통영시",
    "거창군",
    "고성군",
    "남해군",
    "산청군",
    "의령군",
    "창녕군",
    "하동군",
    "함안군",
    "함양군",
    "합천군",
  ];
  var area16 = ["서귀포시", "제주시", "남제주군", "북제주군"];

  // 시/도 선택 박스 초기화

  $("select[name^=sido]").each(function () {
    $selsido = $(this);
    $.each(eval(area0), function () {
      $selsido.append("<option value='" + this + "'>" + this + "</option>");
    });
    $selsido.next().append("<option value=''>구/군 선택</option>");
  });
  // 시/도 선택시 구/군 설정
  $("select[name^=sido]").change(function () {
    var area =
      "area" + $("option", $(this)).index($("option:selected", $(this))); // 선택지역의 구군 Array
    var $gugun = $(this).next(); // 선택영역 군구 객체
    $("option", $gugun).remove(); // 구군 초기화

    if (area == "area0") $gugun.append("<option value=''>구/군 선택</option>");
    else {
      $.each(eval(area), function () {
        $gugun.append("<option value='" + this + "'>" + this + "</option>");
      });
    }
  });
});
</script>
 
<script>
import mapApi from "@/api-ajax/map.js";
import { EventBus } from "@/lib/eventBus";
import campingList from '@/api-ajax/Location';

export default {
  name: "Map",
  data: () => ({
    campingLists:[],
    drawer: false,
    group: null,
    Mylocation: false,
  
  }),

  components: {},

  created() {
    EventBus.$on("triggerEventBus", (drawer) => {
      console.log(drawer);
      this.drawer = drawer;
    });

    EventBus.$on("mylocationEventBus", (Mylocation) => {
      console.log(Mylocation + "나의 위치");
      this.Mylocation = Mylocation;
    });
      campingList.getCampingList().then(res => {
    this.campingLists =[].concat(res.data);
    })

  },
  mounted: function () {
    var map = null;
    var markers = [];
    var infoWindows = [];

    initMap();

    function initMap() {
      map = new naver.maps.Map("naverMap", {
        center: new naver.maps.LatLng(37.3595704, 127.105399),
        zoom: 10,
      });

      naver.maps.Event.addListener(map, "zoom_changed", function () {
        updateMarkers(map, markers);
        console.log("zoom changed");
      });

      naver.maps.Event.addListener(map, "dragend", function () {
        updateMarkers(map, markers);
        console.log("dragend");
      });

      var bounds = map.getBounds(),
        southWest = bounds.getSW(),
        northEast = bounds.getNE(),
        lngSpan = northEast.lng() - southWest.lng(),
        latSpan = northEast.lat() - southWest.lat();

      get_markers(); //캠핑지 마커들
    }

    function change_map_center(latitude, longitude) {
      var position = new naver.maps.LatLng(latitude, longitude);
      map.setCenter(position);
    }
    function make_marker(latitude, longitude) {
      var position = new naver.maps.LatLng(latitude, longitude);
      var marker = new naver.maps.Marker({
        map: map,
        position: position,
      });
      return marker;
    }
    function get_markers() {
      $.get("/get_every_camping_locations", function (datas) {
        jsonData = JSON.parse(datas);
        jsonData.forEach(function (data) {
          console.log(data);

          //TODO : send ajax(maybe get?) to get review and informations
          //TODO : if user click the button in info window, send the info to the search text box
          var marker = make_marker(data["X_LOCATION"], data["Y_LOCATION"]);
          infowindow = get_infowindow(data);
          naver.maps.Event.addListener(marker, "click", function (e) {
            if (infowindow.getMap()) {
              infowindow.close();
            } else {
              infowindow.open(map, marker);
            }
          });
          naver.maps.Event.addListener(infowindow, "load", function (e) {
            document.querySelector();
          });
          // TODO : change icon according to the other factors. factors can be age , theme .. etc
          markers.push(marker);
        });
      });
    }

    function get_infowindow(data) {
      var contentString = [
        '<div class="iw_inner">',
        "   <h3>" + data["CITY"] + "</h3>",
        "   <p>" + data["ROAD_ADDRESS"] + "<br>",
        '       <button id="view_detail_btn" onclick="load_modal()">detail</button>',
        '       <a href="nmap://navigation?lat=37.4979502&lng=127.0276368&zoom=20&appname=com.example.myapp">set destination</button>',
        "   </p>",
        "</div>",
      ].join("");
      var infowindow = new naver.maps.InfoWindow({
        content: contentString,
      });
      return infowindow;
    }

    function load_modal() {
      $("#myModal").modal();
    }

    function updateMarkers(map, markers) {
      var mapBounds = map.getBounds();
      var marker, position;
      for (var i = 0; i < markers.length; i++) {
        marker = markers[i];
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

    function showMarker(map, marker) {
      if (marker.setMap()) return;
      marker.setMap(map);
    }

    function hideMarker(map, marker) {
      if (!marker.setMap()) return;
      marker.setMap(null);
    }
    // mapApi.initMap();

//리스너가 달려있어야 돌아감 
    if (this.Mylocation == true) {
      console.log("ddd");
      get_my_location();
    }
  }, // end_mount
  methods: {
    //현재위치 맵에 표시
    get_my_location() {
      // var location_text = document.querySelector("#start_position_text").text;
      var startPos;
      var geoSuccess = function (position) {
        startPos = position;
        var lat = startPos.coords.latitude;
        var lon = startPos.coords.longitude;
        var start_posi_marker = make_marker(lat, lon);
        markers.push(start_posi_marker);
        showMarker(map, start_posi_marker);
        change_map_center(lat, lon);
      };
      navigator.geolocation.getCurrentPosition(geoSuccess);
    },
  },
};
</script>

<style>
#naverMap {
  height: 100vh;
  min-height: 100vh;
  width: 100%;
}
</style>