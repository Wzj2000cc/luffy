<template>
  <el-carousel id="bannerSwiper" style="height: 400px">
    <el-carousel-item v-for="(value,index) in banner_list" :key="value.id" style="height: 400px" indicator-position='outside'>
      <!--      <router-link :to="value.link">-->
      <a :href="value.link">
        <img :src="value.image_url" alt="">
        <!--      </router-link>-->
      </a>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
      banner_list: [
        // {'id': 1, img_src: require('@/assets/banner/banner1.png'), link: 'http://www.baidu.com'},
        // {'id': 2, img_src: require('@/assets/banner/banner2.png'), link: 'http://www.baidu.com'},
      ]
    }
  },
  methods:{
    get_banner_data(){
      this.$axios.get(`${this.$settings.Host}/home/banner/`).then((res)=>{
        // console.log(res.data())
        this.banner_list = res.data;
      }).catch((error)=>{
        console.log(error);
      })
    }
  },
  created() {
    // 钩子函数，当加载这个组件到某个时刻自动触发created钩子函数
    this.get_banner_data();
  }
}
</script>

<style scoped>
#bannerSwiper a {
  display: inline-block;
  margin-left: -100px;
  width: 2150px;
  height: 400px;
}

#bannerSwiper a img {
  height: 100%;
  width: 100%;
}
</style>
