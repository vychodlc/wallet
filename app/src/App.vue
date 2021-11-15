<template>
  <div id="app">
    <router-view/>
    <TabBar />
  </div>
</template>
<script>
import TabBar from '@/components/TabBar.vue'
export default {
  name: 'Home',
  components: {
    TabBar
  },
}
</script>
<style>
@import 'assets/css/base.css';

#app {
  width: 100vw;
  height: 100vh;
  /* background-color: var(--color); */
  position: fixed;
}
</style>
