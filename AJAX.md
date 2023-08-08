## AJAX

### 传统请求及缺点

* 传统请求有哪些？
  * 直接在地址栏上输入地址
  * 超链接
  * form表单
  * JS发送请求
    * window.open(url)
    * document.location.href = url
    * .......
* 传统请求的问题
  * 页面全部刷新导致了用户的体验感较差
  * 传统的请求导致用户的体验感有空白期。(用户的体验是不连续的)

### XMLHttpRequest对象

* XMLHttpRequest对象是ajax的核心对象，发送请求以及接收服务器数据的返回全依赖它。

* XMLHttpRequest对象，现代浏览器都是支持的，都内置了该对象，直接用即可。

* 创建XMLHttpRequest对象

  * ```
    var xhr = new XMLHttpRequest();
    ```

* XMLHttpRequest对象的方法：
  * open(method,url,async,user,psw)
    * method：请求的方式，GET、POST
    * url:请求的路径
    * async：只能是true或false，true表示AJAX是一个异步请求，false表示同步请求
    * user：用户名、 psw:密码
  * send() ：将请求发送到服务器，用于GET请求
  * send(string) ：将请求发送到服务器，用于POST请求
  
* XMLHttpRequest对象的readyState属性：

  * 0：请求未初始化
  * 1：服务器连接已建立
  * 2：请求已收到
  * 3：正在处理请求
  * 4：请求已完成且响应已就绪

* onreadystatechange :定义当readyState属性发生变化时被调用的函数

* responseText ：以字符串返回响应数据

* responseXML ：以XML数据返回响应数据

* status : 返回请求的状态号

* statusText ：返回状态文本

### 发送AJAX 的get请求

* 前端代码

  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>OA</title>
  </head>
  <body>
  <script type="text/javascript">
      window.onload = function () {
          //点击事件
          document.getElementById("bt01").onclick = function () {
              //创建XMLHttpRequest对象
              var xhr = new XMLHttpRequest();
              //注册回调函数
              xhr.onreadystatechange = function () {
                  if (this.readyState == 4){
                      if(this.status == 200){
                          document.getElementById("div01").innerHTML = this.responseText
                      }else{
                          alert(this.status)
                      }
                  }
              }
              //获取输入框中信息
              var username = document.getElementById("t01").value;
              var password = document.getElementById("t02").value;
              xhr.open("GET","/ajax02/request?username="+username+"&password="+password,true)
              xhr.send()
          }
      }
  </script>
  
  账号:<input type="text" name="username" id="t01"><br>
  密码:<input type="text" name="password" id="t02"><br>
  <input type="button" value="button01" id="bt01"><br>
  <div id="div01"></div>
  </body>
  </html>
  ```

* 后端代码

  ```
  @WebServlet("/request")
  public class AjaxRequest extends HttpServlet {
      @Override
      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
          resp.setContentType("text/html;charset=UTF-8");
          PrintWriter out = resp.getWriter();
          String username = req.getParameter("username");
          String password = req.getParameter("password");
  
  
          out.print("username = " + username + " password = " + password);
      }
  }
  ```

* AJAX的get请求如何提交数据给服务器呢？

  * get请求提交数据是在“请求行”上提交，格式：url?name=value&name=value.....
  * 其实这个get请求提交数据的格式是HTTP协议中规定的，遵循协议即可。

### AJAX GET请求的缓存问题

* 对于低版本的IE浏览器来说，AJAX的get请求可能会走缓存，存在缓存问题，对于现代的浏览器来说，大部分浏览器都已经不存在AJAX get缓存问题了。
* 什么是AJAX get请求缓存问题？
  * 在HTTP协议中是这样规定get请求的：get请求会被缓存起来。
  * 发送AJAX get 请求时，在同一个浏览器上，前后发送的AJAX请求路径也一样的话，对于低版本的IE来说，第二次AJAX get请求会走缓存，不走服务器。
* POST请求在HTTP协议中规定的是：POST请求不会被浏览器缓存。
* GET请求缓存的优缺点：
  * 优点：直接从浏览器缓存中获取资源，不需要从服务器上重新加载资源，速度较快，用户体验好。
  * 缺点：无法实现实时获取最新的服务器资源。
* 浏览器什么时候会走缓存？
  * 第一：是一个get请求
  * 第二：请求路径已经被浏览器缓存过了，第二次发送请求的时候，这个路径没有变化，会走浏览器缓存。
* 如何解决低版本IE浏览器的AJAX get请求的缓存问题：
  * 请求路径url后添加一个时间戳，这个时间戳是随时变化的，所以每一次发送的请求路径都是不一样的，这样就不会走浏览器的缓存问题了。
  * 可以采用时间戳："url?="+new Date().getTime()
  * 或者通过随机数："url?="+ Math.random()

### AJAX POST请求

### AJAX 的POST请求模拟表单提交数据

* POST请求和GET请求区别在前段代码，后端代码没有区别

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OA</title>
</head>
<body>
<script type="text/javascript">
    window.onload = function () {
        //点击事件
        document.getElementById("bt01").onclick = function () {
            //创建XMLHttpRequest对象
            var xhr = new XMLHttpRequest();
            //注册回调函数
            xhr.onreadystatechange = function () {
                if (this.readyState == 4){
                    if(this.status == 200){
                        document.getElementById("div01").innerHTML = this.responseText
                    }else{
                        alert(this.status)
                    }
                }
            }
            xhr.open("POST","/ajax02/request,true)
                     
            //设置请求头的内容类型(这行代码非常关键，是模拟form表单提交的关键代码)
            //注:这行代码不能放在open()函数后面，send()方法之前
            xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded")
            //获取输入框中信息
            var username = document.getElementById("t01").value;
            var password = document.getElementById("t02").value;
            //模拟form表单发送数据，注意与GET请求的区别
            xhr.send("username="+username+"&password="+password)
        }
    }
</script>

账号:<input type="text" name="username" id="t01"><br>
密码:<input type="text" name="password" id="t02"><br>
<input type="button" value="button01" id="bt01"><br>
<div id="div01"></div>
</body>
</html>
```

