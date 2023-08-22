import { IInventory, buyInventories } from "@/api/wms/inventory";
import { defineStore } from "pinia";
import { useInventoriesStore } from "@/store/wms/inventory";

// 定义容器属性：增加 quantity，删除 inventory
type WarehouseInventory = {
  quantity: number;
} & Omit<IInventory, "inventory">;

export const useWarehouseStore = defineStore("warehouse", {
  state: () => {
    return {
      warehouseInventories: [] as WarehouseInventory[],
      checkoutStatus: null as null | string,
    };
  },

  getters: {
    totalPrice(state) {
      return state.warehouseInventories.reduce((total, item) => {
        return total + item.price * item.quantity;
      }, 0);
    },
  },

  actions: {
    addInventoryToWarehouse(inventory: IInventory) {
      console.log("addInventoryToWarehouse", inventory);
      // 是否有库存
      if (inventory.inventory < 1) {
        return;
      }
      // 购物车是否有该商品
      const warehouseItem = this.warehouseInventory.find(
        (item) => item.id == inventory.id
      );
      if (warehouseItem) {
        // 购物车有该商品，增加该商品数量
        warehouseItem.quantity++;
      } else {
        // 购物车没有该商品，添加该商品到购物车
        this.warehouseInventories.push({
          id: inventory.id,
          title: inventory.title,
          price: inventory.price,
          quantity: 1,
        });
      }
      // 更新商品库存
      const inventoriesStore = useInventoriesStore();
      inventoriesStore.reduceInventory(inventory);
    },

    async checkout() {
      const res = await buyInventories();
      this.checkoutStatus = res ? "成功" : "失败";
      // 清空购物车
      if (res) {
        this.warehouseInventories = [];
      }
    },
  },
});
