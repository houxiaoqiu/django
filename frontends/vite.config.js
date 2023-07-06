import { defineConfig } from "vite";

const envResolver = {
    "build": () => ({ ...viteBaseConfig, ...viteProdConfig }),
    "serve": () => ({ ...viteBaseConfig, ...viteDevConfig })
}

// export default defineConfig( config : ({ command : "build" | "serve" , mode : string }) => {
//     return envResolver[command]();
// })