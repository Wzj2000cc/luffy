<!--<template>-->
<!--  <div data-v-501dc584>-->
<!--    <Header></Header>-->
<!--    <main class="information" data-v-f06ef9a0 data-v-501dc584 data-v-501dc584>-->
<!--      <div class="wrapper" data-v-f06ef9a0>-->
<!--        <div data-v-f06ef9a0>-->
<!--          <div class="info-content" data-v-f06ef9a0>-->
<!--            <dl class="info-left" data-v-f06ef9a0>-->
<!--              <dt data-v-f06ef9a0>-->
<!--                <div data-v-f06ef9a0>-->
<!--                  <img alt="用户头像" class="new-img" data-v-f06ef9a0 v-for="i in user" :src="i">-->
<!--                  <div class="camera-icon" style="display:none;" data-v-f06ef9a0>-->

<!--                  </div>-->
<!--                </div>-->
<!--              </dt>-->
<!--              <dd data-v-f06ef9a0>-->
<!--                <h4 data-v-f06ef9a0>-->
<!--                </h4>-->
<!--                <p class="city" data-v-f06ef9a0>-->
<!--                  <span data-v-f06ef9a0>国籍：中国</span>-->
<!--                </p>-->
<!--                <p class="signature" data-v-f06ef9a0>个性签名：我真是个小天才 ~-->
<!--                </p>-->
<!--              </dd>-->
<!--            </dl>-->
<!--            <div class="base-info" data-v-f06ef9a0>-->
<!--              <div class="info-tit-wrap" data-v-f06ef9a0>-->
<!--                <h5 class="info-tit" data-v-f06ef9a0>基本信息</h5>-->
<!--                <button class="edit-btn" data-v-f06ef9a0>-->
<!--                  <img src="//hcdn2.luffycity.com/media/frontend/activity/edit_icon_1564127720.1136944.png"-->
<!--                       data-v-f06ef9a0>-->
<!--                  修改-->
<!--                </button>-->
<!--              </div>-->
<!--              <ul class="base-info-wrap" data-v-f06ef9a0>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>用 户 名</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>{{ name }}</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>微 信</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>{{ Wechat }}</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>学 历</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>博士后</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>性 别</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>男</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>生 日</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>2000.11.26</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>QQ 号</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>2530065079</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>收件地址</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>未填写</span>-->
<!--                </li>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0> 签 名</label>-->
<!--                  <span class="label-point" data-v-f06ef9a0>我真是个小天才 ~</span>-->
<!--                </li>-->
<!--              </ul>-->
<!--            </div>-->
<!--            <div class="base-info" data-v-f06ef9a0>-->
<!--              <div class="info-tit-wrap" data-v-f06ef9a0>-->
<!--                <h5 class="info-tit" data-v-f06ef9a0>认证信息</h5>-->
<!--              </div>-->
<!--              <ul class="base-info-wrap" data-v-f06ef9a0>-->
<!--                <li class="base-info-item" data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>实名认证</label>-->
<!--                  <span class="label-point certification" data-v-f06ef9a0>-->
<!--                未认证-->
<!--              </span>-->
<!--                </li>-->
<!--              </ul>-->
<!--            </div>-->
<!--            <div class="base-info" data-v-f06ef9a0>-->
<!--              <div class="info-tit-wrap" data-v-f06ef9a0>-->
<!--                <h5 class="info-tit" data-v-f06ef9a0>账户安全</h5>-->
<!--              </div>-->
<!--              <div class="security" data-v-f06ef9a0>-->
<!--                <div data-v-f06ef9a0>-->
<!--                  <label class="label" data-v-f06ef9a0>手 机</label>-->
<!--                  <span class="spli" data-v-f06ef9a0>{{ mobile }}</span>-->
<!--                  <span class="modify-text" data-v-f06ef9a0>-->
<!--                <span data-v-f06ef9a0>绑定手机</span>-->
<!--              </span>-->
<!--                </div>-->
<!--                <div data-v-f06ef9a0><label class="label" data-v-f06ef9a0>邮 箱</label> <span class="spli"-->
<!--                                                                                            data-v-f06ef9a0>{{ email }}</span>-->
<!--                  <span class="modify-text" data-v-f06ef9a0><span data-v-f06ef9a0>绑定邮箱</span></span></div>-->
<!--                <div data-v-f06ef9a0><label class="label" data-v-f06ef9a0>登录密码</label> <span class="spli"-->
<!--                                                                                             data-v-f06ef9a0>未设置密码</span>-->
<!--                  <span class="modify-text" data-v-f06ef9a0><span data-v-f06ef9a0>设置密码</span></span></div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="base-info" data-v-f06ef9a0>-->
<!--              <div class="info-tit-wrap" data-v-f06ef9a0><h5 class="info-tit" data-v-f06ef9a0>职业信息</h5></div>-->
<!--              <div class="professional" data-v-f06ef9a0>-->
<!--                <div class="professional-module" data-v-f06ef9a0><label class="label" data-v-f06ef9a0>职 业</label> <span-->
<!--                  class="spli" data-v-f06ef9a0>未设置</span> <span class="modify-text" data-v-f06ef9a0>修改</span></div>-->
<!--                &lt;!&ndash;&ndash;&gt;-->
<!--                <div class="professional-module" data-v-f06ef9a0><label class="label" data-v-f06ef9a0>感 兴 趣</label>-->
<!--                  <div data-v-f06ef9a0><span class="spli" data-v-f06ef9a0>未设置</span></div>-->
<!--                  <span class="modify-text" data-v-f06ef9a0>添加感兴趣的职业方向</span></div> &lt;!&ndash;&ndash;&gt;</div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div> &lt;!&ndash;&ndash;&gt;</main>-->
<!--    <Footer></Footer>-->
<!--  </div>-->
<!--</template>-->