* 实现一个案例：使用AJAX的POST请求实现用户注册的时候，用户名是否可用。(验证用户名是否可以注册)

```
```



### 基于JSON的数据交换

* 如何把服务器端响应的字符串转化为JSON对象

  ```js
  var fromJavaServerJsonStr = "{\"username\":111,\"age\":20}"
  //两种方式:
  //第一种:使用eval函数
  //第二种:使用JavaScript语言中的内置对象JSON的一个方法parse.
  var jsonobj = JSON.parse(fromJavaServerJsonStr)
  alert(jsonobj.usercode + "," + jsonobj.age)
  ```


* 1

* 使用fastjson组件把java对象转化为json格式的字符串

  ```java
  List<Student> stulist = new ArrayList<>();
  while(rs.next()){
      String name = rs.getString("name");
      String age = rs.getInt("age");
      String addr = rs.getString("addr");
      Student s = new Student(name,age,addr);
      stulist.add(s);
  }
  //把List集合转化为JSON字符串
  jsonStr = JSON.toJSONString(stulist);
  ```

  * 注意：需要引入fastjson的jar包

### 基于XML的数据交换

* 注意：如果服务器端响应XML的话，响应的内容类型需要写成:

  ```
  response.setContentType("text/xml;charset=UTF-8")
  ```

* xml和JSON都是常用的数据交换格式

  * XML体积大，解析麻烦，较少用
  * JSON体积小，解析简单，较常用。

* ```
  ```

* 

### AJAX乱码问题

* 测试内容：

  * 发送ajax get请求
    * 发送数据到服务器，服务器获取的数据是否乱码？
    * 服务器响应给前段的中文，会不会出现乱码？
  * 发送ajax post请求
    * 发送数据到服务器，服务器获取的数据是否乱码？
    * 服务器响应给前段的中文，会不会出现乱码？

* 还要测试Tomcat版本

  * Tomcat10和Tomcat9都要进行版本的测试

* 测试结果：

  * 对于Tomcat10来说，关于字符集，程序员不需要干预，不会出现乱码的问题

  * 对于Tomcat9包括之前的版本来说:

    * 响应中文的时候会出现乱码。怎么解决？

      ```
      response.setContentType("text/html;charset=UTF-8");
      ```

    * 发送ajax post请求的时候，发送给服务器的数据，服务器接收之后乱码怎么解决？

      ```
      request.setCharacterEncoding("UTF-8");
      ```

      

### AJAX的异步与同步

* 什么是异步？什么是同步？

  * ajax请求1和请求2，同时并发谁也不用等谁，这就是异步。
  * ajax请求1和请求2，在请求1发送的时候需要等待请求2结束之后才能发送，这是同步请求。

  ```html
  //同步请求
  xhr.open("请求方式","URL",false)
  xhr.send()
  //异步请求
  xhr.open("请求方式","URL",true)
  xhr.send()
  ```

* 什么情况下使用同步？
  * 例如：用户注册
    * 用户名需要校验
    * 邮箱地址需要校验
    * .....
    * 最终只有上面校验完成后，点击注册才能符合要就，否则会出现非法数据

### AJAX代码封装

* ajax请求相关的代码都是类似的，有很多重复的代码，因此封装这些重复的代码，然后直接调用即可。
* 接下来封装一个JS库，这个库记名jQuery

* 引入jQuery库

  ```html
  <script type="text/javascript" src="js/jQuery-1.0.0.js"> </script>
  ```

### AJAX请求封装到jQuery库中

* 注:类的静态方法的调用的前提是，该类必须创建了对象

### AJAX实现省市联动



### AJAX跨域问题

