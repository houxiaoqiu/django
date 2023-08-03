import axios from 'axios';

//1. 创建axios对象:请求实例
const service = axios.create({
  baseURL: import.meta.env.VITE_CVB_API_URL,
});

const drfdemo = axios.create({
  baseURL: "http://localhost:8000",
});

//2. 请求拦截器
service.interceptors.request.use(config => {
  return config;
}, error => {
  Promise.reject(error);
});

//3. 响应拦截器
service.interceptors.response.use(response => {
  //判断code码
  return response.data;
},error => {
  return Promise.reject(error);
});

export default drfdemo;