// 导入网络请求库
import axios from 'axios';

axios.create({
    baseURL: 'https://come-domain.com/api/',
    timeout: 10000,
    headers: {'X-Custom-Header': 'foobar'}
});

export default httptool;
