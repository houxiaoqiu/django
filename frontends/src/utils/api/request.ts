import { useTokenStore } from '@/store/token';
import axios, { AxiosRequestHeaders } from 'axios';

//1. 创建axios对象:请求实例
const service = axios.create({
  baseURL: import.meta.env.VITE_CVB_API_URL,
});

//2. 请求拦截器: 加载 token
service.interceptors.request.use(config => {
  if (!config.headers) {
    config.headers = {} as AxiosRequestHeaders
  }
  const tokenStore = useTokenStore()
  config.headers.Authorization = tokenStore.token
  console.log("request.intercepotrs 拦截器 - tokenStore.token：", tokenStore.token)
  return config;
}, error => {
  Promise.reject(error);
});
// service.interceptors.request.use(config => {
//   return config;
// }, error => {
//   Promise.reject(error);
// });

//3. 响应拦截器
// service.interceptors.response.use(response => {
//   //判断code码
//   return response.data;
// },error => {
//   return Promise.reject(error);
// });

export default  service