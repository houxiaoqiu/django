// 定义用户相关数据ts类型

// 用户登录-入参数据类型
export interface loginFormData {
    username: string
    password: string
};
// 用户登录-返回数据类型
export interface loginResult extends userResponseData {
    data: string
};
// 用户登录-用户信息数据类型
export interface userProfile extends userResponseData {
  data: {
    routes: string[]
    buttons: string[]
    roles: string[]
    name: string
    avatar: string
  }
};

//定义全部接口返回数据都拥有ts基类
export interface userResponseData {
  code: number
  message: string
  success: boolean
}