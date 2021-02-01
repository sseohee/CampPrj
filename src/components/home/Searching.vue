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
                  @click:append="toggleMarker"
                  @click:append-outer="sendMessage"
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
                  @click:append="toggleMarker"
                  @click:append-outer="sendMessage"
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
export default {
  data: () => ({
    password: "Password",
    show: false,
    departure: "",
    arrival:"",
    marker: true,
    iconIndex: 0
    
  }),

  computed: {
   
  },

  methods: {
    toggleMarker() { 
      this.departure= "current location";
    },
    sendMessage() { // arrival && departure complite 
      
    },
    clearMessage() {
      this.message = "";
    }
   
  },
};
</script>