<!--<script>-->
<!--  import Header from "./common/Header";-->
<!--  import Footer from "./common/Footer";-->
<!--  export default {-->
<!--    name: "Edit",-->
<!--    components:{-->
<!--      Header,-->
<!--      Footer-->
<!--    },-->
<!--    data() {-->
<!--      return {-->
<!--        status:true,-->
<!--        name: '',-->
<!--        mobile: '',-->
<!--        email: '',-->
<!--        Wechat: '',-->
<!--        user: {-->
<!--          src: ''-->
<!--        }-->
<!--      }-->
<!--    },-->
<!--    methods: {-->
<!--      submit() {-->
<!--        this.$axios.post(`${this.$settings.Host}/users/account/1/`, {-->
<!--          name: this.name,-->
<!--          area: this.area, population: this.population, gdp: this.gdp-->
<!--        })-->
<!--          .then((request) => {-->
<!--            location.href = 'http://localhost:8080/#/' // 请求成功以后的回调函数-->
<!--          })-->
<!--      },-->
<!--    },-->
<!--    created() {-->
<!--      let user_id = sessionStorage.user_id-->
<!--      this.$axios.get(`${this.$settings.Host}/users/account/`+ user_id + '/').then((res) => {-->
<!--        this.id = res.data.id-->
<!--        this.name = res.data.username-->
<!--        this.mobile = res.data.mobile-->
<!--        this.email = res.data.email-->
<!--        this.Wechat = res.data.Wechat-->
<!--        this.user.src = res.data.avatar-->
<!--      })-->
<!--    }-->
<!--  }-->
<!--</script>-->


