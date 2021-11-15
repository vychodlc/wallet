<template>
  <div class="daily">
    <div class="head">
      <div class="time">{{data.month}}月{{data.day}}日 星期{{week[data.weekday-1]}}</div>
      <div class="sum">{{getSum()}}</div>
    </div>
    <div class="item" v-for="(item,index) in data.detail" :key="index">
      <div class="icon"><img src="../assets/imgs/type/5.png" alt=""></div>
      <div class="name">{{item.name}}</div>
      <div class="number">{{(item.method==0?'-':'') + item.amount}}</div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'daily',
  data() {
    return {
      week: ['一','二','三','四','五','六','日'],
      data: {
        month: 11,
        day: 14,
        weekday: 7,
        detail: [
          // type: 0 餐饮，1 购物，2 日用，3 交通，4 水果
          // name
          // method: 0 支出，1 收入
          { type: 0, name: '水', method: 0, amount: '2.7' },
          { type: 1, name: '服务器', method: 0, amount: '134' },
          // { type: 1, name: '午饭', method: 1, amount: '45' },
          // { type: 4, name: '水果', method: 1, amount: '45' },
          // { type: 3, name: '公交车', method: 0, amount: '454' },
        ],
      }
    };
  },
  methods: {
    getSum() {
      let input = 0, output = 0;
      this.$data.data.detail.map(item=>{
        item.method==0?output+=parseFloat(item.amount):input+=parseFloat(item.amount)
      })
      return (input>0?'收入：'+input:'') + '\u3000' + (output>0?'支出：'+output:'')
    },
    getImg(index) {
      return '../assets/imgs/type/'+ index +'.png'
    }
  }
});
</script>
<style scoped>
.daily {
  width: 100vw;
  background-color: #fff;
}
.daily .head {
  width: 100vw;
  height: 40px;
  padding: 0 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  color: #888;
  line-height: 40px;
  border-bottom: 1px solid #eeeeee;
}
.daily .item {
  padding: 5px 10px;
  width: 100vw;
  height: 60px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.daily .item .icon {
  width: 30px;
  height: 30px;
  margin: 0 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--color);
  border-radius: 50%;
}
.daily .item .icon img {
  width: 20px;
  height: 20px;
}
.daily .item .name {
  flex: 1;
  padding-left: 10px;
  height: 60px;
  line-height: 60px;
  border-bottom: 1px solid #eeeeeeaa;
}
.daily .item .number {
  height: 60px;
  line-height: 60px;
  border-bottom: 1px solid #eeeeeeaa;
}
.daily .item:last-child .name,
.daily .item:last-child .number {
  border-bottom: none;
}
</style>