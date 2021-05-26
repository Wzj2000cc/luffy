import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from "../components/Home";
import Course from "../components/Course";
import Detail from "../components/Detail";
import Cart from "../components/Cart";
import Login from "../components/Login";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      // name: 'HelloWorld',
      // component: HelloWorld
      name:'Home',
      component:Home,
    },
    {
      path:'/course/',
      name:'Course',
      component:Course
    },
    {
      path:'/detail/',
      name:'Detail',
      component:Detail
    },
    {
      path:'/cart/',
      name:'Cart',
      component:Cart
    },
    {
      path:'/login/',
      name:'login',
      component:Login
    },
  ]})
