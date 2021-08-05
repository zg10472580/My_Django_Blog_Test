/* Style Switcher by Paul Sowden, see A List Apart: http://www.alistapart.com/articles/alternate/ */



function clock() {
    var d=new Date();
    var t=d.toLocaleTimeString();

    document.getElementsByTagName("body")[0].style.removeProperty("background")
    document.getElementsByTagName("body")[0].style.background = "url(https://source.unsplash.com/random)"

}
var intab;

function setActiveStyleSheet(title) {
    /*
        https://img.xjh.me/random_img.php     // 返回html
        https://source.unsplash.com/random    //重定向返回图片
        https://unsplash.it/1600/900?random   //重定向返回图片
     */

    if (title == "moren"){
        document.getElementsByTagName("body")[0].style.background = "#ffffff"
        clearInterval(intab);
        setCookie("bzs", "moren", 2);

    }else if (title == "suiji"){
        clock();
        intab = setInterval("clock()",10000);
        setCookie("bzs", "suiji", 2);
    }
}


$(function(){
    H_qqServer={};
    H_qqServer.clickOpenServer = function () {
        $('.skin-btn-open').click(function(){
            $('.skin-btn').animate({
                right: '-50'
            },400);
            $('.skin-content').animate({
                right: '0',
                opacity: 'show'
            }, 800 );
        });
        $('.skin-close').click(function(){
            $('.skin-btn').animate({
                right: '-7px',
                opacity: 'show'
            },400);
            $('.skin-content').animate({
                right: '-250',
                opacity: 'show'
            }, 800 );
        });
    };
    H_qqServer.run= function () {
        this.clickOpenServer();
    };
    H_qqServer.run();
});