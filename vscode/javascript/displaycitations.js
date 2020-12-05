function displaycitations(){
    var quotes=document.getElementsByTagName('blockquote');
    for(var i=0;i<quotes.length;i++){
        if(!quotes[i].getAttribute('cite'))
        continue;
        var url=quotes[i].getAttribute('cite');
        var quotechilden=quotes[i].getElementsByTagName('*');
        if(quotechilden.length<1)
        continue;
        var elem=quotechilden[quotechilden.length-1];  //最后一个元素
        var link=document.createElement('a');
        var link_text=document.createTextNode('引用连接');
        link.appendChild(link_text);
        link.setAttribute('herf',url);
        var superscript=document.createElement('div')  //创建div元素节点，并把他存入变量superscript
        superscript.appendChild(link);
        elem.appendChild(superscript); //把标记superscript，添加到引用中的最后一个元素节点
    }
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
addLoadEvent(displaycitations);