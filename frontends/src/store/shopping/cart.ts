import { IProduct, buyProducts } from "@/api/shopping/shopping";
import { defineStore } from "pinia";
import { useProductsStore } from "@/store/shopping/shopping";

// 定义容器属性：增加 quantity，删除 inventory
type CartProduct = {
  quantity: number;
} & Omit<IProduct, "inventory">;

export const useCartStore = defineStore("cart", {
  state: () => {
    return {
      cartProducts: [] as CartProduct[],
      checkoutStatus: null as null | string,
    };
  },

  getters: {
    totalPrice(state) {
      return state.cartProducts.reduce((total, item) => {
        return total + item.price * item.quantity;
      }, 0);
    },
  },

  actions: {
    addProductToCart(product: IProduct) {
      // console.log('addProductToCart', product)
      // 是否有库存
      if (product.inventory < 1) {
        return;
      }
      // 购物车是否有该商品
      const cartItem = this.cartProducts.find((item) => item.id == product.id);
      if (cartItem) {
        // 购物车有该商品，增加该商品数量
        cartItem.quantity++;
      } else {
        // 购物车没有该商品，添加该商品到购物车
        this.cartProducts.push({
          id: product.id,
          title: product.title,
          price: product.price,
          quantity: 1,
        });
      }
      // 更新商品库存
      const productsStore = useProductsStore();
      productsStore.reduceProduct(product);
    },

    async checkout() {
      const res = await buyProducts();
      this.checkoutStatus = res ? "成功" : "失败";
      // 清空购物车
      if (res) {
        this.cartProducts = [];
      }
    },
  },
});
