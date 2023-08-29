<template>
    <Header></Header>
    <NavSwiper></NavSwiper>
    <div ref="target">
		<NewGoodCourse v-if='targetIsVisible'></NewGoodCourse>
	</div>
    <Footer></Footer>
</template>

<script setup lang="ts">

    import { ref, defineAsyncComponent } from 'vue'
    import { useIntersectionObserver } from '@vueuse/core'
    import Header from '@/components/common/Header.vue'
    import NavSwiper from '@/components/home/NavSwiper.vue'
    import Footer from '@/components/common/Footer.vue'

    const NewGoodCourse = defineAsyncComponent(() =>
    import('@/components/home/NewGoodCourse.vue')
    );

    const target = ref(null);
    const targetIsVisible = ref(false);

    const { stop } = useIntersectionObserver(
    target,
    ([{ isIntersecting }]) => {
        if( isIntersecting ) {
            targetIsVisible.value = isIntersecting
        }
    },
    );

</script>
