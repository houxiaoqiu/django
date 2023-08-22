import { defineStore } from "pinia";
import { getProducts, IProduct } from '@/api/shopping'

export const useProductsStore = defineStore('products', {
  state: () => {
    return {
      all: [] as IProduct[],      //所有商品列表
    };
  },

  getters: {},

  actions: {
    async loadAllProducts () {
        const res = await getProducts()
        this.all = res
    },

    reduceProduct (product: IProduct) {
        const res = this.all.find(item => item.id == product.id )
        if (res) {
            res.inventory
        }
    }
  },
});
