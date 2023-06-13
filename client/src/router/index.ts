import { user } from '@/composable/fetchUser'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
      meta: {
        layout: 'Default'
      }
    },
    {
      path: '/article/:id',
      name: 'article',
      component: () => import('../views/ArticleView.vue'),
      meta: {
        layout: 'Default'
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: {
        layout: 'Empty',
        auth: false
      }
    },
    {
      path: '/registration',
      name: 'registration',
      component: () => import('../views/RegistrationView.vue'),
      meta: {
        layout: 'Empty',
        auth: false
      }
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      meta: {
        layout: 'Empty'
      }
    },
    {
      path: '/edit/:id',
      name: 'edit',
      component: () => import('../views/CreateArticleView.vue'),
      meta: {
        layout: 'Empty',
        auth: true
      }
    },
    {
      path: '/create',
      name: 'create',
      component: () => import('../views/CreateArticleView.vue'),
      meta: {
        layout: 'Empty',
        auth: true,
        create: true
      }
    }
  ]
})

router.beforeEach((to, _, next) => {
  const loggedIn = user.value

  if (to.meta.auth === true && !loggedIn) {
    return next('/login')
  }

  if (to.meta.auth === false && loggedIn) {
    return next(`/profile/${loggedIn.id}`)
  }

  next()
})

export default router
