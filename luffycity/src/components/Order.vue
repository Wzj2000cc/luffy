<template>
  <div class="cart">
    <Header></Header>
    <div class="cart-info">
      <h3 class="cart-top">购物车结算 <span>共{{course_list.length}}门课程</span></h3>
      <div class="cart-title">
        <el-row>
          <el-col :span="2">&nbsp;</el-col>
          <el-col :span="5">课程</el-col>
          <el-col :span="5">名称</el-col>
          <el-col :span="8">有效期</el-col>
          <el-col :span="4">价格</el-col>
        </el-row>
      </div>
      <div class="cart-item" v-for="(value,index) in course_list" :key="value.id">
        <el-row>
          <el-col :span="2" class="checkbox">&nbsp;&nbsp;</el-col>
          <el-col :span="10" class="course-info">
            <img :src="value.course_img" alt="">
            <span>{{value.name}}</span>
          </el-col>
          <el-col :span="8"><span>{{value.expire_text}}</span></el-col>
          <el-col :span="4" class="course-price">¥{{value.real_price}}</el-col>
        </el-row>
      </div>

      <div class="discount">
        <div id="accordion">
          <div class="coupon-box">
            <div class="icon-box">
              <span class="select-coupon">使用优惠劵：</span>
              <a class="select-icon unselect" :class="use_coupon?'is_selected':''" @click="use_coupon=!use_coupon"><img class="sign is_show_select" src="../../static/image/12.png" alt=""></a>
              <span class="coupon-num">有{{coupon_list.length}}张可用</span>
            </div>
            <p class="sum-price-wrap">商品总金额：<span class="sum-price">{{real_total_price}}元</span></p>
          </div>
          <div id="collapseOne" v-if="use_coupon">
            <ul class="coupon-list"  v-if="coupon_list.length > 0">
              <li class="coupon-item" v-for="(item,index) in coupon_list" :key="item.id"
                  :class="selected_coupon(index)"  @click="click_selected_coupon(index,item.id)">
                <p class="coupon-name">{{item.coupon.name}}</p>
                <p class="coupon-condition">满{{item.coupon.condition}}元可以使用</p>
                <p class="coupon-time start_time">开始时间：{{item.start_time.replace('T', " ")}}</p>
                <p class="coupon-time end_time">过期时间：{{item.end_time.replace('T', " ")}}</p>
              </li>
            </ul>
            <div class="no-coupon" v-if="coupon_list.length < 1">
              <span class="no-coupon-tips">暂无可用优惠券</span>
            </div>
          </div>
        </div>
        <div class="credit-box">
          <label class="my_el_check_box"><el-checkbox class="my_el_checkbox" v-model="use_credit"></el-checkbox></label>
          <p class="discount-num1" v-if="!use_credit">使用我的贝里</p>
          <p class="discount-num2" v-else><span>总积分：{{user_credit}}，
            抵扣 <el-input-number @change="handleChange"  v-model="credit" :min="0" :max="max_credit()" label="请填写积分"></el-input-number>，
            本次花费以后，剩余{{parseInt(user_credit-credit)}}积分</span></p>
        </div>
        <p class="sun-coupon-num">优惠券与积分共抵扣：<span>{{(real_total_price - real_total_price_show + credit / credit_to_money).toFixed(2)}}元</span></p>
      </div>

      <div class="calc">
        <el-row class="pay-row">
          <el-col :span="4" class="pay-col"><span class="pay-text">支付方式：</span></el-col>
          <el-col :span="8">
            <span class="alipay" v-if="pay_type===0"><img src="../../static/image/alipay2.jpg" alt=""></span>
            <span class="alipay" v-else @click="pay_type=0"><img src="../../static/image/alipay.jpg" alt=""></span>
            <span class="alipay wechat" v-if="pay_type===1"><img src="../../static/image/wechat2.jpg" alt=""></span>
            <span class="alipay wechat" v-else @click="pay_type=1"><img src="../../static/image/wechat.jpg" alt=""></span>
          </el-col>
          <el-col :span="8" class="count">实付款： <span>¥{{ (real_total_price_show - credit / credit_to_money).toFixed(2)}}</span></el-col>
          <el-col :span="4" class="cart-pay" v-if="pay_type===0"><span @click="pay(pay_type)">支付宝支付</span></el-col>
          <el-col :span="4" class="cart-pay" v-else><span @click="pay(pay_type)">微信支付</span></el-col>
        </el-row>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header"
