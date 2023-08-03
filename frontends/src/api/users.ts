import drfdemo from "@/utils/api/request"

// 用户登录-参数类型
type LoginInfo = {
    username: string
    password: string
}
// 用户登录-返回数据类型
type LoginResult = {
    id: number
    username: string
    mobile: string
    email: string
    token: string
    refresh: string
}

// 用户请求登录
export const login = (loginInfo: LoginInfo) => {
    return drfdemo<LoginResult>({
        method: "POST",
        url: '/drfdemo/login/',
        data: loginInfo,
    })
}
/**
 * 请求类型 application/x-www.form-fulencoded
 *      拼接：data: '属性1=值1&属性2=值2'
 * 请求类型 application/json
 *      对象：data: loginInfo
 */