<template>
  <div class="total-header">
    <div class="header">
      <el-container>
        <el-header height="80px" class="header-cont">
          <el-row>
            <el-col class="logo" :span="3">
              <a href="/">
                <img src="@/assets/head-logo.svg" alt="">
              </a>
            </el-col>
            <el-col class="nav" :span="15">

              <el-row>
                <el-col :span="2" v-for="(value,index) in category_list" :key="value.id">
                  <router-link :to="value.link" :class="{active:nav_num===index}" @click.native="nav_num=index"
                               v-if="!value.is_site">{{value.title}}
                  </router-link>
                  <a :href="value.link" v-else>{{value.title}}</a>
                </el-col>
              </el-row>
            </el-col>

            <el-col :span="!token?8:10" class="header-right-box">
              <div class="search">
                <input type="text" id="Input" placeholder="请输入想搜索的课程" v-show="!status" ref="Input"
                       @blur="ReChangeStatus">
                <ul class="search-ul" v-show="status" @click="ChangeStatus">
                  <span>Python</span>
                  <span>Linux</span>
                </ul>
                <p>
                  <img class="icon" src="@/assets/sousuo1.png" alt="" v-show="status">
                  <img class="icon" src="@/assets/sousuo2.png" alt="" v-show="!status">
                  <img class="new" src="@/assets/new.png" alt="">
                </p>
              </div>
              <div class="register" v-show="!token">
                <router-link to="/login">
                  <button class="signin">登录</button>
                </router-link>
                &nbsp;&nbsp;|&nbsp;&nbsp;
                <a target="_blank" href="https://www.luffycity.com/signup">
                  <router-link to="/register">
                    <button class="signup">注册</button>
                  </router-link>

                </a>
              </div>
              <div class="shop-car" v-show="token">
                <router-link to="/cart">
                  <b>{{$store.state.cart.cart_length}}</b>
                  <img src="@/assets/shopcart.png" alt="">
                  <span>购物车 </span>
                </router-link>
              </div>
              <div class="nav-right-box" v-show="token">
                <div class="nav-right">
                  <router-link to="/myclass">
                    <div class="nav-study">我的教室</div>
                  </router-link>
                  <div class="nav-img" @mouseover="ShowInfoList" @mouseout="HideInfoList">
                    <img v-for="i in user" :src="i" alt="" style="border: 1px solid rgb(243, 243, 243);">
                    <ul class="home-my-account" v-show="list_status">
                      <li>
                        <router-link to="/account">
                          我的账户
                        </router-link>
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/back_1568185800.821227.svg"
                             alt="">
                      </li>
                      <li>
                        <router-link to="/user/order">
                        我的订单
                        </router-link>
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/back_1568185800.821227.svg"
                             alt="">
                      </li>
                      <li>
                        贝里小卖铺
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/back_1568185800.821227.svg"
                             alt="">
                      </li>
                      <li>
                        我的优惠券
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/back_1568185800.821227.svg"
                             alt="">
                      </li>
                      <li>
                    <span>
                      我的消息
                      <b>(26)</b>
                    </span>
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/back_1568185800.821227.svg"
                             alt="">
                      </li>
                      <li @click="LogoutHandler">
                        退出
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/back_1568185800.821227.svg"
                             alt="">
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-header>
      </el-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      token: false, // 登录与否的状态标识
      status: true,  // input搜索标签与ul标签的状态标识
      list_status: true, // 下拉菜单的显示与否的状态标识
      category_list: [], // 构建顶部导航栏的显示数据
      nav_num: null, // 控制选中顶部导航栏的显示样式
      user: {
        src: ''
      },
    }
  },
  methods: {
    ChangeStatus() {
      this.status = false;
      // console.log(this.$refs);  // {Input: input#Input}
      // this.$refs.Input.focus();  // 还是不生效，vue处理dom操作是异步过程，我们需要先执行改变状态，在执行获取光标
      this.$nextTick(() => {
        this.$refs.Input.focus();
      })
    },

    ReChangeStatus(){
      this.status = true;
    },

    ShowInfoList(){
      this.list_status = true
    },
    HideInfoList(){
      this.list_status = false
    },
    get_nav_data(){
      this.$axios.get(`${this.$settings.Host}/home/nav`).then((res)=>{
        // console.log(res)
        this.category_list = res.data;
      }).catch((error)=>{
        console.log(error)
      })
    },

    check_login_status(){
      this.token = sessionStorage.user_token || localStorage.user_token
    },

    LogoutHandler(){
      localStorage.removeItem('user_token');
      localStorage.removeItem('id');
      localStorage.removeItem('username');
      sessionStorage.removeItem('user_token');
      sessionStorage.removeItem('id');
      sessionStorage.removeItem('username');
      this.check_login_status()
    },

    account_user_id(){
      let user_id = sessionStorage.user_id || localStorage.user_id
      this.$axios.get(`${this.$settings.Host}/users/account/`+ user_id + '/').then((res) => {
        this.user.src = res.data.avatar
      })
    },

    // 验证用户是否登录
    check_user_login() {
      let token = localStorage.user_token || sessionStorage.user_token;
      if (!token) {
        return false
      }
      return token;
    },

    // 先要验证用户是否登录
    get_cart_data() {
      let token = this.check_user_login();

      // 将课程id发送到后端
      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }

      // 请求获取购物车数据
      this.$axios.get(`${this.$settings.Host}/cart/`,{
        headers: {
          'Authorization': 'jwt ' + token,
        }
      }).then(res => {
        // console.log(res.data)
        // this.$message.success(res.data.msg)
        let cart_len = res.data.course_len;
        this.$store.commit('add_cart',cart_len)
      }).catch(error => {
        console.log(error.response)
      })
    }
  },
  created() {
    this.get_nav_data();
    this.check_login_status();
    this.account_user_id();
    this.get_cart_data();
  }
}


