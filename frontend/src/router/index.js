import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import Person from '../views/PersonView.vue'


const routes = [
  {
    path: '/',
    name: 'person',
    component: Person
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
