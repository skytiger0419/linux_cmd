# 基本形式
``` javascript
<div id='app'>
    <h1>{{site}}</h1>
    <h2>{{name}}</h2>
    <h3>{{detail()}}</h3>
</div>
<script>
 new Vue({
  el: '#app',
  data: {
    site: 'http://www.baidu.com',
    name: '百度一下'
  }
  methods:{
      detail:function(){
          return this.site + this.name
      }
  }
})
</script>
```

## 相关语法
* v-model
``` html
    <div id="app">
    <p>{{ message }}</p>
    <input v-model="message">
</div>
```
* v-bind 简写：  :class
``` html
<div id="app">
  <label for="r1">修改颜色</label><input type="checkbox" v-model="class1" id="r1">
  <br><br>
  <div v-bind:class="{'class1': class1}">
    v-bind:class 指令
  </div>
</div>
    
<script>
new Vue({
    el: '#app',
  data:{
      class1: false
  }
});
</script>
```
* v-if
``` html
    <p v-if="seen">现在你看到我了</p>
```
* v-else
* v-else-if
* v-on:click 简写：@click
``` html
    <a v-on:click="doSomething">
    <form v-on:submit.prevent="onSubmit"></form>
```
* javascript 方法支持
``` html
<div id="app">
    {{5+5}}<br>
    {{ ok ? 'YES' : 'NO' }}<br>
    {{ message.split('').reverse().join('') }}
    <div v-bind:id="'list-' + id">菜鸟教程</div>
</div>
```

## 过滤器
* {{ message | filterA | filterB }} 串联
* {{ message | filterA('arg1', arg2) }} 参数传递
``` html
<div id="app">
    {{ message | capitalize }}
</div>
    
<script>
new Vue({
  el: '#app',
  data: {
    message: 'runoob'
  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
})
</script>
```


