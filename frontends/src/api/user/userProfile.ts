import service from "@/utils/request";

// 用户信息
type UserProfile = {
  id: number;
  username: string;
  password: string;
};
// 用户登录-返回数据类型
type LoginResult = {
  id: number;
  username: string;
  message: string;
  success: boolean;
  refresh: string;
  access: string;
  content: {
    isUpdatedPassword: boolean;
    portrait: string;
    username: string;
  };
};

// 获取用户信息
export const getUserProfile = () => {
  const res = service<UserProfile>({
    method: "GET",
    url: "/drfdemo/users/",
  });
  return res;
};

// export default getUserProfile
