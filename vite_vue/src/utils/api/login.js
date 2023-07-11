import request from './request'

//用户名/密码登录
export function loginByJson( data ){
    return request({
        url: '/api/u/loginByJson',
        methond: 'post',
        data
    })
}