```html
1、超链接可以跨域
<a href="....."></a>
2、form表单可以跨域
<form action="http://localhost:8081/ajax06/getrequest">
    账号:<input type="text" name="username"><br>
    密码:<input type="text" name="password"><br>
    <input type="submit" value="提交">
</form>
3、js代码中的window.location.href或document.location.href可以跨域
<button onclick="window.location.href='http://localhost:8081/ajax06/index01.html'">按钮</button>
4、可以跨域加载js文件
<script type="text/javasrcipt" src="http:localhost:8081/ajax06/my.js"></script>
5、可以跨域加载图片
<img src="http://localhost:8081/ajax06/Session会话过程.png">
```

* 跨域是指从一个域名的网页去请求另一个域名的资源，比如从百度(https://baidu.com)页面去京东(http://www.jd.com)的资源。
* 通过超链接或form表单提交或者window.location.href的方式进行跨域是不存在问题的，但是一个域名的网页中的一段js代码发送ajax请求去访问另一个域名中的资源，由于同源策略的存在导致无法跨域访问，那么ajax就存在这种跨域问题。
* 同源策略有什么用？如果你刚刚在网银输入账号密码，查看自己还有1万元，紧接着访问一些不规则的网站，这个网站可以访问刚刚的网银密码，这是不安全的，所以同源策略是有利于保护网站信息。
* 有一些情况下，我们是需要使用ajax进行跨域访问的，比如某公司的A页面可能获取B公司页面。
* ajax是不能进行跨域访问的 ，只有进行以下设置才可以。

##### 什么是同源策略

* 协议一致，域名一致，端口号一致
* 只要上面的任一元素不一致，就不是同源。
* 同源，XMLHttpRequest对象可以共享
* 不同源，XMLRequest对象不可以共享

### 复现Ajax跨域问题(解决方案)

#### 方案1：设置响应头

* 核心原理：跨域访问的资源允许你跨域访问

* 实现：

  ```java
  response.setHeader("Access-Control-Allow-Origin","http://localhost:8080");//允许某个
  response.setHeader("Access-Control-Allow-Origin","*")//允许所有
  ```

#### 方案2：jsonp(主要是Script的src为一个servlet)

* jsonp：json with padding(带填充的json)
* jsonp不是一个真正的ajaxq请求，只不过可以完成ajax的局部刷新效果，可以说jsonp是一种类ajax的请求机制。
* jsonp不是ajax请求，但是可以完成局部的刷新效果，并且可以解决跨域问题。
* 注意：jsonp解决跨域的时候，只支持GET请求，不支持POST请求。

##### jsonp深入理解(实现局部刷新)

```javascript
<script type="text/javascript">
    sayCall = function(ar){
        document.getElementById("div").innerHTML = ar
    }
    /**
     * 1、创建属性
     * 2、添加type、src属性
     * 3、将script标签加入srcipt中
     */
    window.onload = function () {
        document.getElementById("bt").onclick = function () {
            var htmlScriptElement = document.createElement("script")
            htmlScriptElement.type = "text/javascript"
            htmlScriptElement.src = "http://localhost:8081/ajax06/getrequest02?fun=sayCall"
            document.getElementsByTagName("body")[0].appendChild(htmlScriptElement)
        }
    }
</script>

<input type="button" value="jsonp实现局部刷新" id="bt">
<div id="div"></div>
```



#### 方案3：jQuery封装的jsonp

* 使用之前需要引入jQuery库的js文件。

* jQuery中的jsonp其实就是方案2的高度封装，底层原理完全相同

* 核心代码

  ```javascript
  $.ajax({
      type:"GET",
      url:"跨域的url",
      dataType:"jsonp",//指定数据类型
      jsonp:"fun",//指定参数名(不设置的时候，默认是“callback”)
      jsonpCallback:"sayHello" //指定回调函数的名字，不设置的时候，jQuery会自动生成一个随机的回调函数，并且这个回调函数还会自动调用success的回调函数。
  })
  ```

#### 方案4：代理机制

* 使用java程序如何发送get/post请求呢？
  * 第一种方案：使用JDK内置的API
  * 第二种方案：使用第三方的开源组件，比如apache的httpclient组件。
* 在java程序中，使用httpclient组件可以发送http请求
  * 使用httpclient组件，需要先将这个组件相关的jar包引入到项目当中。



### Ajax实现搜索联想和自动补全的实现原理

* 搜索联想，自动补全的核心实现原理
  * 当键盘时间发生之后，比如：keyup 键弹起事件
  * 发送ajax请求，请求中提交用户输入的搜索内容，例如：北京(发送ajax请求，携带“北京”两个字)
  * 后端收到ajax请求，接收到“北京”两个字，执行select语句进行模糊查询，返回查询结果集。
  * 将查询结果集封装成json格式的字符串，将json格式字符串响应到前段。
  * 前段接收到json格式的字符串之后，解析这个json字符串，动态展示页面。















