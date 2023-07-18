// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
 
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
  // resolve: {
  //   alias: {
  //     "@": fileURLToPath(new URL("./src", import.meta.url))
  //   },
  // },
  server:{
		proxy:{
			'/api':'http://testapi.xuexiluxian.cn',
      '/cbv': 'http://127.0.0.1:8000'
		}
	}
})