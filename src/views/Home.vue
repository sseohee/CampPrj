<template>
  <div class="Home">
    <v-app>
      <split style="height: 700px">
        <SplitArea :size="30" class="left-group">
          <v-container >
            <v-col>
              <v-row><Searching /></v-row>
              <v-row><Popular /></v-row>
            </v-col>
          </v-container>
        </SplitArea>

        <SplitArea :size="70" class="right-group">
          <v-container >
            <Map />
          </v-container>
        </SplitArea>
      </split>
    </v-app>
  </div>
</template>

<script>
import Popular from "@/components/home/PopularSite.vue";
import Map from "@/components/home/Map.vue";
import Searching from "@/components/home/Searching.vue";
import ListSearch from "../components/home/ListSearch.vue";

export default {
  name: "Home",
  components: {
    Popular,
    Map,
    Searching,
    ListSearch,
  },
};
</script>

<style scoped>
.left-group{
  border: 1px solid rgb(12, 119, 57);
  border-radius: 10px;
  
  
}

.right-group{
  border: 1px solid rgb(12, 119, 57);
   border-radius: 10px;
   
}
</style>