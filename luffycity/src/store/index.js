import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // 数据仓库，类似于vue中的data
  state:{
    cart:{
      cart_length:0,
    }
  },
  // 操作数据的具体方法 类似于vue的methods
  mutations:{
    add_cart(state,cart_len){
      state.cart.cart_length = cart_len;
    }
  },
})





