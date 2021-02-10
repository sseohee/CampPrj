<template>
  <div v-if="Direction">
    <select v-model="stayDuration">
      <option>{{}}</option>
    </select>
    <button>길안내</button>

    <p>밀집도 정보</p>
    <p>해당 도착지는 오늘 하루 0번 검색 되었습니다.</p>
  </div>
</template>

<script>
import { EventBus } from "@/lib/eventBus";


export default {
  data() {
    return {
      Direction: false, //도착지 입력시 true로 변경하여 체류기가, 길안내, 경로, 밀집도, 하루검색량 표출
    };
  },
  created(){

    // EventBus.$on("triggerEventBus", (drawer) => {
    //   console.log(drawer);
    //   this.drawer = drawer;
    // });
  }
  


};





</script>

<style>
button {
  color: blueviolet;
}
</style>