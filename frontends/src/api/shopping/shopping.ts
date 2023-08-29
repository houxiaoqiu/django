/***
 * src/api/shopping.ts
 * Mocking client-server processing
 */
export interface IProduct {
    id: Number
    title: String
    price: Number
    inventory: Number
}

const _products: IProduct[] = [
    {id: 1, title: 'IPad 4 Mini', price: 500.01, inventory: 2},
    {id: 2, title: 'H&M T-Shirt White', price: 10.99, inventory: 20},
    {id: 3, title: 'Charli XCS - Sucker CD', price: 19.99, inventory: 5},
]

export const getProducts = async () => {
    await wait(100)
    return _products
}

export const buyProducts = async () => {
    await wait(100)
    return Math.random() > 0.5      // 随机：支付结算 
}

async function wait(delay: number) {
    return new Promise((resolve) => setTimeout(resolve, delay))
}