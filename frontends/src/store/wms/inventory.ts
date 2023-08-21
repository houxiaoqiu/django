import { defineStore } from "pinia";
import { getInventories, IInventory } from '@/api/wms/inventory'

export const useInventoriesStore = defineStore('inventories', {
  state: () => {
    return {
      all: [] as IInventory[],      //所有商品列表
    };
  },

  getters: {},

  actions: {
    async loadAllInventories () {
        const res = await getInventories()
        this.all = res
    },

    reduceInventory (inventory: IInventory) {
        const res = this.all.find(item => item.id == inventory.id )
        if (res) {
            res.inventory--
        }
    }
  },
});
