<template>
  <div id="title">{{title}}</div>
</template>
<script>
import { defineComponent } from 'vue';
export default defineComponent({
  name: '',
  data() {
    return {
      title: '我爱记帐'
    };
  },
});
</script>
<style scoped>
#title {
  width: 100vw;
  height: 60px;
  line-height: 60px;
  text-align: center;
  font-size: 20px;
  color: #000;
  background-color: var(--color);
}
</style>