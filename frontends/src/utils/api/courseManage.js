import request from './request'

//获取1级分类
export function getFirstCategorys(){
	return request({
		url: '/api/course/category/getFirstCategorys',
	})
}

//获取二级分类
export function getSecondCategorys( params ){
	return request({
		url:'/api/course/category/getSecondCategorys',
		params
	})
}

//查询课程标签 
export function getTagsList(data){
	return request({
		url: '/api/course/tags/list',
		method: 'post',
		data
	})
}

//查询课程 
export function searchCourse(data){
	return request({
		url: '/api/course/search',
		method: 'post',
		data
	})
}

//轮播图  
export function  getSliders(){
	return request({
		url: '/api/slider/getSliders',
	})
}

//查询最新课程  
export function mostNewCourse(data){
	return request({
		url: '/api/course/mostNew',
		method: 'post',
		data
	})
}

//获取网站设置（网站登记信息） 
export function  getSetting(){
	return request({
		url: '/api/setting/get',		// http://testapi.xuexiluxian.cn/api/setting/get
	})
}

//课程详情
export function getCourseDetail( params ){
	return request({
		url:'/api/course/getDetail',		
		params,
	})
}