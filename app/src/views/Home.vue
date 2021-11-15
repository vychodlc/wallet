<template>
  <div class="home">
    <div class="head">
      <Title/>
      <div class="overview">
        <div class="time">
          <div class="year">{{overview.current.year}}年</div>
          <div class="month"><span>{{overview.current.month}}</span>月</div>
        </div>
        <div class="amount">
          <div class="item" v-for="(item,index) in overview.amount" :key="index">
            <div class="subtitle">{{item.name}}</div>
            <div class="number">{{item.int}}.<span>{{item.float}}</span></div>
          </div>
        </div>
      </div>
      <BtnList />
      <div class="list">
        <Daily v-for="(item,index) in 5" :key="index" />
      </div>
    </div>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import BtnList from '@/components/BtnList.vue'
import Daily from '@/components/Daily.vue'

export default {
  name: 'Home',
  components: {
    Title,
    BtnList,
    Daily,
  },
  data() {
    return {
      overview: {
        current: {
          month: 11, year: 2021
        }, 
        amount: [
          {name: '收入', int: '1700', float: '01'},
          {name: '支出', int: '202', float: '18'},
        ]
      }
    }
  }
}
</script>
<style scoped>
.home {
  width: 100vw;
  height: calc(100vh - 60px);
}
.overview {
  width: 100vw;
  height: 65px;
  display: flex;
  background-color: var(--color);
}
.time {
  width: 25vw;
  height: 65px;
  padding-left: 10px;
}
.time .year {
  height: 30px;
  line-height: 30px;
  text-align: left;
  font-size: 12px;
  color: #555;
}
.time .month {
  height: 30px;
  line-height: 30px;
  margin-top: 5px;
  text-align: left;
  color: #000;
  font-size: 14px;
  border-right: 1px solid #555;
}
.time .month span {
  font-size: 24px;
}
.amount {
  width: 75vw;
  height: 65px;
  display: flex;
  flex-direction: row;
}
.amount .item {
  height: 60px;
  width: 28vw;
  margin-left: 7vw;
}
.amount .item .subtitle {
  height: 30px;
  line-height: 30px;
  text-align: left;
  font-size: 12px;
  color: #555;
}
.amount .item .number {
  height: 30px;
  line-height: 30px;
  margin-top: 5px;
  text-align: left;
  color: #000;
  font-size: 20px;
}
.amount .item .number span {
  font-size: 14px;
}

.list {
  widows: 100vw;
  height: calc(100vh - 60px - 65px - 90px - 60px);
  overflow-y: scroll;
  overflow-x: hidden;
}
</style>