import Footer from "./common/Footer"

export default {
  name: "Order",
  data() {
    return {
      course_list: [],
      real_total_price: 0, // 真实价格
      real_total_price_show: 0,  // 设置一个变量，优惠券后的价格
      origin_total_price: 0,  // 商品未参加所有优惠的价格
      pay_type: 0, // 设置支付方式的切换状态
      credit:0,  // 积分
      coupon:0,  // 优惠券对象id
      use_credit: false,  // 是否使用了积分
      use_coupon: false,  // 是否使用优惠券
      coupon_list:[1],   // 优惠券对象列表
      user_credit: localStorage.user_credit || sessionStorage.user_credit,  // 获取当前用户积分
      credit_to_money: localStorage.credit_to_money || sessionStorage.credit_to_money,  // 获取积分折合金额计算方式
    }
  },
  components: {
    Header,
    Footer,
  },
  created() {
    // 刷新页面时执行此方法，获取用户是否登录的token值
    this.token = this.check_user_login();
    this.get_course_list();
    this.get_coupon();
  },
  methods: {
    // 登录认证
    check_user_login() {
      let token = localStorage.user_token || sessionStorage.user_token;
      if (!token) {
        let self = this;
        this.$confirm('对不起，您尚未登录！请先登录在添加购物车', '路飞学城', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(() => {
          self.$router.push('/login/');
        });
        return false
      }
      return token;
    },
    // 订单页面获取购物车选中的所有课程数据
    get_course_list() {
      let token = this.check_user_login();
      // 将课程id发送到后端
      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }
      this.$axios.get(`${this.$settings.Host}/cart/order/`, {
        headers: {'Authorization': 'jwt ' + token,}
      }).then(res => {
          this.course_list = res.data.course_list;
          this.real_total_price = res.data.real_total_price;
          this.real_total_price_show = this.real_total_price;
          this.origin_total_price = res.data.origin_total_price;
        }).catch(error =>{
          this.$message.error(error.response.data);
        })
    },

    // 获取当前用户优惠券信息
    get_coupon(){
      if (!this.token){
        this.$router.push('/login/')
        return false
      }
      // get请求获取当前用户的优惠券
      this.$axios.get(`${this.$settings.Host}/coupon/`, {
        headers: {"Authorization": "jwt " + this.token,}
      }).then(response => {
        this.coupon_list = response.data
      }).catch(error => {
        this.$message.error("对不起，当前购物车没有任何商品被勾选！");
      })
    },

    // 优惠券的选中状态显示
    selected_coupon(index) {
      let user_coupon = this.coupon_list[index];  // 当前的优惠券对象
      // 判断总价格是否满足优惠卷的使用
      if (this.real_total_price < user_coupon.coupon.condition) {
        return 'disable'
      }

      // 判断优惠券是否处于使用的时间范围内
      let start_timestamp = parseInt(new Date(user_coupon.start_time) / 1000);
      let end_timestamp = parseInt(new Date(user_coupon.end_time) / 1000);
      let now_timestamp = parseInt(new Date() / 1000);
      if (now_timestamp < start_timestamp || now_timestamp > end_timestamp) {
        return 'disable';
      }

      // 由于这个方法要循环执行3次（循环执行的次数根据优惠券的个数决定），我们只能让选中的满足条件的优惠券加上背景颜色。
      if (this.coupon === user_coupon.id) {
        return 'active';
      }
      return '';
    },

    // 不可选中的优惠券不能点击（点击时不传该优惠券id）
    click_selected_coupon(index,user_coupon_id){
      let user_coupon = this.coupon_list[index];  // 当前的优惠券对象
      // 判断总价格是否满足优惠卷的使用
      if (this.real_total_price < user_coupon.coupon.condition) {
        return false;
      }

      // 判断优惠券是否处于使用的时间范围内
      let start_timestamp = parseInt(new Date(user_coupon.start_time) / 1000);
      let end_timestamp = parseInt(new Date(user_coupon.end_time) / 1000);
      let now_timestamp = parseInt(new Date() / 1000);
      if (now_timestamp < start_timestamp || now_timestamp > end_timestamp) {
        return false;
      }
      this.coupon = user_coupon_id
      this.calc_real_price(index)
    },

    // 计算使用全场优惠券之后的价格
    calc_real_price(index) {
      let ret = this.coupon_list[index];
      let calc_func = ret.coupon.sale;
      let d = parseFloat(calc_func.substr(1,));
      if (calc_func[0] === '*') {
        this.real_total_price_show = this.real_total_price * d;
      } else {
        this.real_total_price_show = this.real_total_price - d;
      }
      // 解决先使用积分扣光总金额在使用优惠券总金额会显示负数的bug
      if (this.real_total_price_show * this.credit_to_money < this.credit ) {
        this.credit = this.max_credit()
      }
    },

    // 积分折合金额最大不能超过此订单金额
    max_credit(){
      let max_credit_to_money = this.user_credit / this.credit_to_money
      let ret = 0
      if(max_credit_to_money > this.real_total_price_show){
        ret = parseInt(this.real_total_price_show * this.credit_to_money)
      }else {
        ret = parseInt(this.user_credit);
      }
      return ret
    },

    // 积分输入框变化就触发
    handleChange(value){
      // console.log(value)  value是当前用户选择使用积分数量
      if(!value){
        this.credit = 0
      }
    },

    // 点击 微信/支付宝 支付弹出收款码
    pay(type){
      let token = this.check_user_login();

      // 将课程id发送到后端
      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }
      // 支付宝支付
      if (type === 0){
          // 弹框点击确定发送订单生成请求
          this.$axios.post(`${this.$settings.Host}/order/`, {
            pay_type:this.pay_type,
            credit:this.credit,
            coupon:this.coupon,
          },{
            headers: {
              'Authorization': 'jwt ' + token,
            }}).then(res =>{
            this.$message.success('订单生成成功，即将跳转页面')
            this.$axios.get(`${this.$settings.Host}/payments/alipay`,{
              params:{
                order_number:res.data.order_number
              }
            }).then(response => {
              // 支付成功跳转到指定的页面
              location.href = response.data
            }).catch(error => {
              console.log(error.response)
            })
            // window.history.go(-1) // 跳转到上一级页面
          }).catch(error =>{
            this.$message.error('订单生成失败')
          })
        }
      // 微信支付
      else {
        this.$confirm(
          '<strong> <img src="../../static/image/pay1.jpg" alt="" style="width: 350px;height: 480px">'+
          '<p></p></strong>',
          '请尽快完成支付哦亲！',  //弹窗标题
          {
            dangerouslyUseHTMLString: true,//true的时候message会被作为HTML片段处理
            center:true, // 设置弹出框居中对齐
            showCancelButton: true, //显示取消按钮
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            beforeClose: (action, instance, done) => {
              if (action === 'confirm') { //点击确认
                this.$axios.post(`${this.$settings.Host}/order/`, {
                  pay_type:this.pay_type,
                  credit:this.credit,
                  coupon:this.coupon,
                },{
                  headers: {
                    'Authorization': 'jwt ' + token,
                  }}).then(res =>{
                  this.$message.success('订单生成成功，即将跳转页面')
                  window.history.go(-1)
                }).catch(error =>{
                  this.$message.error('订单生成失败')
                })
              }else{   //点击取消
                done();
              }
            }
          });
      }
    },
  }
}
</script>

