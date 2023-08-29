import { useTokenStore } from "@/utils/token";
import axios, { AxiosRequestHeaders } from "axios";
import router from "@/router/index";

// 1. 创建axios对象: 请求实例, 二次封装
const service = axios.create({
  baseURL: import.meta.env.VITE_CVB_API_URL,
  timeout: 5000,
});

// 2. 请求拦截器: 头部加载 token
service.interceptors.request.use(
  (config) => {
    if (!config.headers) {
      config.headers = {} as AxiosRequestHeaders;
    }
    const tokenStore = useTokenStore();
    config.headers.Authorization = tokenStore.token;
    console.log(
      "tuils/api/request.ts 拦截器 - tokenStore.token：",
      tokenStore.token
    );
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);

// 3. 响应拦截器
service.interceptors.response.use(
  (response) => {
    // if(response.code == ?)    //判断code码
    return response;
  },
  (error) => {
    let message = "";
    const status = error.response.status;
    switch (status) {
      case 401:
        message = "TOKEN过期";
        break;
      case 403:
        message = "无权访问";
        break;
      case 404:
        message = "请求地址错误";
        break;
      case 500:
        message = "服务器出现问题";
        break;
      default:
        message = "网络出现问题";
        break;
    }
    ElMessage({
      type: "error",
      message,
    });
    return Promise.reject(error);
  }
);

export default service;