<template>
  <div data-v-501dc584>
    <Header></Header>
    <main class="information" data-v-f06ef9a0 data-v-501dc584 data-v-501dc584>
      <div class="wrapper" data-v-f06ef9a0>
        <div data-v-f06ef9a0>
          <div class="info-content" data-v-f06ef9a0>
            <dl class="info-left" data-v-f06ef9a0>
              <dt data-v-f06ef9a0>
                <div data-v-f06ef9a0>
                  <img alt="用户头像" class="new-img" data-v-f06ef9a0 v-for="i in user" :src="i">
                  <div class="camera-icon" style="display:none;" data-v-f06ef9a0>

                  </div>
                </div>
              </dt>
              <dd data-v-f06ef9a0>
                <h4 data-v-f06ef9a0>

                </h4>
                <p class="city" data-v-f06ef9a0>
                  <span data-v-f06ef9a0>  中国</span>
                </p>
                <p class="signature" data-v-f06ef9a0>这个人很懒，什么有没有留下 ~
                </p>
              </dd>
            </dl>
            <div class="base-info" data-v-f06ef9a0>
              <div class="info-tit-wrap" data-v-f06ef9a0>
                <div data-v-f06ef9a0="" :class="{div1:!status,div2:status}"><p data-v-f06ef9a0="" class="user-name"><span
                  data-v-f06ef9a0="" class="name" style="display: inline !important;">路飞用户8nyN</span>，请填写真实资料
                </p>
                  <div data-v-f06ef9a0="">
                    <ul data-v-f06ef9a0="" class="edit-cont">
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">
                        微信
                        <span data-v-f06ef9a0="" class="edit-error"></span></label> <input data-v-f06ef9a0=""
                                                                                           type="text" placeholder="微信"
                                                                                           class="edit-input" v-model="WeChart"></li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">
                        学历
                        <span data-v-f06ef9a0="" class="edit-error"></span></label>
                          <select data-v-f06ef9a0=""class="edit-input" v-model="education">
                            <option v-for="(item,index) in list" :value="item" :key="index">{{item}}</option>
                        </select>
                      </li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">性别<span
                        data-v-f06ef9a0="" class="edit-error"></span></label>
                        <div data-v-f06ef9a0=""><input data-v-f06ef9a0="" type="text"
                                                       placeholder="请输入性别 ~"
                                                       class="edit-input" v-model="sex">

                        </div>
                      </li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">
                        生日<span data-v-f06ef9a0="" class="edit-error"></span></label> <input data-v-f06ef9a0=""
                                                                                             type="text"
                                                                                             placeholder="出生年月，格式例如：1996-03-12"
                                                                                             class="edit-input" v-model="birthday"></li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">QQ邮箱<span
                        data-v-f06ef9a0="" class="edit-error"></span></label> <input data-v-f06ef9a0="" type="text"
                                                                                     placeholder="QQ邮箱"
                                                                                     class="edit-input" v-model="email"></li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">收件地址<span
                        data-v-f06ef9a0="" class="edit-error"></span></label> <input data-v-f06ef9a0="" type="text"
                                                                                     placeholder="地址用于资料、发票的邮寄，请认真填写 ~ "
                                                                                     class="edit-input" v-model="address"></li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">手机号<span
                        data-v-f06ef9a0="" class="edit-error"></span></label> <input data-v-f06ef9a0="" type="text"
                                                                                     placeholder="请输入手机号 ~"
                                                                                     class="edit-input" v-model="mobile"></li>
                      <li data-v-f06ef9a0="" class="edit-list"><label data-v-f06ef9a0="" class="edit-label">签名<span
                        data-v-f06ef9a0="" class="edit-error"></span></label> <input data-v-f06ef9a0="" type="text"
                                                                                     placeholder="说点什么吧 ~"
                                                                                     class="edit-input" v-model="autograph"></li>
                    </ul>
                  </div>
                  <div data-v-f06ef9a0="" class="" style="text-align: center; margin-top: 20px;">
                    <button data-v-f06ef9a0="" class="modify-btn modify-cancel-btn" @click="change2">
                      取消
                    </button>
                    <button data-v-f06ef9a0="" class="modify-btn modify-sure-btn" @click="change1" >
                      完成
                    </button>
                  </div>
                </div>
                <div :class="{div1:status,div2:!status}" >
                  <h5 class="info-tit" data-v-f06ef9a0>基本信息</h5>
                  <button class="edit-btn" data-v-f06ef9a0 @click="change" style="margin-left: 1000px; margin-bottom: 5px">
                    <img src="//hcdn2.luffycity.com/media/frontend/activity/edit_icon_1564127720.1136944.png"
                         data-v-f06ef9a0>
                    修改
                  </button>
                  <ul class="base-info-wrap" data-v-f06ef9a0>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>用 户 名</label>
                      <span class="label-point" data-v-f06ef9a0>{{username}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>微 信</label>
                      <span class="label-point" data-v-f06ef9a0>{{WeChart}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>学 历</label>
                      <span class="label-point" data-v-f06ef9a0>{{education}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>性 别</label>
                      <span class="label-point" data-v-f06ef9a0>{{sex}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>生 日</label>
                      <span class="label-point" data-v-f06ef9a0>{{birthday}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>QQ 号</label>
                      <span class="label-point" data-v-f06ef9a0>{{email}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>收件地址</label>
                      <span class="label-point" data-v-f06ef9a0>{{address}}</span>
                    </li>
                    <li class="base-info-item" data-v-f06ef9a0>
                      <label class="label" data-v-f06ef9a0>签 名</label>
                      <span class="label-point" data-v-f06ef9a0>{{autograph}}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="base-info" data-v-f06ef9a0>
              <div class="info-tit-wrap" data-v-f06ef9a0>
                <h5 class="info-tit" data-v-f06ef9a0>认证信息</h5>
              </div>
              <ul class="base-info-wrap" data-v-f06ef9a0>
                <li class="base-info-item" data-v-f06ef9a0>
                  <label class="label" data-v-f06ef9a0>实名认证</label>
                  <span class="label-point certification" data-v-f06ef9a0>
                {{asd}}
              </span>
                </li>
              </ul>
            </div>
            <div class="base-info" data-v-f06ef9a0>
              <div class="info-tit-wrap" data-v-f06ef9a0>
                <h5 class="info-tit" data-v-f06ef9a0>账户安全</h5>
              </div>
              <div class="security" data-v-f06ef9a0>
                <div data-v-f06ef9a0>
                  <label class="label" data-v-f06ef9a0>手 机</label>
                  <span class="spli" data-v-f06ef9a0>{{mobile}}</span>
                  <span class="modify-text" data-v-f06ef9a0>
                <span data-v-f06ef9a0>绑定手机</span>
              </span>
                </div>
                <div data-v-f06ef9a0><label class="label" data-v-f06ef9a0>邮 箱</label> <span class="spli"
                                                                                            data-v-f06ef9a0>{{email}}</span>
                  <span class="modify-text" data-v-f06ef9a0><span data-v-f06ef9a0>绑定邮箱</span></span></div>
              </div>
            </div>
            <div class="base-info" data-v-f06ef9a0>
              <div class="info-tit-wrap" data-v-f06ef9a0><h5 class="info-tit" data-v-f06ef9a0>职业信息</h5></div>
              <div class="professional" data-v-f06ef9a0>
                <div class="professional-module" data-v-f06ef9a0><label class="label" data-v-f06ef9a0>职 业</label> <span
                  class="spli" data-v-f06ef9a0>未设置</span> <span class="modify-text" data-v-f06ef9a0>修改</span></div>
                <!---->
                <div class="professional-module" data-v-f06ef9a0><label class="label" data-v-f06ef9a0>感 兴 趣</label>
                  <div data-v-f06ef9a0><span class="spli" data-v-f06ef9a0>未设置</span></div>
                  <span class="modify-text" data-v-f06ef9a0>添加感兴趣的职业方向</span></div> <!----></div>

            </div>
          </div>
        </div>
      </div> <!----></main>
    <Footer></Footer>
  </div>


</template>

<script>
import Footer from "./common/Footer";
import Header from "./common/Header";

export default {
  name: "material",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      asd:'未认证',
      id: '',
      username: '',
      mobile: '',
      email: '',
      WeChart: '',
      address:'',  // 收件地址
      autograph:'', // 个性签名
      birthday:'',
      sex:'',
      password:'',
      education:'请选择学历',
      list:['请选择学历','高中以下','中专/高中','大专','本科','研究生','硕士','博士'],
      user:{
        src:''
      },
      status:0,
    }
  },
  methods: {
    change(){
      this.status=1
    },
    change1(){
      this.asd='已认证';
      let id=sessionStorage.user_id || localStorage.user_id;
      this.status=0;
      this.$axios.put(`${this.$settings.Host}/users/account/`+id+'/',{
        'Wechat':this.WeChart,
        'email':this.email,
        'username':this.username,
        'mobile':this.mobile,
        'address':this.address,
        'autograph':this.autograph,
        'birthday':this.birthday,
        'education':this.education,
        'sex':this.sex,
        'password':this.password
      }).then(data=>{
        console.log(this.education)
      }).catch(error => {
        console.log(error)
      })
    },
    change2(){
      this.status=0;
      let id=sessionStorage.user_id || localStorage.user_id;
      this.$axios.get(`${this.$settings.Host}/users/account/`+id+'/').then(data => {
        this.username = data.data.username;
        this.mobile = data.data.mobile;
        this.email = data.data.email;
        this.WeChart = data.data.Wechat;
        this.user.src=data.data.avatar;
        this.address = data.data.address;
        this.autograph = data.data.autograph;
        this.birthday = data.data.birthday;
        this.education = data.data.education;
        this.sex = data.data.sex
      }).catch(error => {
        console.log(error)
      })
    }
  },


  created() {
    let id=sessionStorage.user_id || localStorage.user_id;
    console.log(id);
    this.$axios.get(`${this.$settings.Host}/users/account/`+id+'/').then(data => {
      this.password = data.data.password;
      this.username = data.data.username;
      this.mobile = data.data.mobile;
      this.email = data.data.email;
      this.WeChart = data.data.Wechat;
      this.user.src=data.data.avatar;
      this.address = data.data.address;
      this.autograph = data.data.autograph;
      this.birthday = data.data.birthday;
      this.education = data.data.education;
      this.sex = data.data.sex
    }).catch(error => {
      console.log(error)
    })
  }
}
</script>


<style scoped data-vue-ssr-id="765b275c:0 1f7d01ce:0 e955a574:0 ef6dde7e:0 4c5998dc:0 6f66de3d:0 5ebdb826:0 6998d1ff:0">
:after, :before {
  box-sizing: border-box;
  margin: 0;
  padding: 0
}
.div1{
  display: none;
}
.div2{
  display: block;
}
#__layout, #__nuxt, #app {
  width: 100%;
  height: 100vh;
  min-height: 100% !important
}

html {
  width: 100%;
  height: 100%;
  min-height: 100vh;
  font-family: Helvetica Neue, Helvetica, Microsoft YaHei, Arial, sans-serif;
  font-size: 16px;
  word-spacing: 0;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box
}

body {
  line-height: 1.42857143;
  font-size: 14px;
  min-height: 100%;
  min-height: 100vh;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  background: #fff !important
}

#routerView, body {
  display: flexbox;
  display: flex
}

#routerView {
  width: 100%;
  -prefix-box-flex: 1;
  flex: 1;
  flex-grow: 1;
  flex-direction: column
}

hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible
}

