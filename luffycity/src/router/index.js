import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Detail from "../components/Detail";
import Cart from "../components/Cart";
import Login from "../components/Login";
import Register from "../components/Register";
import Account from "../components/Account";
import Respwd from "../components/Respwd";
import Course from "../components/Course";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name:'Home',
      component:Home,
    },
    {
      path:'/course/',
      name:'Course',
      component:Course
    },
    {
      path:'/course/detail/:id',
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
    {
      path:'/register/',
      name:'register',
      component:Register
    },
    {
      path:'/account/',
      name:'account',
      component:Account
    },
    {
      path:'/respwd/',
      name:'respwd',
      component:Respwd
    },
  ]})
