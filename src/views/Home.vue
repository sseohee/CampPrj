<template>
  <div class="home">
   <v-app>
     <split style="height: 600px;">
       <SplitArea :size="30">
         <v-container>
         <v-col>
         <v-row><Searching/></v-row>
         <v-row><Popular /></v-row>
         
         </v-col>
          </v-container>
        </SplitArea>

       

       <SplitArea :size="70">
         <v-container>
        
         <Map />

         <Searchlist/>

         </v-container>
       </SplitArea>
     </split>
   </v-app>  
      
 </div>
</template>

<script>

import Popular from '@/components/home/PopularSite.vue'
import Map from '@/components/home/Map.vue'
import Searching from '@/components/home/Searching.vue'
import SearchList from '../components/home/SearchList.vue'

export default {
  
  
  name: 'home',
  components: {
   Popular ,
   Map,
   Searching,
    SearchList
  }
}
</script>
