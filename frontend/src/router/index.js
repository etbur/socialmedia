import { createRouter, createWebHistory } from 'vue-router'
import PostView from '../views/PostView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/post',
      name: 'post',
      component: PostView
    },
   
  ]
})

export default router
