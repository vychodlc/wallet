<template>
  <div id="tabbar">
    <div class="item" v-for="(item,index) in data" :key="index" @click="routeGo(item.path)">
      <div class="icon"><img :src="item.icon" alt=""></div>
      <div class="name">{{ item.name }}</div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'tabbar',
  data() {
    return {
      data: [
        { name: '明细', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg', path: 'Home'},
        { name: '图表', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg', path: 'Graph'},
        { name: '记账', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg', path: 'Add'},
        { name: '社区', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg', path: 'Society'},
        { name: '我的', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg', path: 'Person'},
      ]
    };
  },
  methods: {
    routeGo(path) {
      if(path!=this.$route.name) {
        this.$router.replace({path: path})
      }
    }
  },
});
</script>
<style scoped>
#tabbar {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100vw;
  height: 60px;
  padding: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid #eee;
  background-color: #fff;
}
.item {
  width: 50px;
  height: 50px;
}
.item .icon {
  width: 35px;
  height: 35px;
  margin: 0 auto;
}
.item img {
  width: 35px;
  height: 35px;
}
.item .name {
  width: 50px;
  text-align: center;
  font-size: 12px;
}
</style>