img {
  border-style: none;
  display: inline-block
}

a {
  text-decoration: none !important
}

a, button, input, optgroup, select, textarea {
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0)
}

a, img {
  -webkit-touch-callout: none
}

blockquote, body, button, code, dd, div, dl, dt, fieldset, form, h1, h2, h3, h4, h5, h6, input, legend, li, ol, p, pre, strong, td, textarea, th, ul {
  padding: 0;
  margin: 0;
  font-family: Helvetica Neue, Helvetica, Microsoft YaHei, Arial, sans-serif
}

img {
  border: 0;
  vertical-align: middle
}

a {
  text-decoration: none;
  color: #000;
  outline: none
}

li {
  list-style: none
}

div, h1, h2, h3, h4, h5, h6, p, section, span {
  -webkit-margin-before: 0;
  -webkit-margin-after: 0
}

.clearfix:after {
  content: "\200B";
  clear: both;
  display: block;
  height: 0
}

button {
  cursor: pointer;
  border: none;
  background: transparent
}

i {
  font-style: normal
}

input, select, textarea {
  border: none;
  outline: none
}

select {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
  background: transparent
}

select::-ms-expand {
  display: none
}

button {
  outline: none
}

input:-webkit-autofill {
  　　-webkit-box-shadow: 0 0 0 1000px #fff inset
}

.view[data-v-f810d444] {
  display: flex;
  flex-direction: column;
  min-height: 100vh
}

.view .main[data-v-f810d444] {
  display: flex;
  flex-direction: column;
  flex: 1
}

.hide[data-v-5bb2aec2] {
  display: none
}

header[data-v-5bb2aec2] {
  min-width: 1200px;
  z-index: 100;
  box-shadow: 0 4px 8px 0 hsla(0, 0%, 59.2%, .1)
}

