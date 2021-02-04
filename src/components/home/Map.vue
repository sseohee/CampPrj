<template>
  <div id="wrap" class="section">
    <h1>Map is here</h1>
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
          <v-subheader>Camping Search</v-subheader>
          <v-row align="center">
            <v-select
              :items="regions"
              label="Regions"
              dense
              solo
              width="80%"
            ></v-select>

            <v-select
              :items="cities"
              label="Cities"
              dense
              solo
              width="80%"
            ></v-select>
            <v-btn outlined id="Search">Search</v-btn>
          </v-row>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
 
<script>
 import mapApi from "@/api-ajax/map.js";
import { EventBus } from "@/lib/eventBus";

export default {
  name: "Map",
  data: () => ({
    drawer: false,
    group: null,
    regions: ["Seoul", "Incheon", "Daejeon", "Gwangju"],
    cities: ["1", "2", "3", "4"],
  }),
  components: {},

  created() {
    EventBus.$on("triggerEventBus", (drawer) => {
      console.log(drawer);
      this.drawer = drawer;
    });
  },
  mounted: function() {
    var map = null;
    var markers = [];
    var infoWindows = [];

  
     mapApi.initMap();
    //  initMap();

    // function initMap() {
    //   map = new naver.maps.Map(document.getElementById("naverMap"), {
    //     center: new naver.maps.LatLng(37.3595704, 127.105399),
    //     zoom: 10,
    //     // zoomControl: true,
    //     // zoomControlOptions: {
    //     //   position: naver.maps.Position.RIGHT_TOP,
    //     // },
    //   });

    //   var marker = new naver.maps.Marker({
    //     position: new naver.maps.LatLng(36, 127),

    //     map: map,
    //   });

    //   markers.push(marker);

    //   var infoWindow = new naver.maps.InfoWindow({
    //     content: "표시내용",
    //   });

    //   infoWindows.push(infoWindow);

    //   for (var i = 0; i < markers.length; i++) {
    //     naver.maps.Event.addListener(markers[i], "click", getClickHandler(i));
    //   }
    // }
  }, // end_mount
};
</script>

<style>
#naverMap {
height: 100vh;
min-height: 100vh;
width: 100%;
}
</style>