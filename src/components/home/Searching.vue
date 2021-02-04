<template>
  <div>
    <v-container>
      <v-row>
        <v-form>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="departure"
                  :append-icon="
                  marker ? 'mdi-map-marker' : 'mdi-map-marker'"
                  filled
                  clear-icon="mdi-close-circle"
                  clearable
                  label="Departure"
                  type="text"
                  @click:append="getMylocation" 
                  @click:clear="clearMessage"
                ></v-text-field>
              </v-col>
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
                  label="Arrival"
                  type="text"
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




export default {
  
  data: () => ({
    password: "Password",
    drawer:true,
    show: false,
    departure: "",
    arrival:"",
    marker: true,
    iconIndex: 0
    
  }),

  components: {
   Map,
  }, 

  methods: {
    getMylocation() { 
      getMyloca.get_my_location().then(res => {
     this.departure= "current Location";
      })
    },
    sendMessage() { // arrival && departure complite 
      
    },
    clearMessage() {
      this.message = "";
    },
    openDrawer(){
      EventBus.$emit('triggerEventBus',this.drawer);
    
    }
 },
};
</script>