//统一管理咱们项目用户相关的接口
import request from '@/utils/request'
import type {
  loginFormData,
  loginResult,
  userProfile,
//   loginResponseData,
//   userInfoReponseData,
} from './type'
//项目用户相关的请求地址
enum API {
  LOGIN_URL = '/drfdemo/api/login',
  USERINFO_URL = '/drfdemo/api/users',
  LOGOUT_URL = '/defdemo/api/logout',
//   LOGIN_URL = '/admin/acl/index/login',
//   USERINFO_URL = '/admin/acl/index/info',
//   LOGOUT_URL = '/admin/acl/index/logout',
}

//登录接口
export const reqLogin = (data: loginFormData) =>
  request.post<any, loginResult>(API.LOGIN_URL, data)
//获取用户信息
export const reqUserInfo = () =>
  request.get<any, userProfile>(API.USERINFO_URL)
//退出登录
export const reqLogout = () => request.post<any, any>(API.LOGOUT_URL)
