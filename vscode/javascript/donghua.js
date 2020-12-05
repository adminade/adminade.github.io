function setpostion(){
    var elem=document.getElementsByTagName('img');
    // elem.style.position="absolute";
    elem.style.top="100px";
    elem.style.left="100px";
    alert(elem.style.top)

}
function move(){
    var elem=document.getElementsByTagName("img");
    var xpos=parseInt(elem.style.left);   // parseint函数可以把字符串里的数值信息提出来,因为 style.left 得到单位是 px， so 需要这个函数
    var ypos=parseInt(elem.style.top);
    if(xpos==500&&ypos==500)
    return true;
    if(xpos<500)
        xpos++;
    if(ypos<500)
        ypos++;
    elem.style.left=xpos+'px';
    elem.style.top=ypos+'px';
    movement=setTimeout(move,1000);

}
function addLoadEvent(func) {
    var oldonload = window.onload;//将现有的事件处理函数的值存入变量中
    if (typeof window.onload != 'function') {
        window.onload = func;//如果这个事件处理函数没有绑定任何函数，就把新函数添加给它
    } else {
        window.onload = function() {
            oldonload();
            func();//如果已经绑定了函数，就把新函数追加到现有指令的末尾
      }
    }
}
addLoadEvent(setpostion);
addLoadEvent(move)