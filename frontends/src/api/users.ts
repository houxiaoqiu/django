import service from "@/utils/api/request"

// 用户登录-参数类型
type LoginInfo = {
    username: string
    password: string
};
// 用户登录-返回数据类型
type LoginResult = {
    id: number
    username: string
    message: string
    success: boolean
    refresh: string
    access: string
    content: {
        isUpdatedPassword: boolean
        portrait: string
        username: string
    }
};

// 用户请求登录
export const login = async (loginInfo: LoginInfo) => {
    const res = await service<LoginResult>({
        method: "POST",
        url: '/drfdemo/login/',
        data: loginInfo,
    })
    return res
};

//获取用户信息
type UserProfile = {
    id: number
    username: string
    avatar: string 
};

export const getUserProfile = () => {
    return service<UserProfile>({
        method: "GET",
        url: "/drfdemo/users/1/",
    })
};

/**
 * 请求类型 application/x-www.form-fulencoded
 *      拼接：data: '属性1=值1&属性2=值2'
 * 请求类型 application/json
 *      对象：data: loginInfo
 */