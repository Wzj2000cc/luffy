<template>
  <div class="cart">
    <Header></Header>
    <div class="cart_info">
      <div class="cart_title">
        <span class="text">我的购物车</span>
        <span class="total">共{{ $store.state.cart.cart_length }}门课程</span>
      </div>
      <div class="cart_table">
        <div class="cart_head_row">
          <span class="doing_row"></span>
          <span class="course_row">课程</span>
          <span class="expire_row">有效期</span>
          <span class="price_row">单价</span>
          <span class="do_more">操作</span>
        </div>
        <div class="cart_course_list">
          <CartItem v-for="(value,index) in cart_list" :key="value.id"
                    :cart="value" :check="checked" :status="status"
                    @change_expire_handler="calc_price" @del_course="del_course(index)" @select_ret="select_obj">
          </CartItem>
        </div>
        <div class="cart_footer_row">
          <span class="cart_select" @click="select_all"><label> <el-checkbox v-model="checked"></el-checkbox><span>全选</span></label></span>
          <span class="cart_delete"><i class="el-icon-delete"></i>
            <el-button type="danger" @click="delete_select" style="height: 30px;line-height: 5px">删除选中</el-button>
            <!--            <span @click="delete_select">全部删除</span>-->
          </span>
          <router-link :to="'/order/'" class="goto_pay">去结算</router-link>
          <span class="cart_total">总计：¥{{ total_price.toFixed(2) }}</span>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header"
import Footer from "./common/Footer"
import CartItem from "./common/CartItem"
import Add from "./common/Add";

export default {
  name: "Cart",
  data() {
    return {
      status: true,
      checked: true,
      cart_list: [],
      total_price: 0,
    }
  },
  methods: {
    // 用户登录验证
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

    // 获取购物车所需的数据
    get_cart_data() {
      let token = this.check_user_login();

      if (!token) {  // 如果token为false，AddCart函数不执行
        return false;
      }

      // get请求获取购物车数据
      this.$axios.get(`${this.$settings.Host}/cart/`, {
        headers: {
          'Authorization': 'jwt ' + token,
        }
      }).then(res => {
        this.cart_list = res.data.msg;
        this.calc_price()

        let cart_len = res.data.course_len;
        this.$store.commit('add_cart', cart_len)

        let that = this;
        this.checked = true;
        this.cart_list.some(function (val, i) {
          if (!val.is_selected) {
            that.checked = false;
            return true
          }
        });
      }).catch(error => {
        console.log(error.response);
      })
    },

    // 计算总价
    calc_price() {
      let total = 0
      this.cart_list.forEach(function (value, index) {
        if (value.is_selected) {
          total += parseFloat(value.real_price)
        }
      })
      this.total_price = total
    },

    select_all() {
      let token = this.check_user_login();
      if (!token) {
        return false
      }
      let status = 1;
      this.cart_list.forEach(function (value, index) {
        // console.log(value.is_selected);
        if (!value.is_selected) {
          status = 2;
          // console.log('全选')
          }
      });
      let that = this;
      this.$axios.patch(`${this.$settings.Host}/cart/`,
        {is_selected_all: status},
        {
          headers: {'Authorization': 'jwt ' + token}
        }).then(res => {
        this.status = false;
        this.cart_list.forEach(function (value, index) {
          value.is_selected = res.data.msg;
        });
        setTimeout(function () {
          that.status = true;
        }, 1000);
        this.calc_price();
      }).catch(error => {
      })
    },
    select_obj() {
      let that = this;

      this.checked = true;
      this.cart_list.some(function (val, i) {
        if (!val.is_selected) {
          that.checked = false;
          console.log(that.checked)
          return true
        }
      });
      console.log(this.checked,2)
    },

    // 删除前端单个的cart_list中的课程信息
    del_course(index) {
      this.cart_list.splice(index, 1)
      this.calc_price()
    },

    // 删除前端全部的cart_list里课程信息
    del_all(index) {
      let that = this;
      index.forEach(function (value, index) {
        that.cart_list.splice(value, 1);
      });
      this.calc_price();
      location.reload()
    },

    // 点击全部删除
    delete_select() {
      let token = this.check_user_login();
      if (!token) {
        return false
      }
      let del_list = [];
      let del_index = [];

      this.cart_list.forEach(function (value, index) {
        if (value.is_selected) {
          del_list.splice(-1, 0, value.id);
          del_index.splice(-1, 0, index);
        }
      });
      this.$confirm('亲！此操作将会删除全部选中课程, 确定继续吗? 嘤嘤嘤', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios.delete(`${this.$settings.Host}/cart/?course_list=${del_list}`,
          {
            headers: {
              'Authorization': 'jwt ' + token
            }
          }).then(res => {
          this.$message.success('勾选商品删除成功');
          this.del_all(del_index)
        }).catch(error => {
          this.$message.error(error.response.data.msg)
        })
      })
    },
  },

  created() {
    this.get_cart_data()
  },
  components: {
    Header,
    Footer,
    CartItem,
    Add
  }
}
</script>

<style scoped>
.cart_info {
  width: 1200px;
  margin: 0 auto 50px;
}

.cart_title {
  margin: 25px 0;
}

.cart_title .text {
  font-size: 18px;
  color: #666;
}

.cart_title .total {
  font-size: 12px;
  color: #d0d0d0;
}

.cart_table {
  width: 1170px;
}

.cart_table .cart_head_row {
  background: #F7F7F7;
  width: 100%;
  height: 80px;
  line-height: 80px;
  padding-right: 30px;
}

.cart_table .cart_head_row::after {
  content: "";
  display: block;
  clear: both;
}

.cart_table .cart_head_row .doing_row,
.cart_table .cart_head_row .course_row,
.cart_table .cart_head_row .expire_row,
.cart_table .cart_head_row .price_row,
.cart_table .cart_head_row .do_more {
  padding-left: 10px;
  height: 80px;
  float: left;
}

.cart_table .cart_head_row .doing_row {
  width: 78px;
}

.cart_table .cart_head_row .course_row {
  width: 530px;
}

.cart_table .cart_head_row .expire_row {
  width: 188px;
}

.cart_table .cart_head_row .price_row {
  width: 162px;
}

.cart_table .cart_head_row .do_more {
  width: 162px;
}

.cart_footer_row {
  padding-left: 36px;
  background: #F7F7F7;
  width: 100%;
  height: 80px;
  line-height: 80px;
}

.cart_footer_row .cart_select span {
  margin-left: 14px;
  font-size: 18px;
  color: #666;
}

.cart_footer_row .cart_delete {
  margin-left: 58px;
}

.cart_delete .el-icon-delete {
  font-size: 18px;
}

.cart_delete span {
  margin-left: 15px;
  cursor: pointer;
  font-size: 18px;
  color: #666;
}

.cart_total {
  float: right;
  margin-right: 62px;
  font-size: 18px;
  color: #666;
}

.goto_pay {
  float: right;
  width: 159px;
  height: 80px;
  outline: none;
  border: none;
  background: #ffc210;
  font-size: 18px;
  color: #fff;
  text-align: center;
  cursor: pointer;
}
</style>

