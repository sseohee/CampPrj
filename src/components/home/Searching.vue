<template>
  <div>
    <v-container>
      <v-row>
        <v-form>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field id="start_position_text"
                  v-model="departure"
                  :append-icon="
                  marker ? 'mdi-map-marker' : 'mdi-map-marker'"
                  filled
                  clear-icon="mdi-close-circle"
                  clearable
                  label="출발지"
                  type="text"
                  placeholder="출발지를 입력하세요"
                  @click:append="Mylocation" 
                  @click:clear="clearMessage"
                  style="width:100%"
                ></v-text-field>
            </v-row>
          </v-container>
        </v-form>
      </v-row>
      <v-row>
        <v-form>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="arrival"

                  filled
                  clear-icon="mdi-close-circle"
                  clearable
                  label="도착지"
                  type="text"
                  placeholder="도착지를 입력하세요"
                  @click="openDrawer"
                  @click:clear="clearMessage"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-row>
    </v-container>
  </div>
</template>



<script>
import {EventBus} from '../../lib/eventBus';
import  Map from './Map'
// import CurrentLoca from '@/api-ajax/action';





export default {
  
  data: () => ({
    password: "Password",
    drawer:true,
    show: false,
    departure: "",
    arrival:"",
    marker: true,
    iconIndex: 0,
    
    
  }),

  components: {
   Map,
  }, 

  methods: {
    Mylocation(){
        EventBus.$emit('mylocationEventBus',true);
        var myLocationText="";
      navigator.geolocation.getCurrentPosition(function(position) {
          alert("위도 : " + position.coords.latitude + "\n" + "경도 : " + position.coords.longitude);
          var lat = position.coords.latitude;
          var lon = position.coords.longitude;
          
          myLocationText=lat + lon;
          
      }); this.departure="mylocationText";
    }    
        
    
    
      
    ,
    sendMessage() { // arrival && departure complite 
      
    },
    clearMessage() {
      this.message = "";
    },
    openDrawer(){
      EventBus.$emit('triggerEventBus',this.drawer);
    
    }
 },
 mounted(){
    

 }
};
</script>