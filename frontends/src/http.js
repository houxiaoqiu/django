// 导入网络请求库
import axios from 'axios';

const httptool = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});

export default httptool;
