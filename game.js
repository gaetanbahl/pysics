drawShape = function(x,y,size,rotation){
    x=Math.round(x);
    y=Math.round(y);

    context.save()
    context.translate(x,y);
    context.scale(size,size);
    context.rotate(rotation);
    context.beginPath();
    context.lineWidth=0.3;
    context.lineJoin="miter";
    context.moveTo(-1,-1);
    context.lineTo(+1,0);
    context.lineTo(-1,+1);
    context.lineTo(-0.5,0);
    context.lineTo(-1,-1);
    context.closePath();
    context.strokeStyle = '#0F0';
    context.stroke();
    context.restore()
    return;
}
   
var fps = 30;
var framet = 1000/fps;
var canvas;
var context;
var width = window.innerWidth;
var height = window.innerHeight;

window.onload = function(){
    canvas = document.getElementById('canvas');
    if(!canvas)
        alert("Impossible de charger le canvas");

    canvas.width = width;
    canvas.height = height;

    context = canvas.getContext('2d');
    if(!context)
        alert("Impossible de charger le context");

    context.webkitImageSmoothingEnabled = false;


    setInterval(proc, framet);

}

proc = function(){

    getall();

    context.rect(0,0,width,height);

    if(req_getall!=""){
        context.fillColor=("black");
        context.fill();
        var reqres = req_getall.split('\n');
        if(reqres.length>0)
            for(var i=0 ; i <reqres.length ; i++){
                tempreq = reqres[i].split(' ');
                x=parseFloat(tempreq[0]);
                y=parseFloat(tempreq[1]);
                rot=parseFloat(tempreq[2]);
                drawShape(x+width/2,y+height/2,20,rot);
            }

        //req_getall="";
    }else{
        context.fillColor=("red");
        context.fill();
    }



}

