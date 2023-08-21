<script setup lang="ts">

// #region ts接口

interface ITableRow {
    name: string,
    age: number,
    random: number
}

interface IPage {
    currentPage: number
    pageSize: number
    total: number
}

// #endregion ts接口

onMounted(() => {
    getList()
})

// #region 表格

// 分页数据, 本例由于动态表格封装所以弄了一个
const pagination = ref<IPage>({
    currentPage: 1,
    pageSize: 10,
    total: 0
})

const tableData = ref<ITableRow[]>([])

// 获取列表
const getList = () => {
    const list: ITableRow[] = []
    for (let i = 0; i < 5; i++) {
        list.push({
            name: '姓名' + Math.floor(Math.random() * 10),
            age: Math.floor(Math.random() * 100),
            random: Math.random()
        })
    }
    tableData.value = list
}

// #endregion 表格

</script>

<template>
    <div class="home">
        <div class="home-buttons">
            <div class="home-buttons-opra">
                <el-button type="primary">没用,占位</el-button>
            </div>
            <div class="home-buttons-tools">
                <ColumnControl />
            </div>
        </div>
        <div class="home-list">
            <!-- 如果要隐藏多选或者序号或者你扩展了什么 <ProjectTable hiddenIndex> 你懂得! -->
            <ProjectTable :pagination="pagination" :data="tableData">
                <!-- 使用时就正常使用，不需要写for循环 -->
                <el-table-column prop="name" label="姓名" />
                <el-table-column prop="age" label="年龄" />
                <el-table-column prop="random" label="随机数" />
            </ProjectTable>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.home {
    width: 700px;
    display: flex;
    flex-direction: column;

    &-buttons {
        margin-bottom: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}
</style>