</script>

<style scoped>
.header-cont .nav .active {
  color: #f5a623;
  font-weight: 500;
  border-bottom: 2px solid #f5a623;
}

.total-header {
  min-width: 1200px;
  z-index: 100;
  box-shadow: 0 4px 8px 0 hsla(0, 0%, 59%, .1);
}

.header {
  width: 1200px;
  margin: 0 auto;
}

.header .el-header {
  padding: 0;
}

.logo {
  height: 80px;
  display: flex; /* css3里面的弹性布局，高度设定好之后，设置这个属性就能让里面的内容居中 */
  align-items: center;
}

.nav .el-row .el-col {
  height: 80px;
  line-height: 80px;
  text-align: center;

}

.nav a {
  font-size: 15px;
  font-weight: 400;
  cursor: pointer;
  color: #4a4a4a;
  text-decoration: none;
}

.nav .el-row .el-col a:hover {
  border-bottom: 2px solid #f5a623
}

.header-cont {
  position: relative;
}

.search input {
  width: 185px;
  height: 26px;
  font-size: 14px;
  color: #4a4a4a;
  border: none;
  border-bottom: 1px solid #ffc210;

  outline: none;
}

.search ul {
  width: 185px;
  height: 26px;
  display: flex;
  align-items: center;
  padding: 0;

  padding-bottom: 3px;
  border-bottom: 1px solid hsla(0, 0%, 59%, .25);
  cursor: text;
  margin: 0;
  font-family: Helvetica Neue, Helvetica, Microsoft YaHei, Arial, sans-serif;
}

.search .search-ul, .search #Input {
  padding-top: 10px;
}

.search ul span {
  color: #545c63;
  font-size: 12px;
  padding: 3px 12px;
  background: #eeeeef;
  cursor: pointer;
  margin-right: 3px;
  border-radius: 11px;
}


.search {
  height: auto;
  display: flex;
  align-items: center;
}

.search p {
  position: relative;
  margin-right: 20px;
  margin-left: 4px;
}

.search p .icon {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.search p .new {
  width: 18px;
  height: 10px;
  position: absolute;
  left: 15px;
  top: 0;
}

.register {
  height: 36px;
  display: flex;
  align-items: center;
  line-height: 36px;
}

.register .signin, .register .signup {
  font-size: 14px;
  color: #5e5e5e;
  white-space: nowrap;
}

.register button {
  outline: none;
  cursor: pointer;
  border: none;
  background: transparent;
}

.register a {
  color: #000;
  outline: none;
}

.header-right-box {
  height: 100%;
  display: flex;
  align-items: center;
  font-size: 15px;
  color: #4a4a4a;
  position: absolute;
  right: 0;
  top: 0;
}

.shop-car {
  width: 99px;
  height: 28px;
  border-radius: 15px;
  margin-right: 20px;
  background: #f7f7f7;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
}

.shop-car b {
  position: absolute;
  left: 28px;
  top: -1px;
  width: 18px;
  height: 16px;
  color: #fff;
  font-size: 12px;
  font-weight: 350;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background: #ff0826;
  overflow: hidden;
  transform: scale(.8);
}

.shop-car img {
  width: 20px;
  height: 20px;
  margin-right: 7px;
}

.nav-right-box {
  position: relative;
}

.nav-right-box .nav-right {
  float: right;
  display: flex;
  height: 100%;
  line-height: 60px;
  position: relative;
}

.nav-right .nav-study {
  font-size: 15px;
  font-weight: 300;
  color: #5e5e5e;
  margin-right: 20px;
  cursor: pointer;

}

.nav-right .nav-study:hover {
  color: #000;
}

.nav-img img {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: inline-block;
  cursor: pointer;
}

.home-my-account {
  position: absolute;
  right: 0;
  top: 60px;
  z-index: 101;
  width: 190px;
  height: auto;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 4px 8px 0 #d0d0d0;
}

li {
  list-style: none;
}

.home-my-account li {
  height: 40px;
  font-size: 14px;
  font-weight: 300;
  color: #5e5e5e;
  padding-left: 20px;
  padding-right: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}

.home-my-account li img {
  cursor: pointer;
  width: 5px;
  height: 10px;
}

.home-my-account li span {
  height: 40px;
  display: flex;
  align-items: center;
}

.home-my-account li span b {
  font-weight: 300;
  margin-top: -2px;
}


</style>

