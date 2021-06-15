<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
    // 监听页面刷新事件，将数据保存到sessionStorage中
    window.addEventListener('beforeunload',()=>{
      console.log('页面即将刷新，赶紧保存数据！！！')
      sessionStorage.setItem('cart_length',this.$store.state.cart.cart_length)
    })
  }
}
</script>

<style>
body {
  padding: 0;
  margin: 0;
}

a {
  text-decoration: none;
  color: #4a4a4a;
}

a:hover {
  color: #000;
}

.header .el-menu li .el-submenu__title {
  height: 26px !important;
  line-height: 26px !important;
}

.el-menu--popup {
  min-width: 140px;
}
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
