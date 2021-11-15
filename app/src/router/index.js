import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/Home'},
  { path: '/Home', name: 'Home', component: () => import('../views/Home.vue')},
  { path: '/Graph', name: 'Graph', component: () => import('../views/Graph.vue')},
  { path: '/Add', name: 'Add', component: () => import('../views/Add.vue')},
  { path: '/Society', name: 'Society', component: () => import('../views/Society.vue')},
  { path: '/Person', name: 'Person', component: () => import('../views/Person.vue')},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
