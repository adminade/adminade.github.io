function displayaccesskeys(){
    var links=document.getElementsByTagName('a');
    var akeys= new Array();
    for (var i=0;i<links.length;i++){
        var current_link=links[i];
        if (!current_link.getAttribute('accesskey')) continue;
        var key=current_link.getAttribute('accesskey');
        var text=current_link.lastChild.nodeValue;
        akeys[key]=text;  //添加到数组
        var list=document.createElement('ul');
        for (key in akeys){
            var text=akeys[key];
            var str=key+':'+text;
            var item=document.createElement('li');
            var item_text=document.createTextNode(str);
            item.appendChild(item_text);
            list.appendChild(item);
        }
        var header=document.createElement('h3');
        var header_text=document.createTextNode('accesskeys');
        header.appendChild(header_text);
        document.body.appendChild(header);
        document.body.appendChild(list);
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
addLoadEvent(displayaccesskeys);