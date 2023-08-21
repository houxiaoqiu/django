/***
 * src/api/wms/inventory.ts
 * Mocking client-server processing
 */
export interface IInventory {
    id: number
    title: string
    price: number
    inventory: number
}

const _inventories: IInventory[] = [
    {id: 1, title: 'IPad 4 Mini', price: 500.01, inventory: 2},
    {id: 2, title: 'H&M T-Shirt White', price: 10.99, inventory: 20},
    {id: 3, title: 'Charli XCS - Sucker CD', price: 19.99, inventory: 5},
]

export const getInventories = async () => {
    await wait(100)
    return _inventories
}

export const buyInventories = async () => {
    await wait(100)
    return Math.random() > 0.5
}

async function wait(delay: number) {
    return new Promise((resolve) => setTimeout(resolve, delay))
}