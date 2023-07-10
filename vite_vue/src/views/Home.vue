<template>
	<Header></Header>
	<NavSwiper></NavSwiper>
	<div ref="target">
		<NewGoodCourse v-if='targetIsVisible'></NewGoodCourse>
	</div>
	<Foot></Foot>
</template>

<script setup>
import { useIntersectionObserver } from '@vueuse/core'

import Header from '../components/common/Header.vue'
import NavSwiper from '../components/home/NavSwiper.vue'

const NewGoodCourse = defineAsyncComponent(() =>
  import('../components/home/NewGoodCourse.vue')
)

const target = ref(null);
const targetIsVisible = ref(false);

const { stop } = useIntersectionObserver(
  target,
  ([{ isIntersecting }]) => {
  	if( isIntersecting ) {
  		targetIsVisible.value = isIntersecting
  	}
  },
)

import Foot from '../components/common/Foot.vue'

</script>