<template>
  <div class="login box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="login">
      <div class="login-title">
        <img src="../../static/image/Logotitle.1ba5466.png" alt="">
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span @click="login_type=0">密码登录</span>
          <span @click="login_type=1">短信登录</span>
        </div>
        <div class="inp" v-if="login_type==0">
          <input v-model = "username" type="text" placeholder="用户名 / 手机号码" class="user">
          <input v-model = "password" type="password" name="" class="pwd" placeholder="密码">
          <div id="geetest1"></div>
          <div class="rember">
            <p>
              <input type="checkbox" class="no" name="a" v-model="remember"/>
              <span>记住密码</span>
            </p>
            <router-link to="/respwd">忘记密码</router-link>
          </div>
<!--          <button class="login_btn" @click="LoginHandler">登录</button>-->
          <el-button :plain="true" @click="GetCapycha" class="login_btn">登录</el-button>
          <p class="go_login" >没有账号
            <router-link to="/register">
              <span class="go_login">立即注册</span>
            </router-link>
          </p>
        </div>
        <div class="inp" v-show="login_type==1">
          <input v-model = "username" type="text" placeholder="手机号码" class="user">
          <input v-model = "password"  type="text" class="pwd" placeholder="短信验证码">
          <button id="get_code">获取验证码</button>
          <button class="login_btn">登录</button>

            <p class="go_login" >没有账号
              <router-link to="/register">
                <span class="go_login">立即注册</span>
              </router-link>
            </p>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data(){
    return {
      login_type: 0,
      username:"",
      password:"",
      remember:false, // 判断是否勾选记住密码
    }
  },

  methods:{
    LoginHandler(){
      this.$axios.post(`${this.$settings.Host}/users/login/`,{
        username:this.username,
        password:this.password,
      }).then(res=>{
        // console.log(res.data);
        let data = res.data
        if (this.remember){ // 永久保存
          sessionStorage.clear(); // 永久保存前先清空临时保存的数据
          localStorage.user_token = data.token;
          localStorage.user_id = data.id;
          localStorage.user_name = data.name;
          localStorage.user_credit = data.user_credit;
          localStorage.credit_to_money = data.credit_to_money;
        }else { // 临时保存
          localStorage.clear(); // 临时保存前先清空永久保存的数据
          sessionStorage.user_token = data.token;
          sessionStorage.user_id = data.id;
          sessionStorage.user_name = data.name;
          sessionStorage.user_credit = data.user_credit;
          sessionStorage.credit_to_money = data.credit_to_money;
        }
        this.$router.push('/'); // vue跳转页面功能
        this.$message({
          message: '恭喜你，登录成功！',
          type: 'success'
        });
      }).catch(error=>{
        console.log(error);
        this.$message.error('错了哦，请重新输入');
      })
    },

    handlerPopup(captchaObj){

      document.getElementById('geetest1').innerHTML='';
      captchaObj.appendTo('#geetest1');

      captchaObj.onSuccess(()=>{ // 实时监听滑动验证码
        var validate = captchaObj.getValidate();
        console.log(validate)
        this.$axios.post(`${this.$settings.Host}/users/capycha/`,{
          geetest_challenge: validate.geetest_challenge,
          geetest_validate: validate.geetest_validate,
          geetest_seccode: validate.geetest_seccode,
        }).then(data =>{
          console.log(data)
          if(data.data.status === 'success'){
            this.LoginHandler();
          }
        })
      });
    },

    GetCapycha(){ // 点击登录，发送第一个get请求，获取我们的验证码标签
      this.$axios.get(`${this.$settings.Host}/users/capycha/`).then(data =>{
        initGeetest({
          gt: data.data.gt,
          challenge: data.data.challenge,
          product: "popup", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
          offline: !data.data.success // 表示用户后台检测极验服务器是否宕机，一般不需要关注
        }, this.handlerPopup);
      }).catch(error =>{
        console.log(error)
      });
    },
  },
};
</script>

<style scoped>
.box{
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}
.box img{
  width: 100%;
  min-height: 100%;
}
.box .login {
  position: absolute;
  width: 500px;
  height: 400px;
  top: 0;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}
.login .login-title{
  width: 100%;
  text-align: center;
}
.login-title img{
  width: 190px;
  height: auto;
}
.login-title p{
  font-family: PingFangSC-Regular;
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}
.login_box{
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}
.login_box .title{
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 50px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}
.login_box .title span:nth-of-type(1){
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp{
  width: 350px;
  margin: 0 auto;
}
.inp input{
  border: 0;
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}
.inp input.user{
  margin-bottom: 16px;
}
.inp .rember{
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}
.inp .rember p:first-of-type{
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}
.inp .rember p:nth-of-type(2){
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input{
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp .rember p span{
  display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
  /*left: 20px;*/

}
#geetest{
  margin-top: 20px;
}
.login_btn{
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
}
.inp .go_login{
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}
.inp .go_login span{
  color: #84cc39;
  cursor: pointer;
}
</style>
