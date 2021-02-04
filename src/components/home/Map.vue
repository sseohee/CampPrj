<template>
  <div id="Map">
    
      <h1>Map is here</h1>
      <div>
        
      </div>
    

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
 <script type="text/javascript"
     src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=2bkpqttxm3&&callback=initMap"></script>


<script>
import mapApi from "@/api-ajax/map.js";
import { EventBus } from "../../lib/eventBus";

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
    }),
      mapApi
  },
};
</script>