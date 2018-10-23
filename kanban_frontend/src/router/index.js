import Vue from 'vue'
import Router from 'vue-router'
import KanbanBoard from '@/components/KanbanBoard'
import Boards from '@/components/Boards'
import NotFound from '@/components/NotFound'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Boards',
      component: Boards
    },
    {
      path: '/boards/:id',
      name: 'kanbanboard',
      component: KanbanBoard,
      props: (route) => ({
        id: route.params.id,
      })
    },
    {
      path: '/404',
      component: NotFound,
    },
    {
      path: "*",
      redirect: '/404',
    }
  ],
})
