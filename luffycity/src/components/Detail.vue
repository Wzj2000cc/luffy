<template>
  <div class="detail">
    <Header></Header>
    <div class="main">
      <div class="course-info">
        <!--  视频video部分    -->
        <div class="wrap-left">
          <video-player class="video-player vjs-custom-skin"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions"
                        @play="onPlayerPlay($event)"
                        @pause="onPlayerPause($event)">
          </video-player>
        </div>
        <div class="wrap-right">
          <h3 class="course-name">{{ course.name }}</h3>
          <p class="data">
            {{ course.students }}人在学&nbsp;&nbsp;&nbsp;&nbsp;课程总时长：{{ course.pub_lessons }}课时/{{ course.lessons }}课时&nbsp;&nbsp;&nbsp;&nbsp;
            难度：{{ course.get_level_display }}</p>
          <div class="sale-time" v-if="course.discount_name">
            <p class="sale-type">{{ course.discount_name }}</p>
            <p class="expire">距离结束：
              仅剩 {{ course.active_time / 60 / 60 / 24 | format_time }}天
              {{ course.active_time / 60 / 60 % 24 | format_time }}小时
              {{ course.active_time / 60 % 60 | format_time }}分 <span class="second">
                {{ course.active_time % 60 | format_time }}</span> 秒</p>
          </div>
          <p class="course-price">
            <span v-if="course.discount_name">活动价</span>
            <span class="discount">¥{{ course.active_real_price }}</span>
            <span class="original" v-if="course.discount_name">¥{{ course.price }}</span>
          </p>
          <div class="buy">
            <div class="buy-btn">
              <button class="buy-now">立即购买</button>
              <button class="free">免费试学</button>
            </div>
            <div class="add-cart" @click="AddCart"><img src="@/assets/gouwuche.png" alt="">加入购物车</div>
          </div>
        </div>
      </div>
      <div class="course-tab">
        <ul class="tab-list">
          <li :class="tabIndex==1?'active':''" @click="tabIndex=1">详情介绍</li>
          <li :class="tabIndex==2?'active':''" @click="tabIndex=2">课程章节 <span :class="tabIndex!=2?'free':''">(试学)</span>
          </li>
          <li :class="tabIndex==3?'active':''" @click="tabIndex=3">用户评论 (42)</li>
          <li :class="tabIndex==4?'active':''" @click="tabIndex=4">常见问题</li>
        </ul>
      </div>
      <div class="course-content">
        <div class="course-tab-list">
          <!--  课程详情  -->
          <div class="tab-item" v-if="tabIndex==1">
            <div v-html="course.brief_html"></div>
          </div>
          <!--  课程章节   -->
          <div class="tab-item" v-if="tabIndex==2">
            <div class="tab-item-title">
              <p class="chapter">课程章节</p>
              <p class="chapter-length">共{{course.len_chapter}}章 更新至{{course.lessons}}课时</p>
            </div>
            <div class="chapter-item" v-for="(value1,index1) in course.chapter_list" :key="value1.id"
                 @click="hideShow(index1)">
              <p class="chapter-title"><img src="@/assets/jiahao.png" alt="" v-show="status_dic!==index1"><img
                src="@/assets/jianhao.png" alt="" v-show="status_dic===index1">
                {{ value1.name }}</p>
              <ul class="lesson-list" v-for="(value,index) in value1.lesson_list" :key="value.id"
                  v-show="status_dic===index1">
                <li class="lesson-item">
                  <p class="name"><span class="index">{{ index1 + 1 }}-{{ value.lesson }}</span> {{ value.name }}<span
                    class="free">{{ value.free_trail === true ? `免费` : `付费` }}</span></p>
                  <p class="time">07:30 <img src="@/assets/ziliao.png"></p>
                  <button class="try">立即试学</button>
                </li>
              </ul>
            </div>
          </div>
          <div class="tab-item" v-if="tabIndex==3">
            用户评论
          </div>
          <div class="tab-item" v-if="tabIndex==4">
            常见问题
          </div>
        </div>
        <div class="course-side">
          <!--    老师详情框      -->
          <div class="teacher-info">
            <h4 class="side-title"><span>授课老师</span></h4>
            <div class="teacher-content">
              <div class="cont1">
                <img :src="course.teacher.image">
                <div class="name">
                  <p class="teacher-name">{{ course.teacher.name }}</p>
                  <p class="teacher-title">{{ course.teacher.title }}</p>
                </div>
              </div>
              <p class="narrative">{{ course.teacher.brief }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header"
import Footer from "./common/Footer"
import {videoPlayer} from 'vue-video-player'

export default {
  name: "Detail",
  data() {
    return {
      status_dic : '', // 点击章节展开调用hideShow赋值index
      tabIndex: 2,
      course_id: 0,  // 课程id
      // 课程章节课时数据
      course: {
        teacher: {},
      },
      // video视频播放
      playerOptions: {
        playbackRates: [0.7, 1.0, 1.5, 2.0], // 播放速度
        autoplay: false, //如果true,则自动播放
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 循环播放
        preload: 'auto', // 允许视频缓冲
        language: 'zh-CN',
        aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [{
          type: "video/mp4",//还可以配置其他格式
          // src: "http://img.ksbbs.com/asset/Mon_1703/05cacb4e02f9d9e.mp4" //你的视频地址（必填）
          src: "http://mirror.aarnet.edu.au/pub/TED-talks/911Mothers_2010W-480p.mp4" //你的视频地址（必填）
        },
          // 上一个视频的格式不支持，执行下一个。
          //   {
          //   type: "video/avi",//还可以配置其他格式
          //   src: "http://img.ksbbs.com/asset/Mon_1703/05cacb4e02f9d9e.mp4" //你的视频地址（必填）
          // }
        ],

        poster: "../static/PY1.png", //视频封面图
        width: document.documentElement.clientWidth,
        notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
      }
    }
  },
  created() {
    this.get_course_id();
    this.get_course_detail();
  },
  methods: {

    // 获取当前课程的id（使用VUE中的$route.params.id方法）
    get_course_id() {
      let course_id = this.$route.params.id;
      // alert(typeof course_id);
      course_id = parseInt(course_id);
      console.log(this.course.id)
      // 对id进行限制（防止恶意修改id值，例如：-100，aaa）
      if (course_id > 0) {  // id参数的审核有问题
        this.course_id = course_id;
      } else {
        let self = this;
        this.$alert('参数有误！', '别乱搞！！！', {
          callback() {
            // self.$router.go(-1); // 返回上一页面
            location.href = 'http://www.luffycity.cn:8080/#/course'
          }
        })
      }
    },

    // 通过课程id获取该课程的章节和课时
    get_course_detail() {
      this.$axios.get(`${this.$settings.Host}/course/detail/${this.course_id}/`)
        .then(res => {
          // console.log(res.data.course_img)
          this.course = res.data;
          // 后端获取的课程视频路径赋值到video值里
          this.playerOptions.sources[0].src=res.data.course_video;
          this.playerOptions.poster=res.data.course_img;
          if (this.course.active_time > 0){
            let t = setInterval(() =>{
              if (this.course.active_time > 1){
                this.course.active_time--;
              }else {
                clearInterval(t)
              }
            },1000)
          }
          }
        ).catch(error => {
          console.log(error.response);
        })
    },

    // 点击章节展开调用
    hideShow(index){
      this.status_dic=index
    },

    // 视频播放调用
    player() {
      return this.$refs.videoPlayer.player
    },
    // 视频播放中，播放广告，这就是事件。
    onPlayerPlay(player) {
      alert("点击确定开始播放");
    },
    onPlayerPause(player) {
      alert("暂停一下，点击确定开始播放");
    },

    // 用户添加购物车时判断该用户登录状态
    check_user_login() {
      let token = localStorage.user_token || sessionStorage.user_token;
      if (!token) {
        let self = this;
        this.$confirm('对不起，您尚未登陆,请先登录再添加购物车', '路飞', {
          confirmButtonText: '确定',
          cancelButtonClass: '取消',
        }).then(() => {
          self.$router.push('/login/')
        });
        return false
      }
      return token
    },

    // 点击将该课程添加到购物车
    AddCart() {
      //先要验证用户是否登录
      let token = this.check_user_login();
      //将课程id发送到后端
      if (!token) {  //如果token魏false函数不执行
        return false
      }
      this.$axios.post(`${this.$settings.Host}/cart/`, {
          course_id: this.course_id,
        }, {
          headers: {
            'Authorization': 'jwt ' + token,
          }
        }
      ).then(res => {
        this.$message.success(res.data.msg)
      }).catch(error => {
        console.log(error.response)
      })
    },
  },

  filters:{
    // 课程活动倒计时计时器（判断数字小于10时数字前拼接0；例如：09,08,07）
    format_time(val){
      let timer = parseInt(val)
      if (timer < 10){
        timer = `0${timer}`;
      }
      return timer
    }
  },
  // 挂载
  components: {
    Header,
    Footer,
  }
}
</script>

<style scoped>
.main {
  background: #fff;
  padding-top: 30px;
}

.course-info {
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
}

.wrap-left {
  float: left;
  width: 690px;
  height: 388px;
}

.wrap-right {
  float: left;
  position: relative;
  height: 388px;
}

.course-name {
  font-size: 20px;
  color: #333;
  padding: 10px 23px;
  letter-spacing: .45px;
}

.data {
  padding-left: 23px;
  padding-right: 23px;
  padding-bottom: 16px;
  font-size: 14px;
  color: #9b9b9b;
}

.sale-time {
  width: 464px;
  background: #fa6240;
  font-size: 14px;
  color: #4a4a4a;
  padding: 10px 23px;
  overflow: hidden;
}

.sale-type {
  font-size: 16px;
  color: #fff;
  letter-spacing: .36px;
  float: left;
}

.sale-time .expire {
  font-size: 14px;
  color: #fff;
  float: right;
}

.sale-time .expire .second {
  width: 24px;
  display: inline-block;
  background: #fafafa;
  color: #5e5e5e;
  padding: 6px 0;
  text-align: center;
}

.course-price {
  background: #fff;
  font-size: 14px;
  color: #4a4a4a;
  padding: 5px 23px;
}

.discount {
  font-size: 26px;
  color: #fa6240;
  margin-left: 10px;
  display: inline-block;
  margin-bottom: -5px;
}

.original {
  font-size: 14px;
  color: #9b9b9b;
  margin-left: 10px;
  text-decoration: line-through;
}

.buy {
  width: 464px;
  padding: 0px 23px;
  position: absolute;
  left: 0;
  bottom: 20px;
  overflow: hidden;
}

.buy .buy-btn {
  float: left;
}

.buy .buy-now {
  width: 125px;
  height: 40px;
  border: 0;
  background: #ffc210;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  margin-right: 15px;
  outline: none;
}

.buy .free {
  width: 125px;
  height: 40px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 15px;
  background: #fff;
  color: #ffc210;
  border: 1px solid #ffc210;
}

.add-cart {
  float: right;
  font-size: 14px;
  color: #ffc210;
  text-align: center;
  cursor: pointer;
  margin-top: 10px;
}

.add-cart img {
  width: 20px;
  height: 18px;
  margin-right: 7px;
  vertical-align: middle;
}

.course-tab {
  width: 100%;
  background: #fff;
  margin-bottom: 30px;
  box-shadow: 0 2px 4px 0 #f0f0f0;

}

.course-tab .tab-list {
  width: 1200px;
  margin: auto;
  color: #4a4a4a;
  overflow: hidden;
}

.tab-list li {
  float: left;
  margin-right: 15px;
  padding: 26px 20px 16px;
  font-size: 17px;
  cursor: pointer;
}

.tab-list .active {
  color: #ffc210;
  border-bottom: 2px solid #ffc210;
}

.tab-list .free {
  color: #fb7c55;
}

.course-content {
  width: 1200px;
  margin: 0 auto;
  background: #FAFAFA;
  overflow: hidden;
  padding-bottom: 40px;
}

.course-tab-list {
  width: 880px;
  height: auto;
  padding: 20px;
  background: #fff;
  float: left;
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.tab-item {
  width: 880px;
  background: #fff;
  padding-bottom: 20px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.tab-item-title {
  justify-content: space-between;
  padding: 25px 20px 11px;
  border-radius: 4px;
  margin-bottom: 20px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
  overflow: hidden;
}

.chapter {
  font-size: 17px;
  color: #4a4a4a;
  float: left;
}

.chapter-length {
  float: right;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
}

.chapter-title {
  font-size: 16px;
  color: #4a4a4a;
  letter-spacing: .26px;
  padding: 12px;
  background: #eee;
  border-radius: 2px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
}

.chapter-title img {
  width: 18px;
  height: 18px;
  margin-right: 7px;
  vertical-align: middle;
}

.lesson-list {
  padding: 0 20px;
}

.lesson-list .lesson-item {
  padding: 15px 20px 15px 36px;
  cursor: pointer;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}

.lesson-item .name {
  font-size: 14px;
  color: #666;
  float: left;
}

.lesson-item .index {
  margin-right: 5px;
}

.lesson-item .free {
  font-size: 12px;
  color: #fff;
  letter-spacing: .19px;
  background: #ffc210;
  border-radius: 100px;
  padding: 1px 9px;
  margin-left: 10px;
}

.lesson-item .time {
  font-size: 14px;
  color: #666;
  letter-spacing: .23px;
  opacity: 1;
  transition: all .15s ease-in-out;
  float: right;
}

.lesson-item .time img {
  width: 18px;
  height: 18px;
  margin-left: 15px;
  vertical-align: text-bottom;
}

.lesson-item .try {
  width: 86px;
  height: 28px;
  background: #ffc210;
  border-radius: 4px;
  font-size: 14px;
  color: #fff;
  position: absolute;
  right: 20px;
  top: 10px;
  opacity: 0;
  transition: all .2s ease-in-out;
  cursor: pointer;
  outline: none;
  border: none;
}

.lesson-item:hover {
  background: #fcf7ef;
  box-shadow: 0 0 0 0 #f3f3f3;
}

.lesson-item:hover .name {
  color: #333;
}

.lesson-item:hover .try {
  opacity: 1;
}

.course-side {
  width: 300px;
  height: auto;
  margin-left: 20px;
  float: right;
}

.teacher-info {
  background: #fff;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}

.side-title {
  font-weight: normal;
  font-size: 17px;
  color: #4a4a4a;
  padding: 18px 14px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, .05);
}

.side-title span {
  display: inline-block;
  border-left: 2px solid #ffc210;
  padding-left: 12px;
}

.teacher-content {
  padding: 30px 20px;
  box-sizing: border-box;
}

.teacher-content .cont1 {
  margin-bottom: 12px;
  overflow: hidden;
}

.teacher-content .cont1 img {
  width: 54px;
  height: 54px;
  margin-right: 12px;
  float: left;
}

.teacher-content .cont1 .name {
  float: right;
}

.teacher-content .cont1 .teacher-name {
  width: 188px;
  font-size: 16px;
  color: #4a4a4a;
  padding-bottom: 4px;
}

.teacher-content .cont1 .teacher-title {
  width: 188px;
  font-size: 13px;
  color: #9b9b9b;
  white-space: nowrap;
}

.teacher-content .narrative {
  font-size: 14px;
  color: #666;
  line-height: 24px;
}
</style>

