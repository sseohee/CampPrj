import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Main from '../views/Main.vue'
import Potal from "../views/Potal.vue"
import Mycamping from "../views/Mycamping.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/potal',
    name: 'Potal',
    component: Potal
  }
  ,
  {
    path: '/mycamping',
    name: 'Mycamping',
    component: Mycamping
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
