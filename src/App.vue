<template>
   <div id ="app">
     <Header/>
      <router-view />
     <Footer/>
   </div>
</template>

<script>
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';


export default {
  mounted() {
    $.initialize();
  },

  components: {
    Header,
    Footer

  },

  data: () => ({
    //
  }),
};
</script>
