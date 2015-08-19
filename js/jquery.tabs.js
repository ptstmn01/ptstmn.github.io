$(document).ready(function(){

function Make_Tabsheet(){
var i, j, k, iMax_height, iDT_height

$("dl").each(function(i){
iMax_height=100;
iDT_height=20;
var bFirst_tab = true;
$(this).children('dt').mousedown(function(){
Switch_sheet(this)
})
$(this).children('dd').each(function(j){
if( $(this).height() > iMax_height ){
iMax_height = $(this).height()
}
if( !bFirst_tab ){
$(this).addClass("inactive")
}else{
$(this).addClass("active")
bFirst_tab = false
}
})
$(this).height((iMax_height)*1+"px")
$(this).children('dd').height(iMax_height + "px")
return false
})
}

function Switch_sheet( dt ){
$(dt).siblings('dt').removeClass('on')
var dd=$(dt).next('dd')
$(dt).siblings('dd').not(dd).removeClass('active').addClass('inactive')
$(dt).addClass('on')
$(dd).removeClass('inactive').addClass('active')
return false
}

Make_Tabsheet();

})