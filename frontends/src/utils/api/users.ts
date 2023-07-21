import service from "@/utils/api/request"

// 用户登录，参数类型
type LoginInfo = {
    account: string
    code?: string
    password: string
}
// 用户登录，返回数据类型
type LoginResult = {
    success: boolean
    state: number
    message: string
    content: string
}
// 用户登录请求
export const login = (loginInfo: LoginInfo) => {
    return service<LoginResult>({
        method: "POST",
        url: "/drfdemo/user",                                                 // "/front/user/login",
        //data: 'phone=${loginInfo.phone}&password=${loginInfo.password}',    //数据类型=application/x-www.form-urlencoded
        data: loginInfo,     //数据类型=json

    })
}