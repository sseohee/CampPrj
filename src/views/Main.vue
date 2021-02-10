<template>
<div class= "main" >
 <v-container>
    <v-row  class="row-group" >
    <v-col>
    <v-btn color="secondary" elevation="5" fab large  x-large style="color:#669966;" 
    router-link to="/home">캠핑/차박 검색
    </v-btn>
    </v-col>

    <v-col>
    <v-btn color="secondary" elevation="5" fab large  x-large style="color:#669966;"
    router-link to="/potal">포탈</v-btn>
    </v-col>
    <v-col>
    <v-btn color="secondary" elevation="5" fab large  x-large style="color:#669966;"
    router-link to="/mycamping">마이캠핑</v-btn>
    </v-col>
</v-row>
</v-container>
</div>
</template>

<script>
export default {};
</script>

<style scoped>
.main{
height: 600px;
text-align: center;

}
.row-group{
padding-top: 150px;
}
.v-btn{
    width: 200px;
    height: 200px;
}

</style>