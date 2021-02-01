<template>
  <div id="map">
    <v-container>
      <h1>Map is here</h1>

      <v-app-bar-nav-icon right @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-navigation-drawer v-model="drawer" absolute bottom temporary right>
        <v-list nav dense>
          <v-list-item-group
            v-model="group"
            active-class="deep-purple--text text--accent-4"
          >
           <v-subheader>Camping Search</v-subheader>
             <v-row align="center">
     
       <v-select
          :items="regions"
          label="Solo field"
          dense
          solo
        ></v-select>
        
        <v-select
          :items="cities"
          label="Solo field"
          dense
          solo
        ></v-select>
     
    </v-row>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "map",
  data: () => ({
    drawer: false,
    group: null, 
    regions: ['Seoul', 'Incheon', 'Daejeon', 'Gwangju'],
    cities:['1', '2', '3', '4']
  }),

  watch: {
    group() {
      
    },
  },
};
</script>