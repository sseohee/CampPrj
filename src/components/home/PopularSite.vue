<template>
  <v-card
    tile
    style="width: 100%" 
    v-if="popular"
  >
    <v-list rounded>
      <v-subheader>인기 검색지</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="(popular, i) in populars"
          :key="i"
        >
          <v-list-item-content>
            <v-title v-text="popular.title"></v-title>
          </v-list-item-content>
          <v-list-item-content>
            <v-list-item-title v-text="popular.campingsite"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>

import popularApi from '@/api-ajax/popular';

export default {
 data(){
     
     return {
         populars:[],
         selectedItem: 1,
         popular:true //도착지 입력시 fasle로 변환하여 인기검색지 감추기 
     }
 },
 created(){
     popularApi.getPopular().then(res => {
     this.populars =[].concat(res.data);
     })
 }
}
</script>