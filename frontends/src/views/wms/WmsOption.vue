<template>
  <el-table :data="inventoriesStore.all" style="width: 100%">
    <el-table-column prop="title" label="物料" width="180" />
    <el-table-column prop="price" label="单价" width="180" />
    <el-table-column prop="inventory" label="库存" />
  </el-table>

  <br/><hr /><br/>
  <h1>Pinia 购物车示例</h1>
  <br /><hr /><br>
  <!-- <h2>商品列表</h2> -->
  <ShoppingList></ShoppingList>
  <br /><hr /><br>
  <!-- <h2>你的购物车</h2> -->
  <ShoppingCart></ShoppingCart>
</template>
  
<script lang="ts" setup>
import { useInventoriesStore } from '@/store/wms/inventory'
import { useWarehouseStore } from '@/store/wms/werehouse'

const inventoriesStore = useInventoriesStore()
const warehouseStore = useWarehouseStore()

inventoriesStore.loadAllInventories()

</script>
  