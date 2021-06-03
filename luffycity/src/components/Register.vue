<template>
  <div class="box">
    <img src="../../static/image/Loginbg.3377d0c.jpg" alt="">
    <div class="register">
      <div class="register_box">
        <div class="register-title">注册路飞学城</div>
        <div class="inp">
          <input v-model = "mobile" type="text" placeholder="请输入账号或手机号码" class="user" @blur="checkmobile">
          <input v-model = "password" type="password" placeholder="请输入密码" class="user">
          <div class="sms-box">
            <input v-model = "sms_code" type="text" maxlength='8' placeholder="输入验证码" class="user">
            <div class="sms-btn" @click="smsHandler">点击发送短信</div>
            <div v-show="!show" class="sms-btn1">{{count}} s</div>
          </div>

          <!-- <div id="geetest"></div>滑动验证这里我就不加了 -->
          <button class="register_btn" @click="RegisterHandler" >注册</button>
          <p class="go_login" >已有账号 <router-link to="/login">直接登录</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data(){
    return {
      sms_code:"",
      mobile:"",
      password:"",
      validateResult:false,
      errors_data:{'mobile': '手机号码', 'password': '密码', 'sms_code': '验证码'},
      show: true,
      count: '',
      timer: null,
    }
  },

  methods:{
    RegisterHandler(){
      this.$axios.post(`${this.$settings.Host}/users/register/`, {
        mobile:this.mobile,
        password:this.password,
        sms_code:this.sms_code,
      }).then(res=>{
        console.log(res)
        localStorage.removeItem('user_token');
        localStorage.removeItem('id');
        localStorage.removeItem('username');

        // sessionStorage有就覆盖掉
        sessionStorage.user_token= res.data.token;
        sessionStorage.id= res.data.id;
        sessionStorage.username= res.data.username;

        this.$alert('注册成功，点击确定直接登录',{
          confirmButtonText:'确定',
          callback:action => {
            this.$router.push('/')
          }
        })
        }).catch(async error=>{
          let data = error.response.data;
          let message = '';
          for(let key in data){
            message = await this.errors_data[key]+":"+data[key][0];
            // message = this.errors_data[key]+'字段不能为空';
            // this.$message({offset:num*40,message:message,type:"error"});
            this.$message.error(message)
          }
          // this.$message.error("手机号码或密码或验证码不能为空")
      })
    },
    checkmobile(){

      // if(! /^1[3-9]\d{9}$/.test(this.mobile)){
      //   this.$message.error('手机号码格式不正确')
      // }
      this.$axios.get(`${this.$settings.Host}/users/mobile/${this.mobile}/`).then(
      res=>{
        this.$message.success(res.data.msg)
      }).catch(error=>{
        this.$message.error(error.response.data.msg)
      })
    },
    smsHandler(){
      this.$axios.get(`${this.$settings.Host}/users/sms/${this.mobile}/`).then(res =>{
        this.$message.success(res.data.msg)
        const TIME_COUNT = 60;
        if (!this.timer) {
          this.count = TIME_COUNT;
          this.show = false;
          this.timer = setInterval(() => {
            if (this.count > 0 && this.count <= TIME_COUNT) {
              this.count--;
            } else {
              this.show = true;
              clearInterval(this.timer);
              this.timer = null;
            }
          }, 1000)
        }
      }).catch(error =>{
        this.$message.error(error.response.data.msg)
      })
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
.box .register {
  position: absolute;
  width: 500px;
  height: 400px;
  top: 0;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -120px;
}
.register .register-title{
  width: 100%;
  font-size: 24px;
  text-align: center;
  padding-top: 30px;
  padding-bottom: 30px;
  color: #4a4a4a;
  letter-spacing: .39px;
}
.register-title img{
  width: 190px;
  height: auto;
}
.register-title p{
  font-family: PingFangSC-Regular;
  font-size: 18px;
  color: #fff;
  letter-spacing: .29px;
  padding-top: 10px;
  padding-bottom: 50px;
}
.register_box{
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}
.register_box .title{
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
.register_box .title span:nth-of-type(1){
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
.register_btn{
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

.sms-box{
  position: relative;
}
.sms-btn{
  font-size: 14px;
  color: #ffc210;
  letter-spacing: .26px;
  position: absolute;
  right: 16px;
  top: 10px;
  cursor: pointer;
  overflow: hidden;
  background: #fff;
  border-left: 1px solid #484848;
  padding-left: 16px;
  padding-bottom: 4px;
}

.sms-btn1{
  font-size: 14px;
  color: #ffc210;
  letter-spacing: .26px;
  position: absolute;
  right: 16px;
  top: 10px;
  cursor: pointer;
  overflow: hidden;
  background: #fff;
  border-left: 1px solid #484848;
  padding-left: 75px;
  padding-bottom: 4px;
}
</style>

