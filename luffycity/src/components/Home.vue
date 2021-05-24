<template>
  <div class="home">
        <el-container>
          <el-header class="out-header">
    <Header></Header>
    <Banner></Banner>
    <add></add>

    <Footer></Footer>

          </el-header>
        </el-container>
`
  </div>
</template>

<script>
import Header from './common/Header'
import Banner from "./common/Banner"
import Footer from "./common/Footer";
import Add from "./common/Add";

export default {
  name: "Home",
  components: {
    Header,
    Banner,
    Footer,
    Add,
  }
}
</script>

<style scoped>
  .out-header {
    padding: 0;
    height: 80px !important;
  }
</style>
