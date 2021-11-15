1. 使用 vue-cli 创建 vue3 项目
2. 清空模板
3. 创建目录结构
4. 创建模板 css
5. 配置router
6. 


bug
Q: 明明都修改了100vw100vh但还是能滑动
A: 给 app 加一个 position: fixed 的属性

Q: 字符串空格
A: 可以使用 v-html，也可以使用 &nbsp;，也可以使用 \u3000

# app

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
