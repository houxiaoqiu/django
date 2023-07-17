// CBV-drfdemo API Manager
import request from './request'

//获取1级分类
export function getFirstCategorys(){
	return request({
		url: '/api/course/category/getFirstCategorys',
	})
}

//获取出版商
export function getPublishes(){
	return request({
		url: '/cbv/api/publish',        // http://127.0.0.1:8000/api/publish
	})
}