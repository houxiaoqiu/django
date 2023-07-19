// vite.config.js
import { defineConfig, loadEnv, ConfigEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import path from 'path'
 

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      imports:['vue','vue-router'],    //自动导入vue和vue-router相关函数
      resolvers: [
        ElementPlusResolver(),         //自动导入样式组件
        IconsResolver({               //自动导入图标组件
          prefix: 'Icon',
        }),
      ],
      eslintrc: {enabled: true},
    }),
    Components({
      resolvers: [
        ElementPlusResolver(),        //自动注册样式组件
        IconsResolver({               //自动注册图标组件
          enabledCollections: ['ep'],
        }),
      ],
    }),
    Icons({                           //自动安装图表组件
      autoInstall: true,
    }),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname,'src')
    },
  },
  server:{
		proxy:{
			'/api': {
        target: loadEnv("", process.cwd()).VITE_XXLX_API_URL,  //'http://testapi.xuexiluxian.cn',
        changeOrigin: true,
      },
      '/cbv': {
        target: loadEnv("",process.cwd()).VITE_CVB_API_URL,  //'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/front': {
        // http://39.97.218.60/front/ad/getAdList
        target: loadEnv("",process.cwd()).VITE_USER_API_URL,  //'http://127.0.0.1:8000',
        changeOrigin: true,
      }
		}
	}
})