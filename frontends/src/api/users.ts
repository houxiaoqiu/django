import service from "@/utils/api/request"

// 用户登录-参数类型
type LoginInfo = {
    username: string
    password: string
}
// 用户登录-返回数据类型
type LoginResult = {
    id: number
    username: string
    message: string
    success: boolean
    refresh: string
    access: string
}

// 用户请求登录
export const login = async (loginInfo: LoginInfo) => {
    const res = await service<LoginResult>({
        method: "POST",
        url: '/drfdemo/login/',
        data: loginInfo,
    })
    return res
}
/**
 * 请求类型 application/x-www.form-fulencoded
 *      拼接：data: '属性1=值1&属性2=值2'
 * 请求类型 application/json
 *      对象：data: loginInfo
 */