<style scoped>
.cart {
  margin-top: 80px;
}

.cart-info {
  overflow: hidden;
  width: 1200px;
  margin: auto;
}

.cart-top {
  font-size: 18px;
  color: #666;
  margin: 25px 0;
  font-weight: normal;
}

.cart-top span {
  font-size: 12px;
  color: #d0d0d0;
  display: inline-block;
}

.cart-title {
  background: #F7F7F7;
  height: 70px;
}

.calc {
  margin-top: 25px;
  margin-bottom: 40px;
}

.calc .count {
  text-align: right;
  margin-right: 10px;
  vertical-align: middle;
}

.calc .count span {
  font-size: 36px;
  color: #333;
}

.calc .cart-pay {
  margin-top: 5px;
  width: 110px;
  height: 38px;
  outline: none;
  border: none;
  color: #fff;
  line-height: 38px;
  background: #ffc210;
  border-radius: 4px;
  font-size: 16px;
  text-align: center;
  cursor: pointer;
}

.cart-item {
  height: 120px;
  line-height: 120px;
  margin-bottom: 30px;
}

.course-info img {
  width: 175px;
  height: 115px;
  margin-right: 35px;
  vertical-align: middle;
}

.alipay {
  display: inline-block;
  height: 48px;
}

.alipay img {
  height: 100%;
  width: auto;
}

