<template>
  <div class="cart_item">
    <div class="cart_column column_1">
      <el-checkbox class="my_el_checkbox" v-model="cart.is_selected"></el-checkbox>
    </div>
    <div class="cart_column column_2">
      <img :src="cart.course_img" alt="">
      <span><router-link :to="'/course/detail/' + cart.id + '/'">{{cart.name}}</router-link></span>
    </div>
    <div class="cart_column column_3">
      <el-select v-model="cart.expire_id" size="mini" placeholder="请选择购买有效期" class="my_el_select">
        <el-option v-for="(value,index) in cart.expire_list" :label="value.expire_text" :value="value.id"
                   :key="value.id"></el-option>
      </el-select>
    </div>
    <div class="cart_column column_4">¥{{cart.real_price}}</div>
<!--    <div class="cart_column column_4" @click="delete_course">删除</div>-->
    <el-button type="danger" class="cart_row" @click="delete_course">删除</el-button>
  </div>
</template>

<script>
export default {
  name: "CartItem",
  data() {
    return {
      checked: false,
      expire: "1个月有效",
      ret:true,
    }
  },
  props: ['cart','status'],
  watch:{
    'status': function () {
      this.ret = this.status
    },
    'cart.is_selected': function () {
      if (this.ret) {
        this.change_course_selected()
      }
    },
    "cart.expire_id":function (){
      this.change_expire()
    },


  },
  methods:{
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

    // 实时监听课程勾选状态，发送patch请求修改redis数据库
    change_course_selected(){
      let token = this.check_user_login();

      // 将课程id发送到后端
      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }

      // 请求获取购物车数据
      this.$axios.patch(`${this.$settings.Host}/cart/`,{
        is_selected:this.cart.is_selected,
        course_id:this.cart.id,
        },
        {headers: {
          'Authorization': 'jwt ' + token,}
      }).then(res=>{
        this.$message.success(res.data.msg)
        this.$emit('change_expire_handler')
        this.$emit('select_ret');

      }).catch(error=>{
        this.$message.error(error.response.msg);
        this.cart.is_selected = !this.cart.is_selected
      })
    },

    // 实时监听课程有效期更改状态，发送put请求修改redis数据库
    change_expire(){
      let token = this.check_user_login()

      // 将课程id发送到后端
      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }

      this.$axios.put(`${this.$settings.Host}/cart/`,{
        expire_id:this.cart.expire_id,
        course_id:this.cart.id
      },{
        headers:{
          'Authorization': 'jwt ' + token
        }
      }).then(res=>{
        this.$message.success(res.data.msg)
        this.cart.real_price = res.data.real_price
        this.$emit('change_expire_handler')
      }).catch(error=>{
        this.$message.error(error.response.msg)
      })
    },

    // delete请求删除商品信息
    delete_course(){
      let token = this.check_user_login();

      // 将课程id发送到后端
      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }
      // 点击删除 弹框
      this.$confirm('亲！此操作将删除该课程, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        // 请求删除
        this.$axios.delete(`${this.$settings.Host}/cart/?course_id=${this.cart.id}`,{
          headers: {
            'Authorization': 'jwt ' + token,
          }
        }).then(res =>{
          this.$message.success('删除商品成功')
          this.$emit('del_course')
        }).catch(error =>{
          this.$message.error(error.response.data.msg)
        })
      }).catch(() => {
        this.$message({
          type: 'error',
          message: '已取消删除',
        });
      });
    }
  },
}
</script>

<style scoped>
/*.cart_item{*/
/*  height: 100px;*/
/*}*/
.cart_item::after {
  content: "";
  display: block;
  clear: both;
}

.cart_column {
  float: left;
  height: 150px;
  display: flex;
  align-items: center;
}

.cart_item .column_1 {
  width: 88px;
  position: relative;
}

.my_el_checkbox {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  margin: auto;
  width: 16px;
  height: 16px;
}

.cart_item .column_2 {
  /*padding: 67px 10px;*/
  width: 520px;
  /*height: 116px;*/
}

.cart_item .column_2 img {
  width: 175px;
  /*height: 115px;*/
  margin-right: 35px;
  /*vertical-align: middle;*/
}

.cart_item .column_3 {
  width: 197px;
  position: relative;
  padding-left: 10px;
}

.my_el_select {
  width: 117px;
  height: 28px;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
}

.cart_item .column_4 {
  padding: 0 17.5px;
  /*height: 116px;*/
  width: 142px;
  /*line-height: 116px;*/
}
.cart_row{
  margin-top: 58px;
}
</style>
