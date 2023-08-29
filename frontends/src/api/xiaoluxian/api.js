import request from './request';

// 小路线
const userApi = {
    login: (data) => {
        return request({
            url: 'user/login',
            method: 'post',
            data: data,
            params: {
                noToken: true,
            },
        });
    },

    myPage: () => {
        return request({
            url: 'userAccount',
            method: "get",
        });
    },

    address: (data) => {
        return request({
            url: '/user/wallet/add/address2',
            method: "post",
            data: data,
        });
    },
};