.pay-text {
  display: block;
  text-align: right;
  height: 100%;
  line-height: 100%;
  vertical-align: middle;
  margin-top: 20px;
}

.coupon-box{
  text-align: left;
  padding-bottom: 22px;
  padding-left:30px;
  border-bottom: 1px solid #e8e8e8;
}
.coupon-box::after{
  content: "";
  display: block;
  clear: both;
}
.icon-box{
  float: left;
}
.icon-box .select-coupon{
  float: left;
  color: #666;
  font-size: 16px;
}
.icon-box::after{
  content:"";
  clear:both;
  display: block;
}
.select-icon{
  width: 20px;
  height: 20px;
  float: left;
}
.select-icon img{
  max-height:100%;
  max-width: 100%;
  margin-top: 2px;
  transform: rotate(-90deg);
  transition: transform .5s;
}
.is_show_select{
  transform: rotate(0deg)!important;
}
.coupon-num{
  height: 22px;
  line-height: 22px;
  padding: 0 5px;
  text-align: center;
  font-size: 12px;
  float: left;
  color: #fff;
  letter-spacing: .27px;
  background: #fa6240;
  border-radius: 2px;
  margin-left: 20px;
}
.sum-price-wrap{
  float: right;
  font-size: 16px;
  color: #4a4a4a;
  margin-right: 45px;
}
.sum-price-wrap .sum-price{
  font-size: 18px;
  color: #fa6240;
}

.no-coupon{
  text-align: center;
  width: 100%;
  padding: 50px 0px;
  align-items: center;
  justify-content: center; /* 文本两端对其 */
  border-bottom: 1px solid rgb(232, 232, 232);
}
.no-coupon-tips{
  font-size: 16px;
  color: #9b9b9b;
}
.credit-box{
  height: 30px;
  margin-top: 40px;
  display: flex;
  align-items: center;
  justify-content: flex-end
}
.my_el_check_box{
  position: relative;
}
.my_el_checkbox{
  margin-right: 10px;
  width: 16px;
  height: 16px;
}
.discount{
  overflow: hidden;
}
.discount-num1{
  color: #9b9b9b;
  font-size: 16px;
  margin-right: 45px;
}
.discount-num2{
  margin-right: 45px;
  font-size: 16px;
  color: #4a4a4a;
}
.sun-coupon-num{
  margin-right: 45px;
  margin-bottom:43px;
  margin-top: 40px;
  font-size: 16px;
  color: #4a4a4a;
  display: inline-block;
  float: right;
}
.sun-coupon-num span{
  font-size: 18px;
  color: #fa6240;
}
.coupon-list{
  margin: 20px 0;
}
.coupon-list::after{
  display: block;
  content:"";
  clear: both;
}
.coupon-item{
  float: left;
  margin: 15px 8px;
  width: 180px;
  height: 100px;
  padding: 5px;
  background-color: #fa3030;
  cursor: pointer;
}
.coupon-list .active{
  background-color: #fa9000;
}
.coupon-list .disable{
  cursor: not-allowed;
  background-color: #fa6060;
}
.coupon-condition{
  font-size: 12px;
  text-align: center;
  color: #fff;
}
.coupon-name{
  color: #fff;
  font-size: 24px;
  text-align: center;
}
.coupon-time{
  text-align: left;
  color: #fff;
  font-size: 12px;
}
.unselect{
  margin-left: 0;
  transform: rotate(-90deg);
}
.is_selected{
  transform: rotate(-1turn)!important;
}
.coupon-item p{
  margin: 0;
  padding: 0;
}
</style>
