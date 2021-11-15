<template>
  <div id="box">
    <div id="btnlist">
      <div class="item" v-for="(item,index) in data" :key="index">
        <div class="icon"><img :src="item.icon" alt=""></div>
        <div class="name">{{ item.name }}</div>
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'btnlist',
  data() {
    return {
      data: [
        { name: '账单', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg'},
        { name: '预算', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg'},
        { name: '资产管家', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg'},
        { name: '理财知识', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg'},
        { name: '购物返现', icon: 'https://s3.bmp.ovh/imgs/2021/11/02224ebc175121fb.jpg'},
      ]
    };
  },
});
</script>
<style scoped>
#box {
  width: 100vw;
  background-color: var(--color);
  padding: 5px 0;
}
#btnlist {
  width: 96vw;
  margin: 0 auto;
  border-radius: 10px;
  height: 80px;
  background-color: #fff;
  padding: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid #eee;

  box-shadow: 2px 5px 5px #ccc;
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