.active-top[data-v-5bb2aec2] {
  width: 100%;
  height: 52px;
  background: linear-gradient(117deg, #ff4080, #ffa700);
  box-shadow: 0 4px 8px 0 hsla(0, 0%, 81.6%, .49);
  text-align: center
}

.active-top a[data-v-5bb2aec2] {
  color: #fff;
  font-size: 16px;
  line-height: 52px;
  width: 100%;
  height: 100%;
  display: inline-block
}

.active-top a i[data-v-5bb2aec2] {
  font-style: normal;
  margin-left: 32px;
  display: inline-block
}

.header[data-v-5bb2aec2] {
  width: 100%;
  height: 60px;
  background: #fff;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  border-bottom: 1px solid hsla(0, 0%, 59.2%, .1)
}

.header .header-cont[data-v-5bb2aec2] {
  width: 1200px;
  height: 100%;
  display: flex;
  align-items: center;
  position: relative
}

.header .header-cont .left[data-v-5bb2aec2] {
  display: flex;
  align-items: center;
  position: absolute;
  left: 0;
  top: 12px
}

.header .header-cont .logo[data-v-5bb2aec2] {
  width: 118px;
  height: auto;
  cursor: pointer;
  margin-right: 50px
}

.header .header-cont .nav[data-v-5bb2aec2] {
  width: auto;
  height: 36px;
  display: flex;
  line-height: 36px;
  margin-left: 160px
}

.header .header-cont .nav a[data-v-5bb2aec2] {
  height: 36px;
  display: inline-block;
  margin-right: 30px
}

.header .header-cont .nav a li[data-v-5bb2aec2] {
  font-size: 15px;
  font-weight: 400;
  cursor: pointer;
  color: #4a4a4a
}

.header .header-cont .nav a[data-v-5bb2aec2]:last-child {
  margin-right: 0
}

.header .header-cont .nav a.active-link[data-v-5bb2aec2], .header .header-cont .nav a[data-v-5bb2aec2]:hover {
  border-bottom: 2px solid #f5a623
}

.header .header-cont .nav a.active-link li[data-v-5bb2aec2] {
  color: #f5a623;
  font-weight: 500
}

.header .header-cont .header-right-box[data-v-5bb2aec2] {
  height: 100%;
  display: flex;
  align-items: center;
  font-size: 15px;
  color: #4a4a4a;
  position: absolute;
  right: 0;
  top: 0
}

.header .header-cont .header-right-box .search[data-v-5bb2aec2] {
  height: auto;
  display: flex
}

.header .header-cont .header-right-box .search input[data-v-5bb2aec2] {
  width: 185px;
  height: 26px;
  font-size: 14px;
  color: #4a4a4a;
  border-bottom: 1px solid #ffc210
}

.header .header-cont .header-right-box .search[data-v-5bb2aec2] ::-webkit-input-placeholder {
  color: #9d9d9d
}

.header .header-cont .header-right-box .search[data-v-5bb2aec2] :-moz-placeholder, .header .header-cont .header-right-box .search[data-v-5bb2aec2] ::-moz-placeholder {
  color: #9d9d9d
}

.header .header-cont .header-right-box .search[data-v-5bb2aec2] :-ms-input-placeholder {
  color: #9d9d9d
}

.header .header-cont .header-right-box .search ul[data-v-5bb2aec2] {
  width: 185px;
  height: 26px;
  display: flex;
  align-items: center;
  padding-bottom: 3px;
  border-bottom: 1px solid hsla(0, 0%, 59.2%, .25);
  cursor: text
}

.header .header-cont .header-right-box .search ul span[data-v-5bb2aec2] {
  color: #545c63;
  font-size: 12px;
  padding: 3px 12px;
  background: #eeeeef;
  cursor: pointer;
  margin-right: 3px;
  border-radius: 11px
}

.header .header-cont .header-right-box .search p[data-v-5bb2aec2] {
  position: relative;
  margin-right: 20px;
  margin-left: 4px
}

.header .header-cont .header-right-box .search p .icon[data-v-5bb2aec2] {
  width: 16px;
  height: 16px;
  cursor: pointer
}

.header .header-cont .header-right-box .search p .new[data-v-5bb2aec2] {
  width: 18px;
  height: 10px;
  position: absolute;
  left: 15px;
  top: 0
}

.header .header-cont .header-right-box .shop-cart[data-v-5bb2aec2] {
  width: 99px;
  height: 28px;
  border-radius: 15px;
  margin-right: 20px;
  background: #f7f7f7;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer
}

.header .header-cont .header-right-box .shop-cart img[data-v-5bb2aec2] {
  width: 20px;
  height: 20px;
  margin-right: 7px
}

.header .header-cont .header-right-box .shop-cart span[data-v-5bb2aec2] {
  font-size: 14px;
  font-weight: 300;
  color: #5e5e5e
}

.header .header-cont .header-right-box .shop-cart b[data-v-5bb2aec2] {
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
  transform: scale(.8)
}

.header .header-cont .header-right-box .shop_car:hover span[data-v-5bb2aec2] {
  color: #000 !important
}

.header .header-cont .header-right-box .auth-button[data-v-5bb2aec2] {
  height: 36px;
  display: flex;
  align-items: center;
  line-height: 36px
}

.header .header-cont .header-right-box .auth-button .signin[data-v-5bb2aec2], .header .header-cont .header-right-box .auth-button .signup[data-v-5bb2aec2] {
  cursor: pointer;
  border-radius: 4px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  white-space: nowrap;
  font-weight: 500
}

.header .header-cont .header-right-box .auth-button .signin[data-v-5bb2aec2] {
  width: 76px;
  border: 1px solid #ffc210;
  color: #ffc210;
  margin-right: 14px;
  margin-left: 5px
}

.header .header-cont .header-right-box .auth-button .signup[data-v-5bb2aec2] {
  width: 98px;
  background: #ffc210;
  color: #fff
}

.header .header-cont .header-right-box .auth-button .signin[data-v-5bb2aec2]:hover {
  color: #f5a623;
  border: 1px solid #f5a623
}

.header .header-cont .header-right-box .auth-button .signup[data-v-5bb2aec2]:hover {
  background: #f5a623
}

.header .header-cont .header-right-box .nav-right-box[data-v-5bb2aec2] {
  position: relative
}

.header .header-cont .header-right-box .nav-right-box .nav-right[data-v-5bb2aec2] {
  float: right;
  display: flex;
  height: 100%;
  line-height: 60px;
  position: relative
}

.header .header-cont .header-right-box .nav-right-box .nav-right .nav-study[data-v-5bb2aec2] {
  font-size: 15px;
  font-weight: 300;
  color: #5e5e5e;
  margin-right: 20px
}

.header .header-cont .header-right-box .nav-right-box .nav-right .nav-study[data-v-5bb2aec2]:hover {
  color: #000
}

.header .header-cont .header-right-box .nav-right-box .nav-right div[data-v-5bb2aec2] {
  line-height: 60px;
  cursor: pointer
}

.header .header-cont .header-right-box .nav-right-box .nav-right div[data-v-5bb2aec2]:first-child {
  padding-left: 0
}

.header .header-cont .header-right-box .nav-right-box .nav-right div[data-v-5bb2aec2]:last-child {
  padding-right: 0
}

.header .header-cont .header-right-box .nav-right-box .nav-right img[data-v-5bb2aec2] {
  width: 22px;
  height: 22px;
  cursor: pointer
}

.header .header-cont .header-right-box .nav-right-box .nav-right .nav-img span[data-v-5bb2aec2] {
  width: 100px;
  height: auto;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden
}

.header .header-cont .header-right-box .nav-right-box .nav-right .nav-img img[data-v-5bb2aec2] {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: inline-block;
  border: 1px solid #f3f3f3
}

.header .header-cont .header-right-box .nav-right-box .nav-right .nav-img .this[data-v-5bb2aec2] {
  border: 1px solid #ffc210
}

.header .header-cont .header-right-box .nav-right-box .nav-right .home-my-account[data-v-5bb2aec2] {
  position: absolute;
  right: 0;
  top: 60px;
  z-index: 101;
  width: 190px;
  height: auto;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 4px 8px 0 #d0d0d0
}

.header .header-cont .header-right-box .nav-right-box .nav-right .home-my-account li[data-v-5bb2aec2] {
  display: block;
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
  box-sizing: border-box
}

.header .header-cont .header-right-box .nav-right-box .nav-right .home-my-account li span[data-v-5bb2aec2] {
  height: 40px;
  display: flex;
  align-items: center
}

.header .header-cont .header-right-box .nav-right-box .nav-right .home-my-account li b[data-v-5bb2aec2] {
  font-weight: 300;
  margin-top: -2px
}

.header .header-cont .header-right-box .nav-right-box .nav-right .home-my-account li img[data-v-5bb2aec2] {
  width: 5px;
  height: 10px
}

.header .header-cont .header-right-box .nav-right-box .nav-right .home-my-account li[data-v-5bb2aec2]:hover {
  color: #000;
  font-weight: 400;
  background: #f5f7f9
}

.my[data-v-501dc584] {
  background: #f9f9f9;
  align-items: center
}

.my[data-v-501dc584], .my .children[data-v-501dc584] {
  flex: 1;
  display: flex;
  flex-direction: column
}

.my-tab[data-v-501dc584] {
  width: 100%;
  height: auto;
  cursor: pointer;
  background: #fff;
  box-shadow: 0 2px 4px 1px #f3f3f3;
  justify-content: center
}

.my-tab[data-v-501dc584], .my-tab ul[data-v-501dc584] {
  display: flex;
  align-items: center
}

.my-tab ul[data-v-501dc584] {
  width: 1200px;
  height: 50px
}

.my-tab ul a[data-v-501dc584] {
  margin-right: 30px;
  padding-bottom: 3px;
  font-size: 15px;
  font-weight: 400;
  color: #5e5e5e;
  font-family: PingFangSC-Regular
}

.my-tab ul a[data-v-501dc584]:hover {
  color: #333
}

.my-tab ul .active-link[data-v-501dc584] {
  font-weight: 500;
  color: #333 !important;
  font-family: PingFangSC-Medium;
  box-shadow: 0 2px 0 0 #f5a623
}

.wrapper[data-v-f06ef9a0] {
  width: 1200px;
  height: auto;
  margin: 0 auto;
  white-space: nowrap
}

.modify-text[data-v-f06ef9a0] {
  font-size: 14px;
  color: #4a90e2;
  display: inline-block;
  margin-left: 17px;
  cursor: pointer;
  font-family: PingFangSC-Regular
}

.label-point[data-v-f06ef9a0] {
  flex: 1;
  color: #5e5e5e;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap
}

.label[data-v-f06ef9a0], .label-point[data-v-f06ef9a0] {
  font-size: 14px;
  font-weight: 400;
  display: inline-block;
  font-family: PingFangSC-Regular
}

.label[data-v-f06ef9a0] {
  padding: 0;
  color: #9b9b9b;
  margin-bottom: 0;
  line-height: 20px;
  margin-right: 20px;
  text-align: left
}

.info-tit-wrap[data-v-f06ef9a0] {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 30px;
  font-family: PingFangSC-Regular
}

.professional[data-v-f06ef9a0] {
  width: 100%;
  margin-left: 14px
}

.professional .professional-module[data-v-f06ef9a0] {
  margin-right: 40px;
  margin-bottom: 20px;
  display: flex;
  align-items: center
}

.professional .professional-module .spli[data-v-f06ef9a0] {
  font-size: 14px;
  font-weight: 400;
  font-family: PingFangSC-Regular;
  color: #5e5e5e
}

.professional .professional-module[data-v-f06ef9a0]:last-child {
  margin-bottom: 0
}

.professional .professional-module:last-child div[data-v-f06ef9a0] {
  display: flex;
  align-items: center
}

.professional .professional-module:last-child div .spli[data-v-f06ef9a0] {
  margin-right: 20px;
  font-family: PingFangSC-Regular
}

.professional .professional-module:last-child div .spli[data-v-f06ef9a0]:last-child {
  margin-right: 0 !important;
  font-family: PingFangSC-Regular
}

.edit-btn[data-v-f06ef9a0] {
  font-size: 12px;
  color: #4a4a4a;
  display: flex;
  align-items: center
}

.edit-btn img[data-v-f06ef9a0] {
  width: 14px;
  height: auto;
  margin-right: 10px
}

.info-tit[data-v-f06ef9a0] {
  font-size: 18px;
  color: #4a4a4a;
  margin: 0
}

.base-info[data-v-f06ef9a0] {
  margin-bottom: 20px
}

.base-info-wrap[data-v-f06ef9a0] {
  display: flex;
  flex-wrap: wrap;
  margin-left: 14px
}

.base-info-wrap .base-info-item[data-v-f06ef9a0] {
  width: 30%;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  margin-right: 56px
}

.base-info-wrap .base-info-item[data-v-f06ef9a0]:nth-of-type(3n) {
  margin-right: 0
}

.info-content[data-v-f06ef9a0] {
  width: 1200px;
  min-height: 480px;
  margin-top: 20px;
  background: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 4px 1px hsla(0, 0%, 95.3%, .5);
  padding: 30px;
  box-sizing: border-box
}

.info-content .info-left[data-v-f06ef9a0] {
  width: 100%;
  display: flex;
  align-items: center;
  margin-bottom: 30px
}

.info-content .info-left dt[data-v-f06ef9a0] {
  width: 80px;
  height: 80px;
  cursor: pointer;
  border-radius: 4px;
  margin-right: 12px;
  position: relative;
  overflow: hidden
}

.info-content .info-left dt .new-img[data-v-f06ef9a0], .info-content .info-left dt div[data-v-f06ef9a0] {
  width: 100%;
  height: 100%
}

.info-content .info-left dt .camera-icon[data-v-f06ef9a0] {
  text-align: center;
  position: absolute;
  left: 0;
  top: 0;
  z-index: 10;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: rgba(74, 73, 74, .6) url(//hcdn2.luffycity.com/media/frontend/activity/camera_1564141047.1900802.svg) no-repeat 25px 25px;
  background-size: 30px
}

.info-content .info-left dd[data-v-f06ef9a0] {
  flex: 1;
  overflow: hidden;
  font-weight: 400;
  font-family: PingFangSC-Regular
}

.info-content .info-left dd h4[data-v-f06ef9a0] {
  color: #000;
  font-size: 18px;
  margin: 0 0 8px
}

.info-content .info-left dd .city[data-v-f06ef9a0] {
  display: flex;
  align-items: center;
  margin-bottom: 10px
}

.info-content .info-left dd .city span[data-v-f06ef9a0] {
  display: block;
  font-size: 12px;
  color: #9b9b9b
}

.info-content .info-left dd .city i[data-v-f06ef9a0] {
  color: #9b9b9b;
  font-style: normal
}

.info-content .info-left dd .signature[data-v-f06ef9a0] {
  width: 100%;
  font-size: 14px;
  color: #5e5e5e;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap
}

.info-content dl[data-v-f06ef9a0] {
  margin-bottom: 0
}

.information[data-v-f06ef9a0] {
  margin-bottom: 63px
}

li[data-v-f06ef9a0] {
  list-style: none
}

.edit-base-wrap[data-v-f06ef9a0] {
  margin-bottom: 50px
}

.user-name[data-v-f06ef9a0] {
  font-size: 12px;
  color: #5e5e5e;
  letter-spacing: .19px;
  margin-bottom: 21px
}

.user-name > .name[data-v-f06ef9a0] {
  font-size: 16px;
  color: #333;
  letter-spacing: .25px
}

.edit-label[data-v-f06ef9a0] {
  font-size: 14px;
  color: #4a4a4a;
  display: inline-block
}

.edit-label .edit-error[data-v-f06ef9a0] {
  margin-left: 6px;
  color: #fd7b4d
}

.edit-input[data-v-f06ef9a0] {
  padding: 0 10px;
  width: 100%;
  border: 1px solid #d0d0d0;
  border-radius: 3px;
  height: 42px;
  font-size: 14px;
  color: #4a4a4a;
  font-family: PingFangSC-Regular
}

.edit-input.active[data-v-f06ef9a0] {
  border: 1px solid #ffc210
}

.edit-input.error[data-v-f06ef9a0] {
  border: 1px solid #fd7b4d
}

.edit-cont[data-v-f06ef9a0] {
  width: 100%;
  display: flex;
  flex-wrap: wrap
}

.edit-cont li[data-v-f06ef9a0] {
  margin-right: 40px
}

.edit-cont li[data-v-f06ef9a0]:nth-of-type(3n) {
  margin-right: 0
}

.edit-list[data-v-f06ef9a0] {
  width: 336px;
  list-style: none;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column
}

.sex-input[data-v-f06ef9a0] {
  width: 157px;
  text-align: center;
  background: #fff
}

.woman-spec[data-v-f06ef9a0] {
  margin-left: 16px
}

.sex-input-active[data-v-f06ef9a0] {
  border: 1px solid #ffc210;
  border-radius: 2px
}

.select-input[data-v-f06ef9a0] {
  display: block;
  border: 1px solid #d0d0d0;
  border-radius: 3px
}

.modify-btn[data-v-f06ef9a0] {
  margin-top: 10px;
  border-radius: 5px;
  width: 108px;
  height: 40px;
  outline: none;
  font-size: 14px;
  font-family: PingFangSC-Regular
}

.modify-cancel-btn[data-v-f06ef9a0] {
  color: #ffc210;
  background: none;
  border: 1px solid #ffc210;
  margin-right: 20px
}

.modify-sure-btn[data-v-f06ef9a0] {
  color: #fff;
  border: none;
  background: #ffc210
}

.industry[data-v-f06ef9a0], .interested[data-v-f06ef9a0] {
  display: flex;
  align-items: center;
  flex-wrap: wrap
}

.industry li[data-v-f06ef9a0], .interested li[data-v-f06ef9a0] {
  list-style: none;
  width: 120px;
  height: 30px;
  border: 1px solid #e9e9e9;
  border-radius: 4px;
  font-size: 14px;
  color: #d0d0d0;
  text-align: center;
  line-height: 30px;
  margin-right: 10px;
  margin-bottom: 10px;
  cursor: pointer
}

.industry li[data-v-f06ef9a0]:last-child, .interested li[data-v-f06ef9a0]:last-child {
  margin-right: 0
}

.industry .pro-mark-active[data-v-f06ef9a0], .interested .pro-mark-active[data-v-f06ef9a0] {
  color: #ffc210;
  border: 1px solid #ffc210
}

.btn-wrap[data-v-f06ef9a0] {
  width: 300px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between
}

.btn-wrap .img-btn[data-v-f06ef9a0] {
  width: 93px;
  height: 31px;
  outline: none;
  border: none;
  border-radius: 2px;
  font-size: 14px
}

.btn-wrap .img-change[data-v-f06ef9a0] {
  background: #f4d8ab;
  color: #f5a623
}

.btn-wrap .img-cancel[data-v-f06ef9a0] {
  background: #d8d8d8;
  color: #fff
}

.btn-wrap .img-sure[data-v-f06ef9a0] {
  background: #7ed321;
  color: #fff
}

.security[data-v-f06ef9a0] {
  margin-left: 14px;
  margin-bottom: 50px
}

.security[data-v-f06ef9a0], .security div[data-v-f06ef9a0] {
  display: flex;
  align-items: center
}

.security div[data-v-f06ef9a0] {
  width: 30%;
  margin-right: 56px
}

.security div[data-v-f06ef9a0]:last-child {
  margin-right: 0
}

.shadow-wrap[data-v-f06ef9a0] {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 111
}

.shadow[data-v-f06ef9a0] {
  background: rgba(0, 0, 0, .2);
  display: flex;
  justify-content: center;
  align-items: center
}

.security-first-box[data-v-f06ef9a0], .security-next-box[data-v-f06ef9a0] {
  text-align: center;
  width: 410px;
  height: auto;
  background: #fff;
  box-shadow: 0 4px 10px 0 #9d9d9d;
  border-radius: 4px;
  position: relative;
  padding: 30px 30px 60px;
  z-index: 222
}

.security-first-box .security-next-content[data-v-f06ef9a0], .security-next-box .security-next-content[data-v-f06ef9a0] {
  margin-top: 40px
}

.security-first-box .next-btn[data-v-f06ef9a0], .security-first-box .set-success-btn[data-v-f06ef9a0], .security-next-box .next-btn[data-v-f06ef9a0], .security-next-box .set-success-btn[data-v-f06ef9a0] {
  margin-top: 10px;
  display: inline-block;
  width: 100%;
  height: 40px;
  background: #ffc210;
  color: #fff;
  line-height: 40px;
  cursor: pointer
}

.modal-tip[data-v-f06ef9a0], .security-first-box .next-btn[data-v-f06ef9a0], .security-next-box .next-btn[data-v-f06ef9a0] {
  margin-top: 30px
}

.modal-tip[data-v-f06ef9a0] {
  font-size: 13px;
  color: #9d9d9d;
  letter-spacing: 1.08px
}

.modal-tip span[data-v-f06ef9a0] {
  display: inline-block;
  margin-bottom: 6px
}

.modal-phone[data-v-f06ef9a0] {
  margin: 24px 0;
  font-size: 15px;
  color: #4a4a4a;
  letter-spacing: 1.25px
}

.edit-tit[data-v-f06ef9a0] {
  font-size: 24px;
  color: #5e5e5e;
  letter-spacing: 2px
}

.code-btn[data-v-f06ef9a0] {
  display: block;
  font-size: 16px;
  color: #ffc210;
  outline: none;
  border: none;
  background: none;
  margin-left: auto;
  margin-right: 10px;
  cursor: pointer;
  position: absolute;
  right: 0;
  top: 50%;
  margin-top: -12px
}

.error-tip[data-v-f06ef9a0] {
  height: 20px;
  color: #fd7b4d;
  margin-top: 5px;
  display: block;
  text-align: left
}

.inp[data-v-f06ef9a0] {
  width: 100%;
  height: 46px;
  position: relative
}

.inp .log-input[data-v-f06ef9a0] {
  width: 100%;
  height: 100%;
  text-indent: 10px;
  position: absolute;
  right: 0;
  border: 1px solid #e4e7ed;
  border-radius: 4px
}

.inp .log-input[data-v-f06ef9a0]:focus {
  border: 1px solid #ffc210
}

.inp .log-input.error[data-v-f06ef9a0] {
  border: 1px solid #fd7b4d
}

.change-professional[data-v-f06ef9a0] {
  margin-bottom: 30px
}

.side[data-v-20420f28] {
  width: 50px;
  height: auto;
  position: fixed;
  right: 10px;
  bottom: 50%;
  margin-bottom: -108px;
  z-index: 10
}

.side li[data-v-20420f28] {
  width: 100%;
  height: 50px;
  background: #ccc;
  border-radius: 2px;
  font-size: 12px;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 4px;
  cursor: pointer;
  font-family: PingFangSC-Regular;
  transition: all .2s ease-in-out;
  position: relative
}

.side li span[data-v-20420f28] {
  display: none
}

.side li img[data-v-20420f28] {
  width: 24px;
  height: auto;
  margin-bottom: 2px
}

.side li .code[data-v-20420f28] {
  width: 130px;
  height: auto;
  padding-top: 20px;
  padding-bottom: 5px;
  background: #fff;
  position: absolute;
  left: -140px;
  font-size: 12px;
  color: #5e5e5e;
  text-align: center;
  box-shadow: 0 2px 4px 0 #e8e8e8;
  border-radius: 4px;
  font-family: PingFangSC-Regular
}

.side li .code span[data-v-20420f28] {
  padding-bottom: 5px;
  display: block
}

.side li .code img[data-v-20420f28] {
  width: 110px;
  height: 110px;
  margin: 0 auto
}

.side li[data-v-20420f28]:hover {
  background: #ffc210
}

.side li:hover img[data-v-20420f28], .side li:hover p[data-v-20420f28] {
  display: none
}

.side li:hover span[data-v-20420f28] {
  display: inline-block
}

.side li[data-v-20420f28]:nth-of-type(2):hover {
  background: #ffc210
}

.side li:nth-of-type(2):hover .code[data-v-20420f28], .side li:nth-of-type(2):hover .wechat[data-v-20420f28] {
  display: block
}

.mbox[data-v-250c3340] {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background: rgba(0, 0, 0, .75);
  z-index: 1010;
  display: flex;
  align-items: center;
  justify-content: space-around
}

.mbox .mask[data-v-250c3340] {
  position: relative;
  text-align: center;
  cursor: pointer
}

.mbox .mask .close[data-v-250c3340] {
  width: 22px;
  height: 22px;
  position: absolute;
  right: -25px;
  top: 0;
  opacity: 1;
  cursor: pointer
}

.mbox .mask .popup[data-v-250c3340] {
  width: 593px;
  height: 270px
}

@-webkit-keyframes maskanimation-data-v-250c3340 {
  0% {
    transform: scale(.9);
    opacity: .3
  }
  50% {
    transform: scale(1.1);
    opacity: .7
  }
  to {
    transform: scale(1);
    opacity: 1
  }
}

@keyframes maskanimation-data-v-250c3340 {
  0% {
    transform: scale(.9);
    opacity: .3
  }
  50% {
    transform: scale(1.1);
    opacity: .7
  }
  to {
    transform: scale(1);
    opacity: 1
  }
}

.img1[data-v-dabcc042] {
  width: 18px;
  height: 18px
}

#course1[data-v-dabcc042] {
  margin-bottom: -2px
}

.foot-about[data-v-dabcc042] {
  background-color: #282828;
  width: 100%;
  height: 680px
}

.foot-about2[data-v-dabcc042] {
  display: flex;
  justify-content: center;
  margin-left: -500px
}

.box1[data-v-dabcc042], .box2[data-v-dabcc042] {
  float: left;
  width: 6%
}

.box3[data-v-dabcc042] {
  float: left;
  width: 10%
}

.box-title[data-v-dabcc042] {
  font-size: 12px;
  font-weight: 700;
  color: #d0d0d0;
  margin-top: 25px
}

.box-content1[data-v-dabcc042]:hover {
  color: #ffc210
}

.box-content1[data-v-dabcc042] {
  line-height: 30px
}

.box-content[data-v-dabcc042] {
  font-size: 10px;
  margin-left: 24px
}

.box-content a[data-v-dabcc042] {
  color: #d0d0d0
}

footer[data-v-dabcc042] {
  width: 100%;
  height: 380px;
  flex-direction: column;
  overflow: hidden;
  background: #191c25
}

footer[data-v-dabcc042], footer .foot-item[data-v-dabcc042] {
  display: flex;
  align-items: center
}

footer .foot-item[data-v-dabcc042] {
  width: 960px;
  height: 100%;
  justify-content: space-between
}

footer .foot-item .foot-left[data-v-dabcc042] {
  display: flex;
  align-items: center
}

footer .foot-item .foot-left .foot-content a[data-v-dabcc042] {
  color: #fff
}

footer .foot-item .foot-left .foot-content .copyright[data-v-dabcc042]:hover {
  color: #ffc210
}

footer .foot-item .foot-left .foot-content .copyright[data-v-dabcc042], footer .foot-item .foot-left .foot-content .report-link[data-v-dabcc042], footer .foot-item .foot-left .foot-content p[data-v-dabcc042]:first-child {
  color: #d0d0d0
}

footer .foot-item .foot-left .foot-content p:first-child span[data-v-dabcc042] {
  font-size: 16px;
  font-weight: 400;
  display: inline-block;
  font-family: PingFangSC-Regular;
  cursor: pointer
}

footer .foot-item .foot-left .foot-content p[data-v-dabcc042] {
  margin-bottom: 10px;
  font-size: 13px;
  font-family: PingFangSC-Regular;
  font-weight: 400;
  color: #d0d0d0
}

footer .foot-item .report-img[data-v-dabcc042] {
  display: inline-block;
  height: 20px;
  margin-right: 12px
}

footer .foot-item .code[data-v-dabcc042] {
  width: 74px;
  height: auto;
  margin-right: 100px
}</style>
