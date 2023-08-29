import service from "@/utils/request";
import { loginFormData, loginResult, userProfile } from "./type";

// // 用户登录-参数类型
// type LoginInfo = {
//   username: string;
//   password: string;
// };
// // 用户登录-返回数据类型
// type LoginResult = {
//   id: number;
//   username: string;
//   message: string;
//   success: boolean;
//   refresh: string;
//   access: string;
//   content: {
//     isUpdatedPassword: boolean;
//     portrait: string;
//     username: string;
//   };
// };
// //获取用户信息
// type UserProfile = {
//   id: number;
//   username: string;
//   avatar: string;
// };
// 项目用户相关的请求地址
enum API {
  LOGIN_URL = '/defdemo/api/login',
  USERINFO_URL = '/defdemo/users',
  LOGOUT_RUL = '/defdemo/api/logout'
}

// 用户登入接口
export const login = async (loginInfo: loginFormData) => {
  const res = await service<loginResult>({
    method: "POST",
    url: "/drfdemo/login/",
    data: loginInfo,
  });
  return res;
};
export const reqLogin = (data: loginFormData) =>
  service.post<loginFormData, loginResult>(API.LOGIN_URL)

// 用户信息接口
export const getUserProfile = () => {
  return service<userProfile>({
    method: "GET",
    url: "/drfdemo/users/1",
  });
};
export const reqUserProfile = () =>
  service.post<any, userProfile>(API.USERINFO_URL)

  // 退出登录接口
export const reqLogout = () => service.post<any, any>(API.LOGOUT_RUL)

